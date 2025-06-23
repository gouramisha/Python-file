from functools import lru_cache

@lru_cache(maxsize=None)
def slow_function(n):
    print(f"Calculating for {n}")
    return n * n

# Call the function
print(slow_function(4))  # Will calculate
print(slow_function(4))  # Will fetch from cache


# ✅ Function Caching: Result ko yaad rakhta hai using @lru_cache, fast performance on repeated calls.