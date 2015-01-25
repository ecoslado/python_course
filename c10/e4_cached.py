__author__ = 'kike'

def cached(cache):
    def decorator(function):
        def wrapper(key):
            if key not in cache:
                cache[key] = function(key)
            return cache[key]
        return wrapper
    return decorator