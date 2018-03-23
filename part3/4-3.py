listValue = list(range(1,21))
for value in listValue:
    print(value)

million = list(range(1,10**6+1))
print(min(million))
print(max(million))
print(sum(million))
# for value in million:
    # print(min)
# 1-20的奇数
odds = list(range(1,21,2))
for odd in odds:
    print(odd)
print("3-30能被3整除")
lists = list(range(3,31,3))
for value in lists:
    print(value)
print("1-10的立方")
cubes = [value**3 for value in range(1,11)]
print(cubes)