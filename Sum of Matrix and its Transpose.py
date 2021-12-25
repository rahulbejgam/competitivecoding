l=[]
print("Enter the size of your square matrix")
h=int(input())

print("Enter the matrix elements in row wise")
for i in range(h):
    a=list(map(int,input().split(" ")))
    l.append(a)
r=[]

for i in range(h):
    for j in range(h):
        b=l[i][j]+l[j][i]
        r.append(b)

print("Output")
for i in range(len(r)):
    if i%h==0 and i!=0:
        print( )
    print(r[i], end=" ")