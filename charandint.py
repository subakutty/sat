p=str(input())
q=len(p)
a=0
b=0
for i in range(0,q):
    if p[i].isalpha():
        a=a+1
    if p[i].isnumeric():
        b=b+1
if a==0 or b==0:
    print("N0")
else:
    print("Yes")
