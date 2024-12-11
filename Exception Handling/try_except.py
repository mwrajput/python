# prompt: Exception Handling 

def divide_numbers(x, y):
  """Divides two numbers and handles potential ZeroDivisionError.

  Args:
    x: The numerator.
    y: The denominator.

  Returns:
    The result of the division, or an error message if division by zero occurs.
  """
  try:
    result = x / y
    return result
  except ZeroDivisionError:
    return "Error: Division by zero is not allowed."
  except TypeError:
    return "Error: Inputs must be numbers."
  except Exception as e:  # Catching other potential exceptions
    return f"An unexpected error occurred: {e}"


# Example usage
print(divide_numbers(10, 2))  # Output: 5.0
print(divide_numbers(10, 0))  # Output: Error: Division by zero is not allowed.
print(divide_numbers(10, "a")) # Output: Error: Inputs must be numbers.
print(divide_numbers(10, 2.5)) # Output: 4.0