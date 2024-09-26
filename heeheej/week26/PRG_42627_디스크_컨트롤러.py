# 디스크 컨트롤러
# 프로그래머스 코딩테스트 고득점 kit > 힙
'''
1. 현재 시점(t)까지 요청 들어온 애들을 모두 힙에 넣는다. (소요 시간에 대해서 최소 힙이 되도록)
- t의 초기값은 0
- 힙에 이미 넣은 애 또 넣으면 안되니까, 현재 시점을 last 변수에 저장해둔 후,
다음 반복에서는 그 후부터 현재시점까지 들어온 애들을 힙에 넣어준다. (last의 초기값은 -1)
2. 힙이 비어있지 않다면, heappop해서 소요시간 가장 작은 애 꺼낸다.
- l, s = heapq.heappop(heap)
- 현재시간 += s, 평균 계산을 위해 걸린 시간(t-s) 더하기, 작업 완료한 개수 + 1 해주기
힙이 비어있다면, 현재시간만 +1 해준다. 
- t += 1 대신 job에서 t보다 요청시간이 큰 것 중 요청시간 제일 빠른 걸로 하면 더 좋을 것 같지만, 속도는 별 차이 없는 듯 하다.
'''

import heapq

def solution(jobs):
    answer = 0
    jobs.sort()
    N = len(jobs)
    cnt = 0 # 완료된 작업의 개수
    heap = []
    last, t = -1, 0 # 마지막으로 저장한 시점, 현재 시점
    sum = 0 # 평균 계산을 위해 걸리는 시간을 모두 더함
    while cnt < N:
        for s, l in jobs:
            if last < s <= t:
                heapq.heappush(heap, (l, s))    # 소요 시간을 기준으로 최소 힙이 되도록
        last = t    # 힙에 이미 넣은 애를 또 넣으면 안되니까, 현재 시점을 저장해둠
        
        if heap:
            l, s = heapq.heappop(heap)
            t += l
            sum += (t - s)
            cnt += 1    # 한 개 처리
        else:
            # for s, l in jobs:
            #     if s > t:
            #         t = s
            #         break
            t += 1
    answer = sum // N
    return answer