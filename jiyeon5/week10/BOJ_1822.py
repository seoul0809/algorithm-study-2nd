a,b=map(int,input().split())
a_list=list(map(int,input().split()))
b_list=list(map(int,input().split()))

dictionary=dict()
for i in range(a):
    dictionary[a_list[i]]=True
for i in range(b):
    if b_list[i] in dictionary:
        del dictionary[b_list[i]]

print(len(dictionary))
a_minus_b=list(dictionary.keys())
a_minus_b.sort()
for x in a_minus_b:
    print(x, end=' ')