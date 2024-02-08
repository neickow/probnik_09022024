def f1(a,b, p, x):
    if (a+b>=x) and (p==4): # petya
        return True
    if (a+b>=x) and (p==3): # ivan
        return False
    if (a+b<x) and (p==4):  # petro
        return False
    if p%2==0: # petr
        return f1(a+2,b,p+1, x) and f1(a*2,b, p+1, x) and f1(a, b+2, p+1, x)  and f1(a, b*2, p+1, x)
    if p%2==1: # vanya
        return f1(a+2,b,p+1, x) or f1(a*2,b, p+1, x) or f1(a, b+2, p+1, x)  or f1(a, b*2, p+1, x)
k=0
for x in range(1,1000):
    if f1(10,15,1, x)==True:
        k+=1
print(k)

#