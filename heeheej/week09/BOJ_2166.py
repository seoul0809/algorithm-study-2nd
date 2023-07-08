# 다각형의 면적
# 125ms, 114976kb
# 수학 문제
# 다각형의 넓이 공식(신발끈 공식)을 사용한다.

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
point = [tuple(map(int, input().split())) for _ in range(N)]
point.append(point[0])


def getArea(arr):
    area = 0
    for i in range(N):
        area += arr[i][0] * arr[i + 1][1] - arr[i + 1][0] * arr[i][1]
    area = abs(area) * 0.5
    return area


print(getArea(point))
