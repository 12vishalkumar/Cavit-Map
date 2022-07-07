import math
import os
import random
import re
import sys
# Complete the 'cavityMap' function below.
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
n = int(input())
arr = []
for i in range(n):
    l = input()
    if l[-1] == '\n':
        l = l[:-1]
    arr.append([int(c) for c in l])
arr1 = [[c for c in l] for l in arr]
ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for x in range(1, n - 1):
    for y in range(1, n - 1):
        v = arr[x][y]
        if all(map(lambda z: arr[x + z[0]][y + z[1]] < v, ds)):
            arr1[x][y] = 'X'
for l in arr1:
    print(''.join(map(str, l)))