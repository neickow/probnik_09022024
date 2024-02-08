def f1(a,b, p, x):
    if (a+b>=x) and (p==3 or p==5): # petya
        return True
    if (a+b>=x) and (p==2 or p==4): # ivan
        return False
    if (a+b<x) and (p==5):  # petro
        return False
    if p%2==0: # petr
        return f1(a+2,b,p+1, x) or f1(a*2,b, p+1, x) or f1(a, b+2, p+1, x)  or f1(a, b*2, p+1, x)
    if p%2==1: # vanya
        return f1(a+2,b,p+1, x) and f1(a*2,b, p+1, x) and f1(a, b+2, p+1, x)  and f1(a, b*2, p+1, x)
k=0
for x in range(1,1000):
    if f1(8,8,1, x)==True:
        print(x)
