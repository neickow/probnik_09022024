from functools import lru_cache
import sys
sys.setrecursionlimit(10000000)
@lru_cache(None)
def f(n):
    if n>=10000:
        return 1
    if n%2==0:
        return f(n+3)+7
    return f(n + 1) - 3
ans=[]                           # просто так он не выводит, заканчивает ошибкой, походу только списком можно досчитывать :(
for i in range(9999, 49, -1):
    ans.append(f(i))
print(ans[-1]- ans[-8])

