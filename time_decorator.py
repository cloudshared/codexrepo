import time


def timing_decorator(func):
    """Simple decorator that logs start and stop time of a function."""

    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"Function {func.__name__} started at {start}")
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} ended at {end}")
        print(f"Elapsed: {end - start:.6f} seconds")
        return result

    return wrapper
