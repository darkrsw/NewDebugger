# Assignment #2: Improved Debugger

Your submission must satisfy the following requirements:

* R1. Shall initialize your assignment repository from ___
* R2. Write your `CondBreakDebugger.py` in the repository.
* R3. Test your `CondBreakDebugger.py` by using `pytest`.
* R4. You need to let your TA know your repository URL and your student ID together.
* R5. `CondBreakDebugger` class should be defined in the `CondBreakDebugger.py`
* R6. The above class is tested as:

```
from CondBreakDebugger import CondBreakDebugger
from utils import next_inputs, clear_next_inputs

def test_debug_1():
    clear_next_inputs()
    next_inputs([...])
    with CondBreakDebugger() as debugged:
        func1(args)
      	func2(args2)
        
    assert ...
```

* R7. This assignment assumes that you already have a `Debugger()` class composed from `debuggingbook.org`.
* R8. You have to add (or inherit; or modify) the following new commands to your `CondBreakDebugger()` based on `Debugger()`:
   - `attr` -- Use as 'attr OBJ, VAR, EXPR'. Set the result of EXPR to member variable VAR of object OBJ.
   - `set` -- Use as 'set VAR=VALUE'. Assign VALUE to local variable VAR.
   - `break` -- Set a breakoint in given line or expression. e.g., `break 9` or `break var==value`. If no line or expression is given, list all breakpoints
* R9. `next_inputs()` and `clear_next_inputs()` are given for testing. DO NOT change them.




## Note:

* N1. `pytest` (based on `test_cbd*.py`) is just for validating your program. The final grading will be made by other test cases.
* N2. Submissions via GitHub Classroom will only be accepted. Submissions via LMS or any other means are not accepted.
* N3. DO NOT change files in this repository except for `CondBreakDebugger.py`. Adding new files are allowed.
