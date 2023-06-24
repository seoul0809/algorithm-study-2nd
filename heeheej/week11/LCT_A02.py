# 곱하기 혹은 더하기
# +보다 *를 먼저 계산하는 일반적인 방식과는 달리, 왼쪽에서부터 순서대로 연산이 이루어진다.
# 이 때, 대부분의 경우에서는 곱하기를 수행한 결과가 더 크게 될 것이다.
# 더하기가 더 큰 경우는 두 수 중에서 하나라도 0이거나 1인 수가 있을 때이다!
# 정리하면 앞에서부터 차례대로 연산을 진행하는데,
# 현재 숫자가 1 이하이면 +, 아니면 *를 해주면 항상 최적의 해를 얻을 수 있다. => 그리디

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
S = list(input().rstrip())
result = int(S[0])
N = len(S)
for i in range(1, N):
    x = int(S[i])
    if result <= 1 or x <= 1:
        result += x
    elif result + x > result * x: # +를 해야하는 경우
        result += x
    else:
        result *= x

print(result)