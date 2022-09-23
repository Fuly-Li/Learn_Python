def fun(a, b, c, d):
    return a, b, c, d


list01 = [1, 2, 3, 4]
print(fun(*list01))

dict01 = {"a": 4, "b": 3, "c": 2, "d": 1}
print(fun(**dict01))


def sum01(*args):
    a = sum(*args)
    return a


print(sum01((1, 2, 3, 9)))
