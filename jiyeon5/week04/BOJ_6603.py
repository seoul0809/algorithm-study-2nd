'''
푼 시간 : 13분
성능 : 메모리 115268KB, 시간 152ms
주의할 점 :
    조합 라이브러리 사용법 익히기
'''

import itertools

while True:

    # k와 S에 포함되는 수 입력받기
    arr = list(map(int,input().split()))
    k = arr[0]
    arr = arr[1:]

    # 0이 입력되면 종료
    if(k == 0): break

    # 조합 라이브러리를 이용해 조합 리스트 구하기
    for comb in itertools.combinations(arr,6):
        # 리스트 안 조합 하나하나 출력하기
        for c in comb:
            print(c, end=" ")
        print()

    print()
