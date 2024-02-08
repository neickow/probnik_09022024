print('1 ЗАДАНИЕ')
def f1(a,b, p, x):
    if (a+b>=x) and (p==3): # petya
        return True
    if (a+b>=x) and (p==2): # ivan
        return False
    if (a+b<x) and (p==3):  # petro
        return False
    if p%2==1: # petr
        return f1(a+2,b,p+1, x) and f1(a*2,b, p+1, x) and f1(a, b+2, p+1, x)  and f1(a, b*2, p+1, x)
    if p%2==0: # vanya
        return f1(a+2,b,p+1, x) or f1(a*2,b, p+1, x) or f1(a, b+2, p+1, x)  or f1(a, b*2, p+1, x)
for x in range(1,1000):
    if f1(4,9,1, x)==True:
        print(x)
        break
