
#列表推导式： 【表达式2，循环体，表达式1】执行的顺序，先执行循环体，其次执行后面的表达式1，最后执行表达式2

# 需求： 生存一个1-10的列表
lst = []
for x in range(1,11):
    lst.append(x)
print(lst)
lst1 = [x for x in range(1,11)]
print(lst1)

# 需求，生成一个1-10的列表，需求只打印奇数的数

lst2 =[x for x in range(1,11) if x % 2 != 0]
print(lst2)


# 需求，生成一个1-10的列表，需求只打印奇数的数,生成的奇数的值再加10

lst2 =[x+10 for x in range(1,11) if x % 2]

print(lst2)










