# 모음사전
# 프로그래머스 코딩테스트 고득점 kit > 완전탐색
# 1278 (+1)
# 중복순열 product 사용해서 리스트 만든 후, 사전순으로 정렬한다음 인덱스찾기

from itertools import product
def solution(word):
    answer = 0
    moeum = ["A", "E", "I", "O", "U"]
    arr = []
    for i in range(1, 6):
        prods = product(moeum, repeat = i)
        for prod in prods:
            temp = ''.join(prod)
            arr.append(temp)
    arr.sort()
    for i, x in enumerate(arr):
        if word == x:
            answer = i+1
            break
    return answer