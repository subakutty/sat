m,c=input().split()
n=len(m)
o=0
for i in range(0,n,1):
  if m[i]!=c[i]:
    o=o+1
if o==1:
  print("yes")
else:
  print("no")
