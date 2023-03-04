# [S/W 문제해결 기본] 9일차 - 중위순회
# 176ms, 58780kb
# 재귀
import sys
sys.stdin = open("input.txt", "r")

def inOrder(n):
    if n > N:
        return
    inOrder(2*n)
    global result
    result += arr[n]
    inOrder(2*n+1)

for t in range(1, 11):
    N = int(input())
    arr = [0]
    for _ in range(N):
        inputs = list(map(str, input().split()))
        arr.append(inputs[1])
    result = ''
    inOrder(1)
    print(f"#{t} {result}")