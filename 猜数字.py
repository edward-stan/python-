num=int(input("请输入一个数字："))
while num!=147:
    if num>147:
        print("你猜大了")
        break
    elif num<147:
        print("你猜小了")
        break
else:
    print("你猜对了")
