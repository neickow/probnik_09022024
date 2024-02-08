f=open('24_1.txt')
s=f.readline()
s=s.replace('OCK', '*')
s=s.replace('ST', ')')
k=0
for i in range(len(s)-1):
    if s[i]!=')' and s[i+1]=='*':
        k+=1
print(k)