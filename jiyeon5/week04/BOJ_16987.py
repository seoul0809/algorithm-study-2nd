'''
푼 시간 : 59분
성능 : 메모리 128988KB, 시간 940ms
주의할 점 :
'''



# 계란 수 입력받기
n = int(input())

# 계란의 내구도와 무게를 배열에 저장
eggs = []
for _ in range(n):
    eggs.append(list(map(int,input().split())))

# 깨진 계란 최대값
answer = 0

def dfs(hand_egg, cnt):
    global answer

    # 가장 최근 든 계란이 가장 오른쪽에 위치한 계란이었을 경우 깨진 계란 수 최대값과 비교한 후 함수 탈출
    if hand_egg == n:
        if cnt > answer:
            answer = cnt
        return

    # 손에 든 계란이 깨진 경우 다음으로 넘어가기
    if eggs[hand_egg][0] <= 0:
        dfs(hand_egg+1,cnt)
        return

    # 깨진 계란의 수 확인하기 위해
    check = 0
    # 모든 계란을 확인하면서 계란 치기
    for i in range(n):
        # 자기자신의 계란일 경우 넘어가기
        if i==hand_egg:
            check += 1
            continue
        # 계란이 깨진 경우 넘어가기
        if eggs[i][0] <= 0:
            check += 1
            continue

        # 계란으로 계란치기
        eggs[hand_egg][0] -= eggs[i][1]
        eggs[i][0] -= eggs[hand_egg][1]
        # 계란이 깨진 경우 tmp 증가
        tmp=0
        if eggs[hand_egg][0]<=0:
            tmp += 1
        if eggs[i][0]<=0:
            tmp += 1

        # 오른쪽 계란을 손에 들고 다시 dfs
        dfs(hand_egg+1,cnt+tmp)

        # 백트래킹을 위해 계란 원래대로 되돌리기
        eggs[hand_egg][0] += eggs[i][1]
        eggs[i][0] += eggs[hand_egg][1]

    # 깨지지 않은 계란이 없다면 다음으로 넘어가기
    if check == n:
        dfs(hand_egg+1,cnt)

dfs(0,0)

print(answer)