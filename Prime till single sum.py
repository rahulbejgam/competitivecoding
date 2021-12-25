#Rahul codes here
def rs(b):
    s=0
    a=b
    while(a!=0):
        s=s+a%10
        a=a//10
    if s<10 and s>=0:
        if s in [2,3,5,7]:
            return 1
    else:
        return rs(s)

print("enter the range of minimum and maximum value")
a,b=map(int,input().split())

h=[]
for i in range(a+1,b):
    m=0
    for j in range(2,i+1):
        if i%j==0:
            m=m+1
    if m<2:
        h.append(i)
print(h)

for i in h:
    if rs(i):
        print(i,">> YES")
    else:
        print(i,">> NO")