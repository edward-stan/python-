t=input("是否为会员:Y/N")
total=eval(input("输入金额"))
if (t=="Y"):
    if (total>100):
        print(total*0.8)
    elif (total>200):
        print(total*0.75)
    else:
        print(total)
else:
    if (total>100):
        print(total*0.9)
    else:
        print(total)
