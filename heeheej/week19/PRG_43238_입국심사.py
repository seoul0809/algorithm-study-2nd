# 입국심사
# 이분탐색!!!!!!!!!
# right => 가장 긴 심사시간이 소요되는 심사관에게 n 명 모두 심사받는 경우
# mid: 모든 심사관들에게 주어진 시간
# people: 모든 심사관들이 mid분 동안 심사한 사람의 수

def solution(n, times):
    answer = 0
    left, right = 1, max(times)*n
    while left <= right:
        mid = (left + right) // 2
        people = 0
        for time in times:
            people += mid // time
        if people >= n:
            answer = mid
            right = mid - 1
        elif people < n:
            left = mid + 1
    return answer