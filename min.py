import sys, string, math
a1,a2 = input().split()
n1 = len(s1)
n2 = len(s2)
if n2 > n1 :
    i = 0
    while i<n1 and a1[i] == a2[i] :
        i += 1
    print(n2-i)
elif n2 == n1 :
    i = 0
    while i<n2 and a1[i] == a2[i] :
        i += 1
    print(n2-i)
else :
    i = 0
    while i<n2 and a1[i] == a2[i] :
        i += 1
    a31 = a1[i:]
    a32 = a2[i:]
    L = list(a31)
    k = 0
    for c in a32 :
        if c in L :
            k += 1
            L.remove(c)
    print(n1-i-k)
