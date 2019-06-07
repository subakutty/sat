a=input()
a=int(a)
b1=[]
for j in range(0,a):  
    n1=input()
    b1.append(n1)
f1=[]
for j in zip(*a1):
    if j.count(j[0])==len(j): 
        f1.append(j[0])
    else:
        break
print(''.join(f1))
