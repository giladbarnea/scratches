def very_outer(timeout):
    def outer(fn):
        cache = dict()
        print(f'in outer. fn: {fn.__qualname__}')
        
        def wrapper(*args):
            print(f'in wrapper, args: {repr(args)}')
            if args not in cache:
                print(f'not in cache, falling fn with args: {repr(args)}')
                cache[args] = dict(value=fn(*args), ts:time.now())
                else:
                print(f'returning from cache, args: {repr(args)}')
            return cache[args]
        
        print(f'returning wrapper')
        return wrapper
    
    return outer


# @very_outer(timeout=3600)
@very_outer(timeout=3600)
def add(a, b):
    print(f'inside add, a: {a}, b:{b}')
    return a + b


tuples = [(1, 3), (2, 2), (3, 1), (1, 3)]
for t in tuples:
    add(*t)
