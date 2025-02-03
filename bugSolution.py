def function_with_uncommon_error(a, b):
    try:
        if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
            raise TypeError("Operands must be numbers")
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError as e:
        print(f"Error: {e}")
        return None

# Example usage:
result1 = function_with_uncommon_error(10, 2)  # Returns 5.0
result2 = function_with_uncommon_error(10, 0)  # Returns None and prints error message
result3 = function_with_uncommon_error(10, 'a') # Returns None and prints error message
result4 = function_with_uncommon_error(10, 2.5) # Returns 4.0