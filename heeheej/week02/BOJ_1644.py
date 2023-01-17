# 소수의 연속합
# 884ms, 162028kb
# 범위 내의 모든 소수 -> 에라토스테네스의 체!!
# 주의: N이 1인 경우도 고려해야 한다.

import sys

sys.stdin = open("../input.txt", "r")
input = sys.stdin.readline
N = int(input())


def getPrimeNumbers(n):
    arr = list()
    sieve = [True] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i] == True:
            arr.append(i)
            for j in range(i * 2, n + 1, i):
                sieve[j] = False
    return arr


primes = getPrimeNumbers(N)
size = len(primes)
left, right, sum = 0, 0, 0
result = 0
# print(size)

while True:
    if left > right or right >= size:
        if size != 0 and primes[size - 1] == N:
            result += 1
        break

    if sum < N:
        sum += primes[right]
        right += 1
    elif sum == N:
        result += 1
        sum -= primes[left]
        left += 1
    else:
        sum -= primes[left]
        left += 1
    # print(f"left: {left}, right: {right}, sum: {sum}, result: {result}")

print(result)