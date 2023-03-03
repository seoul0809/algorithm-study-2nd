# 정수 삼각형
# 152ms, 116108kb

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
N = int(input())
tri = list()
for i in range(N):
    tri.append(list(map(int, input().split())))

k = 2
for i in range(1, N):
    for j in range(k):
        if j == 0:
            tri[i][j] += tri[i-1][j]
        elif j == k-1:
            tri[i][j] += tri[i-1][j-1]
        else:
            tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])
    k += 1
print(max(tri[N-1]))