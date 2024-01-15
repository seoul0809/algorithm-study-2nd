# 의상
# 프로그래머스 코딩테스트 고득점 kit > 해시
# 1179(+7)
# 딕셔너리 자료형 이용
# 서로 다른 옷의 조합의 가지수
#  -> (옷 종류별 의상 가짓수 + 1)를 모두 곱하고, 
# 아무 의상도 안입는 경우 -1을 해주면 된다.
# +1 을 해주는 이유 -> 그 종류 의상을 안 입는 경우의 수 까지!

from collections import defaultdict

def solution(clothes):
    answer = 1
    d = defaultdict(int)
    for name, category in clothes:
        d[category] += 1
    print(d)
    for n in d.values():
        answer *= (n + 1)   # 안입는 경우까지 + 1
    answer -= 1
    return answer