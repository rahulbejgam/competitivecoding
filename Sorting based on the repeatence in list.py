print("Enter the elements seperated by space")
l=list(map(int,input().split()))
print(l)

g=list(set(l))
f={}
for i in range(len(g)):
    f[g[i]]=l.count(g[i])
#print(f)

k=dict(sorted(f.items(),key= lambda x:x[1],reverse=True))
#print(k)
l=list(k.keys())
#print(l)

m=[]
for i in l:
    for j in range(f[i]):
        m.append(i)
print(m)