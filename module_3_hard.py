data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
print(*data_structure)

def calculate_structure_sum (a):
    x = 0
    if isinstance(a, (int, float)):
        return a
    elif isinstance(a, str):
        return len(a)

    elif isinstance(a, (list, set, tuple)):
        for i in a:
            x = x + calculate_structure_sum(i)
        return x
    elif isinstance(a, dict):
        for k, v in a.items():
            x = x + calculate_structure_sum(k)
            x = x + calculate_structure_sum(v)
    return x

result = calculate_structure_sum(data_structure)
print(result)
