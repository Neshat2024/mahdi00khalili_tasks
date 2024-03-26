

""" example for decorators

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()  # Call the original function
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# Call the decorated function
say_hello()

"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
Please write a decorator that takes an integer parameter n as input.
When we place this decorator above a function, 
that function will be executed in a separate thread and after n seconds, 
the execution of the function will stop.
"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~






import threading
import time


def timeout_decorator(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Define a function to run in a separate thread
            def run_function():
                func(*args, **kwargs)

            # Create a thread to execute the function
            t = threading.Thread(target=run_function)

            # Set the thread as a daemon, so it exits when the main thread exits
            t.daemon = True

            # Start the thread
            t.start()

            # Wait for the specified time period
            t.join(n)

            # If the thread is still alive after the specified time, interrupt it
            if t.is_alive():
                print(f"Function {func.__name__} timed out after {n} seconds")
                # Interrupt the thread
                t.join()

        return wrapper

    return decorator


# Example usage:
@timeout_decorator(5)  # Function will stop after 5 seconds
def my_function():
    print("Starting function...")
    time.sleep(10)  # Simulate a long-running operation
    print("Function completed.")


# Calling the decorated function
my_function()


