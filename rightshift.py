x=list(map(int,input().split()))
y=list(map(int,input().split()))
for i in range(0,x[1]):
  y=[y[-1]] + y[:-1]
print(*y,end=' ')
