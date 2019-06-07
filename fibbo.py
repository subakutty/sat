a=int(input())
s=0
b=1
for i in range(0,a):
  print(b,end==" ")
  temp=s+b
  s=b
  b=temp
