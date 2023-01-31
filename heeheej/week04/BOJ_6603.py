# 로또
# 176ms, 115272kb
# 조합을 이용한다.

import sys
from itertools import combinations

sys.stdin = open("input.txt", "r", encoding = "UTF-8")
input = sys.stdin.readline

while True:
    inputs = list(map(int, input().split()))
    k = inputs[0]
    if k == 0:
        break
    inputs = inputs[1:]

    nums = [i for i in range(k)]
    combs = combinations(nums, 6)
    for comb in combs:
        for i in comb:
            print(inputs[i], end=' ')
        print()
    print()