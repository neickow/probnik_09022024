f=open('17_1.txt')
s=[int(x) for x in f.readlines()]
k100=0
for i in range(len(s)):
    if abs(s[i])<100:
        k100+=1
mxs=0
k=0
for i in range(len(s)-1):
    if (s[i]+s[i+1])/2>k100:
        k+=1
        mxs=max(mxs, s[i]+s[i+1])
print(k, mxs)
