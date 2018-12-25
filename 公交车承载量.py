num=int(input("输入车上人数："))
while True:
    if num<25:
        num+=1
        print("还能承载{}人，".format(26-num))
    else:
        print("座位已满，不能再承载了。")
        break
