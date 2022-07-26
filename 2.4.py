a=float(input('一个实数'))
b=float(input('另一个实数'))
c=float(input('最后一个实数'))
if a > b and b > c:
    print(a,'>',b,'>',c)
elif a > c and c > b:
    print(a, '>', c, '>', b)
elif b > a and a > c:
    print(b,'>',a,'>',c)
elif b > c and c > a:
    print(b,'>',c,'>',a)
elif c > b and b > a:

    print(c,'>',b,'>',a)
else:
    print(c,'>',a,'>',b)