"""
Write a decorator named dont_execute
His work can be seen from his name
"""



def dont_execute(condition):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition:
                print("Function execution is skipped due to condition.")
                return None  # Return None or any other default value
            else:
                return func(*args, **kwargs)
        return wrapper
    return decorator

# Example usage:
@dont_execute(condition=True)
def my_function():
    print("This function won't be executed")

# Example where the condition is False, so the function will be executed
@dont_execute(condition=False)
def another_function():
    print("This function will be executed")

# Test the decorators
my_function()  # This won't execute
another_function()  # This will execute
