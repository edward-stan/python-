a=[(x,y,z)for x in range(1,5)for y in range(1,5)for z in range(1,5)if x!=y and y!=z and z!=x]
print(a)
print("一共有"+str(len(a))+"种组合")
