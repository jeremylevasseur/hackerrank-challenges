data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
indices = range(10)
result = sorted(i for i in indices if i in data)
print(result)