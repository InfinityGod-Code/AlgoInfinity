## Stack In Python

Stack in python can be implemented using the List by append() which will add elements into the stack and pop() removing from the last in elements. Stack follows LIFO — Last In, First Out.

CheatSheet : 
```
| Operation | Python       | Complexity |
| --------- | ------------ | ---------- |
| Push      |  append(x)   | O(1)       |
| Pop       |  pop()       | O(1)       |
| Peek      |  stack[-1]   | O(1)       |
| Empty     |  not stack   | O(1)       |
| Size      |  len(stack)  | O(1)       |

```

### Patterns of the Stack Questions are : 

- Matching Parentheses
- Monotonic Stack : strictky increasing or decresing
- Process Until Condition : Keep removing previous elements until the current element can fit.
- Expression Problems
- Simulating Undo / History
- DFS

### Things to Remember
- Check empty
  
  ```
  Use : 
    if not stack:
  Instead : 
    if len(stack) == 0:
  ```

- Peek safely 
  ```
  if stack:
    top = stack[-1]

  ```
- Don't pop blindly
  ```
  if stack : 
    stack.pop() 
  ```