# PCCP 모의고사 1 1번 외톨이 알파벳
# 구현

def solution(input_string):
    answer = ''
    once = []   # 한번 이상 나타난 알파벳
    arr = []    # 외톨이 알파벳
    last_char = "-"
    for x in input_string:
        if x not in once:   # 처음 나온 알파벳이면
            once.append(x)
        elif last_char != x and x not in arr:
            # 두번 이상 나온 알파벳인데, 
            # 앞 덩어리와 분리되어있고 
            # 외톨이 알파벳 리스트에도 안들어있는 경우 외톨이 알파벳에 추가
            arr.append(x)
        last_char = x
    if arr:
        arr.sort()  # 알파벳순으로 정렬
        answer = ''.join(arr)
    else:
        answer = "N"
    return answer