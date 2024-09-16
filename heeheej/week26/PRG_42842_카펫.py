# 카펫
'''
yellow를 소인수분해해서, i와 yellow//i로 나타낼 수 있다.
brown == 2*(i+2) + 2*(yellow//i+2) - 4(겹치는부분) 이라는 식이 나오는데,
간소화하면 2*(i + yellow//i)+4 == brown이라 할 수 있다.
'''
def solution(brown, yellow):
    answer = []
    N = int(yellow**(1/2))+1
    for i in range(1, N):
        if yellow % i == 0 and 2*(i + yellow//i) + 4 == brown:
            answer = [yellow//i+2, i+2]
    return answer