year=int(input("请输入年份："))
month=int(input("请输入月份："))
day=int(input("请输入日期："))
a,b=0,0
months=(0,31,59,90,120,151,181,212,243,273,304,334)
if (year % 400 == 0)or((year % 4 == 0)and(year % 100 != 0)):
    if month>12:
        a=1
    elif month<=12:
        if (month<=7):
            if (month%2==0)and(month!=2) and (day>30):
                a=1
            if (month%2!=0)and(day>30):
                a=1
            if (month==2)and(day>29):
                a=1
        else:
            if (month%2==0)and(day>31):
                a=1
            if (month%2!=0)and(day>30):
                a=1
    b=1
else:
    if month>12:
        a=1
    elif month<=12:
        if (month<=7):
            if (month%2==0)and(month!=2) and (day>30):
                a=1
            if (month%2!=0)and(day>30):
                a=1
            if (month==2)and(day>28):
                a=1
        else:
            if (month%2==0)and(day>31):
                a=1
            if (month%2!=0)and(day>30):
                a=1
while a==1:
        print('dateError')
        break
else:
    sum=months[month-1]
    sum+=day
    if (b!=1)and(month>2):
        sum+=1
    if(b==1)and(month==2)and(day==29):
        sum=60
    print("这是{}年第{}天".format(year,sum))
