string = input()
a=0
b=0
for i in range(len(string)):
    if(string[i].isalpha() or string[i].isdigit()):
       a=a+1
    else:
        b=b+1
print(b)
