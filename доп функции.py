def func(param):
    result_ = 0
    if isinstance(param, int):
        return param
    elif isinstance(param, str):
        return len(param)
    elif isinstance(param, (set, list, tuple)):
        for i in param:
            result_ += func(i)
    elif isinstance(param, dict):
        for key, values in param.items():
            result_ += func(key)
            result_ += func(values)
    return result_

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(func(data_structure))