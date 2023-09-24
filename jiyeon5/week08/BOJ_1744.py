import heapq
n=int(input())
q=[]
for _ in range(n):
    heapq.heappush(q,int(input()))

answer=0
temp=-1001
second=False
remain=-1001
zero=False
one=False
while q:
    num=heapq.heappop(q)
    if num>=0:
        if num==0:
            zero=True
            if q:
                num=heapq.heappop(q)
        if num==1:
            answer+=1
            break
        heapq.heappush(q,num)
        break
    if second==False:
        temp=num
        remain=num
        second=True
    else:
        answer+=(temp*num)
        remain=-1001
        second=False

if remain!=-1001 and not zero:
    answer+=remain

while q:
    num=heapq.heappop(q)
    if num==1 or num==0:
        answer+=num
    else:
        heapq.heappush(q,num)
        break

if len(q)%2!=0:
    num=heapq.heappop(q)
    answer+=num

temp=-1001
second=False
while q:
    num=heapq.heappop(q)
    if second==False:
        temp=num
        second=True
    else:
        answer+=(temp*num)
        second=False

print(answer)