n=int(input())
list=list(map(int,input().split()))
list.sort()

print(list[(n-1)//2])