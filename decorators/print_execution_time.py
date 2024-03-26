"""
Write a decorator that prints the execution time of the function
"""


import time

def print_execution_time(func):
    def wrapper(*args, **kwargs):
        # Record the start time
        start_time = time.time()

        # Execute the function
        result = func(*args, **kwargs)

        # Calculate the execution time
        execution_time = time.time() - start_time

        # Print the execution time
        print(f"Execution time of {func.__name__}: {execution_time:.6f} seconds")

        return result  # Return the result of the function
    return wrapper

# Example usage:
@print_execution_time
def some_function():
    # Simulate some computation
    time.sleep(2)

some_function()

