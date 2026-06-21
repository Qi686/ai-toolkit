#访问列表元素
names=['Alice','Bob','charlie','David']
print(names[0].lower())
print(names[1].title())
print(names[2].upper())
print(names[3])
print(names[-1])

#使用列表中的各个值
message="hello,my name is"+" "+names[-1].title()+"."
print(message)
message="hello,my name is"+" "+names[-2].title()+"."
print(message)
message="hello,my name is"+" "+names[-3].title()+"."
print(message)
message="hello,my name is"+" "+names[-4].title()+"."
print(message)

# 我注意到，代码中间是需要流出空格的，不只是为了美观和可读性，也是为了规范代码严密性

# 修改列表元素
names[0] = 'Anna'
print(names)

# 在列表中添加元素
names.append('even')
print(names)

fruits = []
fruits.append('apple')
fruits.append('banana')
fruits.append('orange')
print(fruits)

fruits.insert(1,'grape')
print(fruits)  

del fruits[3]           # 这里已经删除了列表中的'orange'元素了
print(fruits)

popped_fruit = fruits.pop()
print(fruits)
print(popped_fruit)

last_owned = fruits.pop()
print("The last fruit i owned was"+" "+last_owned.upper()+".")

fruits = ['apple','banana','grape']                   # 这里出现给变量重新赋值一个列表
print(fruits)
fruits.remove('banana')
print(fruits)


fruits = ['apple','banana','grape']                  # 这里出现给变量重新赋值一个列表
print(fruits)
too_cheap = 'banana'
fruits.remove(too_cheap)
print(fruits)
print("\nA"+too_cheap.lower()+"is too cheap for me.")

# 动手试一试
# 嘉宾名单
list = ['Alice','Bob','Charlie','David']
print("I want to invite"+" "+list[0].title()+" "+"to my party.")
print("I want to invite"+" "+list[1].title()+" "+"to my party.")
print("I want to invite"+" "+list[2].title()+" "+"to my party.")
print("I want to invite"+" "+list[3].title()+" "+"to my party.")

# 修改嘉宾名单
print(list[0].title()+" "+"can not come to my party.")
print(list[0])
del list[0]
print(list)
print("I want to invite"+" "+list[0].title()+" "+"to my party.")
print("I want to invite"+" "+list[1].title()+" "+"to my party.")
print("I want to invite"+" "+list[2].title()+" "+"to my party.")

# 添加嘉宾
print("I found a bigger table.")
list.insert(0,'Anna')
list.insert(2,'even')
list.append('frank')
print(list)
print("I want to invite"+" "+list[0].title()+" "+"to my party.")
print("I want to invite"+" "+list[1].title()+" "+"to my party.")
print("I want to invite"+" "+list[2].title()+" "+"to my party.")
print("I want to invite"+" "+list[3].title()+" "+"to my party.")
print("I want to invite"+" "+list[4].title()+" "+"to my party.")
print("I want to invite"+" "+list[5].title()+" "+"to my party.")

# 缩减名单
print("I am sorry that I can only invite two people for my party.")
popped_list = list.pop(5)
print("I am sorry that I can not invite"+" "+popped_list.title()+" "+"to my party.")
popped_list = list.pop(4)
print("I am sorry that I can not invite"+" "+popped_list.title()+" "+"to my party.")
popped_list = list.pop(3)
print("I am sorry that I can not invite"+" "+popped_list.title()+" "+"to my party.")
pop_list = list.pop(2)
print("I am sorry that I can not invite"+" "+popped_list.title()+" "+"to my party.")
print(list)
print("I want to invite"+" "+list[0].title()+" "+"to my party.")
print("I want to invite"+" "+list[1].title()+" "+"to my party.")
del list[0]
del list[0]
print(list)

# 使用 sort() 对列表进行永久性排列
names = ['charlie','David','Alice','Bob']
names.sort()
print(names)
names.sort(reverse=True)
print(names)

# 使用 sorted() 对列表进行临时排列
names = ['charlie','David','Alice','Bob']
print("Here is the original list:")
print(names)
print("\nHere is the sorted list:")
print(sorted(names))
print("\nHere is the original list again:")
print(names)

# 倒转排序列表
fruits = ['apple','banana','grape']
print(fruits)
fruits.reverse()
print(fruits)

# 确定列表的长度
fruits = ['apple','banana','grape']
print(len(fruits))

# 练习
# 放眼世界
places = ['beijing','shanghai','guangzhou','hangzhou','shenzhen']
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

# 晚餐嘉宾
list = ['Alice','Bob','Charlie','David']
print(len(list))
