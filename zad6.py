def fun(a: list, b: list) -> list:
    result = list(set(a + b))
    return [x**3 for x in result]


print(fun([1, 1, 2], [1, 1, 3]))
