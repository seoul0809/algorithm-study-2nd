# 구명보트
'''
1270 (+11)
투포인터 이용
몸무게를 오름차순 정렬한 뒤,
1. 두 명(몸무게가 가장 적은 사람, 몸무게가 가장 많은 사람)을 태우거나
2. 한 명(몸무게가 가장 많은 사람)을 태운다.
l == r 인 경우는 남은 사람이 한명인 경우이므로, 무조건 answer+=1 -> while l <= r로 처리
'''

def solution(people, limit):
    answer = 0
    people.sort()
    N = len(people)
    l, r = 0, N-1
    while l <= r:
        answer += 1 # 구명보트 수 +1
        if people[l] + people[r] <= limit:  # 두명 태울 수 있는 경우
            l += 1
            r -= 1
        else:   # 두명 못태우는 경우 무거운 사람만 태운다.
            r -= 1
    
    return answer