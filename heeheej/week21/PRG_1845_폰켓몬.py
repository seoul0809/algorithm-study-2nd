# 폰켓몬
# 프로그래머스 고득점 kit > 해시
# 딕셔너리 자료형 이용
 
def solution(nums):
    answer = 0
    d = dict()
    for x in nums:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    N = len(nums)
    max_len = len(d)
    if max_len < N//2:
        answer = max_len
    else:
        answer = N//2
    return answer