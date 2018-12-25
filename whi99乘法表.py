i=0
while i<9:
    i+=1
    j=1
    while j<=i:
        print("{}*{}={}".format(j,i,i*j),end=' , ')
        j+=1
    print()
