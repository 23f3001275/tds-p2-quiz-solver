import time

def timer(func):
    async def wrapper(*args, **kwargs):
        start = time.time()
        result = await func(*args, **kwargs)
        print(f"[Timer] {func.__name__} took {time.time() - start:.2f}s")
        return result
    return wrapper
