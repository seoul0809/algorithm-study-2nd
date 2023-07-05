# 문자열 재정렬
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

arr = list(input().rstrip())
arr.sort()
result = ''.join(arr)
length = len(arr)
n = 0
for i in range(length):
    if arr[i].isdigit():
        n += int(arr[i])
    else:
        result = ''.join(arr[i:])
        break

if n == 0:
    print(result)
else:
    print(result + str(n))