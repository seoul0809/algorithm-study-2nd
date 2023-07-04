# 문자열 압축 (2020 카카오 기출)
# https://school.programmers.co.kr/learn/courses/30/lessons/60057
# TC5 -> 문자열은 반드시 첫번째 문자부터 정해진 길이만큼 잘라야한다!
# 입력조건이 1개일때처럼 조건이 매우 작을때부터 매우 클 경우까지 극단적으로 생각해서 시뮬레이션 해보기
# => "aaaaaaaaaa"처럼 문자열이 10번이상 반복되는 경우, 10a이므로 + (sep + 1)이 아니라 (sep+2)를 해줘야함.

import math
# import pprint

def solution(s):
    length = len(s)
    results = [0]*(length//2+1)
    results[0] = float('inf')
    if length == 1:
        return 1
    for sep in range(1, length // 2 + 1):    # sep: 자르는 단위,
        # length // 2 + 1 이상은 문자열이 두개로 나눠지는데 이 두 문자열은 절대 같을 수 없으므로 안봐도 된다
        length2 = math.ceil(length/sep)
        dup_cnt = 1
        last = ''
        for k in range(length2):
            now = ''
            if k == length2 - 1: # 마지막 문자열이면
                now = s[sep*k:length]
                if last == now:
                    dup_cnt += 1
                    results[sep] += len(str(dup_cnt)) + sep
                else:
                    if dup_cnt == 1:    # 이 분기처리를 안해줘서 tc 2,6,11,12,14,15,17,26,27,28 틀림
                        results[sep] += sep + len(now)
                    else:
                        results[sep] += len(str(dup_cnt)) + sep + len(now)
            else:
                now = s[sep*k:sep*k+sep]
                if last == now: # 반복
                    dup_cnt += 1
                else:
                    if k != 0:  # 첫번째 문자열이면 이전문자열이 없으므로 안더해줘도 됨
                        if dup_cnt == 1:
                            results[sep] += sep
                        else:
                            results[sep] += len(str(dup_cnt)) + sep
                            dup_cnt = 1
                last = now
    answer = min(results)
    return answer