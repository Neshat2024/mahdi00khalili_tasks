"""
Write a decorator that does not allow multiple instances of a function 
to be executed at the same time and 
write a test for the correctness of this decorator's performance.
"""


import threading

def single_instance_decorator(func):
    lock = threading.Lock()

    def wrapper(*args, **kwargs):
        with lock:
            return func(*args, **kwargs)
    
    return wrapper

# Example usage:
@single_instance_decorator
def my_function():
    print("Executing my_function")

# Test the correctness of the decorator's performance
def test_decorator_performance():
    import time

    # Define a function that waits for some time
    @single_instance_decorator
    def func_with_delay(seconds):
        print(f"Starting execution with delay of {seconds} seconds")
        time.sleep(seconds)
        print("Execution completed")

    # Call the function with delay multiple times concurrently
    threads = []
    for _ in range(5):
        t = threading.Thread(target=func_with_delay, args=(2,))
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

test_decorator_performance()
