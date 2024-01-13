# 전화번호 목록
# 프로그래머스 코딩테스트 고득점 kit > 해시
# 1172 (+13)
# 왜 해시 문제인지 모르겠다.. 정렬과 슬라이싱 이용해 풀이

from collections import defaultdict

def solution(phone_book):
    answer = True
    phone_book.sort()
    N = len(phone_book)
    for i in range(N-1):
        val = phone_book[i]
        if val == phone_book[i+1][:len(val)]:
            answer = False
            break
    return answer