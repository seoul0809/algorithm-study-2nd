# 가장 큰 수
# 프로그래머스 코딩테스트 고득점 kit > 정렬
# 1231 (+12)
# https://yuna0125.tistory.com/145 참고

def solution(numbers):
    answer = ''
    numbers = [str(x) for x in numbers]
    numbers.sort(key = lambda x : x*3, reverse = True)
    answer = str(int(''.join(numbers)))
    return answer