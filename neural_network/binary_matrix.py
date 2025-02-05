import numpy as np

def generate(n=2):
    if n == 0:
        return [[]]
    prev = generate(n-1)
    res = [[0] + i for i in prev] + [[1] + i for i in prev]
    return res

# print(generate(2))

print(np.array(generate(4)))