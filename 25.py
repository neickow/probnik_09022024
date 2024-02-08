from fnmatch import fnmatch

for i in range(2468336, 10**9, 13):
    if fnmatch(str(i), '24*68?35'):
        if int(str(i)[-3])%3==0 and int(str(i)[-3])%2!=0:
            n=str(i)[2:-3]
            if len(n)==0 or all(int(x)%2==0 for x in n):
                print(i, i//13)