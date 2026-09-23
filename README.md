# AlgoInfinity

<p align="center">
  <img src="assets/algoinfinity_1.png" alt="Alt" width="100%">
</p>

A structured repo mastering DSA. Each problem includes multiple solution tiers (Brute-Force, Slight-Optimal, Optimal, and Sub-Optimal edge-case variants) with deep complexity tradeoffs. Every directory features a notes.md mapping out key intuitions, edge cases handled, and core reusable code patterns learned during the process.


### Running for Test cases : 
Just run the Python file and it should automatically displays proper results with proper Status : 

<p align="center">
  <img src="assets/demo.png" alt="Alt" width="100%" height="65%">
</p>

### Adding a new problem

Follow this layout for every problem folder:

```text
ProblemName/
  main.py
  test_cases.csv
  problem_statement.md
  notes.md
```

`main.py` should always expose a `Solution` class with a method named `solution`.
The arguments of `solution` must match the `args` column in `test_cases.csv`.

```python
class Solution:
    def solution(self, nums: list, target: int) -> int:
        # Write the main accepted approach here.
        return 0


if __name__ == "__main__":
    import sys
    from pathlib import Path

    root = Path(__file__).resolve().parent
    while not (root / "run_tests.py").exists() and root.parent != root:
        root = root.parent
    sys.path.insert(0, str(root))

    from run_tests import run_tests_for

    _, failed, _, _ = run_tests_for(__file__)
    raise SystemExit(1 if failed else 0)
```

`test_cases.csv` must use JSON values for `args` and `expected`. Keep the
`function` column as `solution` unless you intentionally want to test another
method.

```csv
name,function,args,expected
basic,solution,"[[1, 2, 3], 3]","true"
edge_empty,solution,"[[], 0]","0"
```

Useful commands:

```bash
python3 path/to/ProblemName/main.py
python3 run_tests.py path/to/ProblemName/main.py
python3 run_tests.py
```
