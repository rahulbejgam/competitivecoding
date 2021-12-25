a,b=map(int,input().split())
h=[]
for i in range(a+1,b):
    m=0
    for j in range(2,i+1):
        if i%j==0:
            m=m+1
    if m<2:
        h.append(i)
for i in h:
    i=str(i)
    if i==i[::-1]:
        print(i,end=" ")