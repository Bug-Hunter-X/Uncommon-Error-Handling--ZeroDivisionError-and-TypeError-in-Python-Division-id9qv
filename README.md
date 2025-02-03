This repository contains a Python example demonstrating an uncommon error handling scenario. The `bug.py` file shows a function that attempts a division and handles both `ZeroDivisionError` and `TypeError` exceptions. This scenario might be uncommon because the error handling needs to consider data type mismatches in addition to the division by zero error. The solution file `bugSolution.py` is the same, but includes additional checks for type before division is attempted.