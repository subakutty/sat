m1,m2=input().split()
n=0
for i in range(int(m1),int(m2)+1):
    n=1
    f=0
    while n<=i:
        if i%n==0:
            f+=1
        n+=1
    if f==2:
        n+=1
print(n)
