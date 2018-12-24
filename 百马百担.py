#___________________
for a in range(100//3+1):
    for b in range(50+1):
        c=100-a-b
        if(3*a+2*b+0.5*c==100):
            print(a,b,c)
