ticket=int(input("输入门票类型,（儿童票输1，团体票输2）"))
儿童票=1
成人票=2
m=100
n=int(input("购票数量"))
if (ticket==2):
    if (n>=0 and n<20):
        N=m*n*0.9
    elif (n>=20 and n<50):
        N=m*n*0.8
    elif (n>=50 and n<100):
        N=m*n*0.7
    else:
        N=m*n*0.5
else:
    N=m*n*0.5
M=int(input("输入付款金额"))
if (N>M):
    print("钱不够")
else:
    print('找零',M-N)
