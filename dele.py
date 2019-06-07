from itertools import combinations
a,b=map(int,input().split())
c=len(str(a))
k=list(combinations(str(a),c-b))
k=(sorted(k))
s="".join(k[0])
print(s)
