for x in "0123456789abc":
   s1=int(f'537{x}623', 13)
   s2=int(f'6{x}35{x}2', 13)
   if (s1-s2)%3==0:
      print(x)
