"""
Write a decorator that logs every execution of the function 
in a file whose path is part of the decorator's parameters. 
The log contains the name, input and output of the function
"""


def log_execution(log_file):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Execute the function and capture its output
            result = func(*args, **kwargs)

            # Log the function execution to the specified file
            with open(log_file, 'a') as f:
                f.write(f"Function Name: {func.__name__}\n")
                f.write(f"Input Arguments: {args}, {kwargs}\n")
                f.write(f"Output: {result}\n\n")

            return result  # Return the result of the function
        return wrapper
    return decorator

# Example usage:
@log_execution("execution_log.txt")
def add(a, b):
    return a + b

# Test the decorated function
add(2, 3)
add(4, 5)


