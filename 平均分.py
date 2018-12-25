#平均分
L=[75, 98, 59, 81, 66, 43, 69, 85]
b=0
n=0
for x in L:
    b=b+x
    n=n+1
print (b/n)
#60以上平均分
for x in L:
    if x < 60:
        continue
    b=b+x
    n=n+1
print(b/n)
