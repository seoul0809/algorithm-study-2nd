# 랜선 자르기
# 128ms, 115216kb
# 이진탐색
# right = arr[0](최솟값)으로 잘랐을 때 개수가 N보다 큰 경우가 존재하기 때문에 arr[-1](최댓값)으로 해야한다.
# cnt == N이 되었다고 해서 반복문을 바로 탈출하면 안된다.
# N이 되는 길이가 여러개가 나올 수 있는데, 그 길이 중 최대 길이를 찾아야하기 때문이다!
# 최대 길이를 찾아야 하므로 right값을 출력해준다.

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]
arr.sort()
left, right = 1, arr[-1]
while left <= right:
    mid = (left + right) // 2

    cnt = 0
    for x in arr:
        cnt += x // mid
    if cnt >= N:
        left = mid + 1
    else:
        right = mid - 1
print(right)