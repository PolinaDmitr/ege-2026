def f(x):
    x = x * 5
    return x


d = {}

def cache_f(x):
    if x in d.keys():
        return d[x]
    result = f(x)
    d[x] = result
    return result

print(f(5))
print(cache_f(5))
print(cache_f(5))