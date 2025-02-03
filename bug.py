def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Unsupported operand type(s) for /'")
        return None

# Example usage:
result1 = function_with_uncommon_error(10, 2)  # Returns 5.0
result2 = function_with_uncommon_error(10, 0)  # Returns None and prints error message
result3 = function_with_uncommon_error(10, 'a') # Returns None and prints error message
result4 = function_with_uncommon_error(10, 2.5) # Returns 4.0
