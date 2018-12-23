number = int(input('输入数字'))        #number=3  输入的数字是3
time = int(input('次数'))              #time=4    次数为4
# while time>1:
    # number = number*(10^time)            #number = 30000
    # time = time-1
    # number1 = number*(10^time)+number
# print(number1)

number1 = 0
n = time
result = 0
while n > 0:
        while time>=1:
                number1 += number*(10**(time-1))
                time-=1
        result+=number1
        number1=0
        n-=1
        time = n
print(result)
