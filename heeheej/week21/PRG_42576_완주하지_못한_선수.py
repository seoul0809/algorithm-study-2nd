# 완주하지 못한 선수
# 프로그래머스 코딩테스트 고득점 kit > 해시
# 1159 (+6)
# 초깃값 처리 귀찮아서 defaultdict 사용
# defaultdict(int) -> 0으로 초기화, defaultdict(list) -> 빈 리스트로 초기화된다!

from collections import defaultdict
def solution(participant, completion):
    answer = ''
    d = defaultdict(int)
    for name in completion:
        d[name] += 1
    
    for name in participant:
        if name not in d or d[name] == 0:
            answer = name
            break
        else:
            d[name] -= 1
    return answer
