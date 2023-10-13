# 딕셔너리 활용
n=int(input())
n_list=list(map(int,input().split()))
m=int(input())
m_list=list(map(int,input().split()))

dictionary=dict()
for i in range(n):
    dictionary[n_list[i]]=True

for i in range(m):
    if m_list[i] in dictionary:
        print('1', end=' ')
    else:
        print('0',end=' ')


# 이분탐색 활용
n=int(input())
n_list=sorted(list(map(int,input().split())))
m=int(input())
m_list=list(map(int,input().split()))

for ml in m_list:
    start,end=0,n-1
    flag=False
    while start<=end:
        mid=(start+end)//2
        if n_list[mid]==ml:
            flag=True
            print('1', end=' ')
            break
        elif n_list[mid]<ml:
            start=mid+1
        else:
            end=mid-1
    if not flag: print('0', end=' ')