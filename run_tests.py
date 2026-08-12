"""CSV-driven test runner for the AlgoInfinity solution files.

Usage:
    python run_tests.py                          # auto-discover every main.py under the repo
    python run_tests.py <path/to/main.py>        # run a single solution's tests
    python main.py                               # also runs its own tests via __main__

Each solution lives next to a test_cases.csv whose rows look like:

    name,function,args,expected
    basic,isValidParentheses,"[""()"",""()[]{}""]",true

Cells `args` and `expected` are JSON values. `args` is decoded to *args and
`kwargs` (optional column) to **kwargs. The `function` column picks which
method on the Solution class to call, so multiple solution tiers can share
one test file.

Requires `rich` (see requirements.txt) but degrades to plain ANSI output if
it is not installed.
"""

from __future__ import annotations

import argparse
import csv
import importlib.util
import json
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
TEST_FILE = "test_cases.csv"

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    from rich.text import Text

    _HAS_RICH = True
except ImportError:  # pragma: no cover
    _HAS_RICH = False

    class Console:
        def __init__(self):
            pass

        def print(self, *args, **kwargs):
            print(*args)


def _import_module_from_path(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _discover_solutions() -> list[Path]:
    """Return every main.py under REPO_ROOT that has a sibling test_cases.csv."""
    results = []
    for path in REPO_ROOT.rglob("main.py"):
        if ".git" in path.parts:
            continue
        if path.parent.joinpath(TEST_FILE).exists():
            results.append(path)
    return sorted(results)


def _load_cases(csv_path: Path) -> list[dict]:
    with csv_path.open(newline="") as fh:
        return list(csv.DictReader(fh))


def _decode(row: dict) -> tuple:
    defaults = {"args": "[]", "kwargs": "{}", "expected": "null"}
    for field in ("args", "kwargs", "expected"):
        cell = row.get(field) or defaults[field]
        try:
            if field == "args":
                args = json.loads(cell)
            elif field == "kwargs":
                kwargs = json.loads(cell)
            else:
                expected = json.loads(cell)
        except json.JSONDecodeError as exc:
            raise ValueError(
                f"{field!r} cell is not valid JSON in test case {row.get('name')!r}: {exc}. "
                'Remember: JSON strings must be quoted, e.g. bare `ca` must be written as "ca".'
            ) from None
    return args, kwargs, expected


def _run_single(console, solution_cls, row) -> tuple[bool, float, object, str | None]:
    function = row.get("function") or "solution"
    args, kwargs, expected = _decode(row)

    if not hasattr(solution_cls, function):
        return False, 0.0, None, f"Solution has no method {function!r}"

    started = time.perf_counter()
    try:
        result = getattr(solution_cls(), function)(*args, **kwargs)
        elapsed_ms = (time.perf_counter() - started) * 1000
        return result == expected, elapsed_ms, result, None
    except Exception as exc:
        elapsed_ms = (time.perf_counter() - started) * 1000
        return False, elapsed_ms, None, f"raised {type(exc).__name__}: {exc}"


def _render_result(console, row, ok, elapsed_ms, error, expected, got):
    name = row.get("name") or "case"
    function = row.get("function") or "solution"
    args, kwargs, _ = _decode(row)

    if _HAS_RICH:
        badge = (
            Text("PASS", style="bold green") if ok else Text("FAIL", style="bold red")
        )
        desc = Text()
        desc.append(f"{name}  ", style="bold")
        desc.append(f"[{function}({_format_args(args, kwargs)})] ", style="dim")
        desc.append(f"{elapsed_ms:.2f} ms", style="dim")
        console.print(badge, desc)
        if not ok:
            if error:
                console.print(f"      [dim]input:[/dim] {_format_args(args, kwargs)}")
                console.print(f"      [red]{error}[/red]")
            else:
                console.print(f"      [dim]input:[/dim] {_format_args(args, kwargs)}")
                console.print(f"      [green]expected:[/green] {_pp(expected)}")
                console.print(f"      [red]got:[/red]      {_pp(got)}")
    else:  # pragma: no cover
        status = "PASS" if ok else "FAIL"
        console.print(f"[{status}] {name} ({function}): {elapsed_ms:.2f} ms")
        if not ok:
            console.print(f"    expected: {_pp(expected)}")
            console.print(f"    got:      {_pp(got)}")
            if error:
                console.print(f"    {error}")


def _format_args(args, kwargs) -> str:
    parts = [json.dumps(a, ensure_ascii=False) for a in args]
    parts += [f"{k}={json.dumps(v, ensure_ascii=False)}" for k, v in kwargs.items()]
    return ", ".join(parts)


def _pp(value) -> str:
    return json.dumps(value, indent=2, ensure_ascii=False, default=str)


def run_tests_for(main_py: str | Path) -> tuple[int, int, int, float]:
    """Run every CSV case for a solution. Returns (passed, failed, total, total_ms)."""
    main_path = Path(main_py).resolve()
    csv_path = main_path.parent.joinpath(TEST_FILE)
    console = Console()

    if not csv_path.exists():
        console.print(
            f"[bold yellow]skip[/bold yellow] {main_path.name}: no {TEST_FILE} next to it"
        )
        return 0, 0, 0, 0.0

    cases = _load_cases(csv_path)
    module = _import_module_from_path(main_path)
    solution_cls = getattr(module, "Solution", None)
    if solution_cls is None:
        console.print(
            f"[bold red]error[/bold red] {main_path}: no Solution class found"
        )
        return 0, 1, 1, 0.0

    passed = failed = 0
    total_ms = 0.0
    for row in cases:
        ok, elapsed_ms, got, error = _run_single(console, solution_cls, row)
        args, kwargs, expected = _decode(row)
        _render_result(console, row, ok, elapsed_ms, error, expected, got)
        passed += int(ok)
        failed += int(not ok)
        total_ms += elapsed_ms

    _render_summary(console, main_path, passed, failed, len(cases), total_ms)
    return passed, failed, len(cases), total_ms


def _render_bar(passed, total, width: int = 24) -> object:
    """A graphical progress bar: green filled / dim unfilled."""
    ratio = (passed / total) if total else 0.0
    filled = int(round(ratio * width))
    if _HAS_RICH:
        bar = Text()
        bar.append("█" * filled, style="bold green")
        bar.append("░" * (width - filled), style="dim red")
        bar.append(f" {ratio * 100:5.1f}%", style="bold")
        return bar
    return "█" * filled + "░" * (width - filled) + f" {ratio * 100:5.1f}%"


def _render_summary(console, main_path, passed, failed, total, total_ms):
    rate = (passed / total * 100) if total else 0.0
    color = "green" if failed == 0 else "red"
    status = "ALL TESTS PASSED" if failed == 0 else f"{failed} TEST(S) FAILED"

    if _HAS_RICH:
        grid = Table.grid(expand=False, padding=(0, 2))
        grid.add_column(justify="right", style="dim")
        grid.add_column(justify="left")
        grid.add_row("Test Suite", f"[bold]{main_path.parent.name}[/bold]")
        grid.add_row("Total Test Cases", f"[bold]{total}[/bold]")
        grid.add_row("Passed", f"[bold green]{passed}[/bold green]")
        grid.add_row("Failed", f"[bold red]{failed}[/bold red]")
        grid.add_row("Pass Rate", f"[bold]{rate:.1f}%[/bold]")
        grid.add_row("Progress", _render_bar(passed, total))
        grid.add_row("Total Time", f"{total_ms:.2f} ms")
        console.print(
            Panel(
                grid,
                title=f"[bold]Status Report — {main_path.parent.name}[/bold]",
                subtitle=f"[{color}]{status}[/{color}]",
                border_style=color,
            )
        )
    else:  # pragma: no cover
        console.print(f"== {main_path.parent.name} ==")
        console.print(f"    Total Test Cases : {total}")
        console.print(f"    Passed           : {passed}")
        console.print(f"    Failed           : {failed}")
        console.print(f"    Pass Rate        : {rate:.1f}%")
        console.print(f"    Progress         : {_render_bar(passed, total)}")
        console.print(f"    Total Time       : {total_ms:.2f} ms")


def _render_overall_summary(console, passed, failed, total, total_ms, suites):
    color = "green" if failed == 0 else "red"
    status = "ALL SUITES PASSED" if failed == 0 else f"{failed} FAILING TEST(S)"
    if _HAS_RICH:
        grid = Table.grid(expand=False, padding=(0, 2))
        grid.add_column(justify="right", style="dim")
        grid.add_column(justify="left")
        grid.add_row("Suites Tested", f"[bold]{suites}[/bold]")
        grid.add_row("Total Test Cases", f"[bold]{total}[/bold]")
        grid.add_row("Passed", f"[bold green]{passed}[/bold green]")
        grid.add_row("Failed", f"[bold red]{failed}[/bold red]")
        grid.add_row(
            "Pass Rate", f"[bold]{(passed / total * 100 if total else 0.0):.1f}%[/bold]"
        )
        grid.add_row("Progress", _render_bar(passed, total))
        grid.add_row("Total Time", f"{total_ms:.2f} ms")
        console.print(
            Panel(
                grid,
                title="[bold]Overall Status Report[/bold]",
                subtitle=f"[{color}]{status}[/{color}]",
                border_style=color,
            )
        )
    else:  # pragma: no cover
        console.print(f"== OVERALL: {passed}/{total} passed, {failed} failed ==")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Run CSV-driven tests for AlgoInfinity solutions."
    )
    parser.add_argument(
        "path", nargs="?", help="Path to a specific main.py. Defaults to all solutions."
    )
    args = parser.parse_args(argv)

    console = Console()
    if args.path:
        targets = [Path(args.path).resolve()]
    else:
        targets = _discover_solutions()
        if not targets:
            console.print(
                "[bold yellow]No solutions with a test_cases.csv found under the repo.[/bold yellow]"
            )
            return 0

    total_passed = total_failed = total_cases = 0
    total_ms = 0.0
    for target in targets:
        if len(targets) > 1:
            console.print()
            console.print(
                Panel(
                    f"[bold]{target.relative_to(REPO_ROOT)}[/bold]",
                    title="suite",
                    border_style="blue",
                )
            )
        passed, failed, total, ms = run_tests_for(target)
        total_passed += passed
        total_failed += failed
        total_cases += total
        total_ms += ms

    if len(targets) > 1:
        console.print()
        _render_overall_summary(
            console, total_passed, total_failed, total_cases, total_ms, len(targets)
        )

    return 1 if total_failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
