N=eval(input("输入行数"))
for i in range(1,N+1):
    for j in range(2*i-1):
        print("*",end="")
    print()
#-----------------
N=eval(input("输入行数"))
for i in range(N):
    for j in range(N-1):
        print(" ",end="")
    for j in range(2*i-1):
        print("*",end="")
    print()
    
