'''
"우선순위"라는게 나오면 heapq(우선순위 큐)를 생각하자
q라는 우선순위 큐를 특정 시각 기준에 아직 처리되지 않은 프로그램들이 담겨있는 대기 목록이라 생각하고,
여기서 우선순위 가장 높은 애를 빠르게 뽑을 수 있다
일단, 로직의 흐름은 다음과 같다
1. 큐에서 하나 꺼낸다. (얘는 대기 목록에서 우선순위가 가장 높은 애)
    - 큐에 아무것도 없으면 now값 조정해주고 call_programs 한다.
2. 시간 계산해주고, answer 배열에 잘 더해준다.
3. 현재 시각 이하로 대기 목록 q에 추가할 애들을 모두 큐에 넣는다.
    - while program[i][1] (호출 시간)이 현재시각 이하일때 반복
    - 얘를 하기 위해서 호출시간 순으로 program을 정렬해둔다.
주의: 0초에 호출되는 프로그램이 없을 수도 있다.
주의: 3-1-2순으로 하면 골치아파짐
참고: 리스트도 pop 할 수 있다! popleft()는 없고 pop()하면 맨 마지막 원소, pop(0)하면 첫번째 원소
'''

'''
힙큐 사용법 다시...
1. import heapq
2. q 배열을 일단 만든다 or 기존의 리스트를 heapify를 통해 변환 가능
3. push할 때: heapq.heappush(q, 값) / pop할 때: heapq.heappop(q)
'''

'''
아래는 틀린 생각... 호출시간 순서로 정렬을 했어도 두개 이상의 프로그램이 호출시간이 0일 수 있음.
한번에 여러애들을 가져와야함

일단, 로직의 흐름은 다음과 같다
호출시간 가장 빠른 애를 program 배열에서 pop한다
걔가 끝나는 시간이 현재 시각?
'''

import heapq

def call_programs(program, now, q):
    while program and program[0][1] <= now:
        heapq.heappush(q, program.pop(0))
    # print(f"현재 대기열: {q}")

def solution(program):
    answer = [0]*11
    program.sort(key = lambda x:x[1])
    
    q = []  # 우선순위 큐
    now = 0 # 현재 시각
    while program or q:
        if not q:   # 0초에 호출된 애가 없으면 call_program을 했을 때 q에 아무값이 없는데 pop을 하게 돼서 오류난다.
            now = program[0][1]    # 현재 시각을 호출시각이 가장 빠른 프로그램의 호출시각으로 바꿔준다.
            call_programs(program, now, q)
            continue
        score, call_time, exe_time = heapq.heappop(q) # 우선순위가 최소인 애를 빼낸다. (첫번째 원소 기준으로 우선순위 판별)
        # print(f"우선순위 가장 높은 애: [{score}, {call_time}, {exe_time}]")
        answer[score] += (now - call_time)  # 대기 시간(지금 시각 - 프로그램 호출 시각)을 answer배열에 더해준다
        # print(f"now: {now}, call_time: {call_time}, {now-call_time}")
        now += exe_time # 현재시각 갱신: 현재 시각 + 프로그램 수행 시간
        call_programs(program, now, q)  # 이제 갱신된 현재 시각에 따라 대기중인 애들 우선순위큐에 넣기
    
    answer[0] = now
    return answer