# 암호 만들기
# 112ms, 114328kb
# 1. 입력받은 문자 값들을 정렬해준 뒤,
# 2. 조합을 이용해서 L개 선택 후
# 3. 조합 결과마다 모음, 자음개수를 확인해주었다.

import sys
from itertools import combinations

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

L, C = map(int, input().split())
inputs = list(map(str, input().split()))
inputs.sort()

nums = [i for i in range(C)]
combs = combinations(inputs, L)
aeiou = ['a', 'e', 'i', 'o', 'u']
for comb in combs:
    cnt1, cnt2 = 0, 0   # 모음개수, 자음개수
    chars = list()
    for x in comb:
        if x in aeiou:
            cnt1 += 1
        else:
            cnt2 += 1

    if cnt1 >= 1 and cnt2 >= 2:
        print(''.join(comb))