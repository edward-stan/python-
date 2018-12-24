weight=int(input("输入你的体重"))
high=int(input("输入你的身高"))
标准体重=high-110
if (weight<(标准体重+5) and weight>(标准体重-5)):
    print("正常")
elif(weight>标准体重+5):
    print("过胖")
else:
    print("过瘦")
