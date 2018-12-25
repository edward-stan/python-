a,b=0,1
for n in range(1000):
    print(a,end=',')
    a,b=b,a+b
    if a>1000:
        break
