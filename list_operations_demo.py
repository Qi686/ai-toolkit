# 遍历整个列表
fruits = ['apple','banana','cherry','date','elderberry']
for fruit in fruits:
    print(fruit)
    print(fruit.title() + ",I love you!")
    print("I can not wait to eat you," + fruit.lower() + ".\n")
print("I love you so much!" + "\n")

# 动手试一试
pizzas = ['Durian pizza','Mango pizza','Apple pizza','Tomato beef pizza']
for pizza in pizzas:
    print("I like" + pizza.title() + "!\n")
print("I really love pizza!" + "\n")

pets = ['cat','dog','pig']
for pet in pets:
    print("A" +" " + pet.lower() + " "+"would make a great pet" + ".\n")
print("Any of these animals would make a great pet" + ".\n")

#   创造数值列表
for value in range(1,6):
    print(value)
numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,21,2))
print(even_numbers)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

squares = []
for value in range(1,12):
    squares.append(value**2)
print(squares)

digits = [1,2,3,4,5,6,7,8,9,10,11,12]
print(min(digits))
print(max(digits))
print(sum(digits))

squares = [value**2 for value in range(1,11)]
print(squares)

#   动手试一试
#   数到20
for value in range(1,21):
    print(value)

#   一百万
numbers = list(range(1,1000001))
print(numbers)
for value in numbers:
    print(value)

#   计算1~1000000的总和
numbers = list(range(1,1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#   奇数
odd_numbers = list(range(1,21,2))
for value in odd_numbers:
    print(value)

#   3的倍数
result = [num for num in range(3,31)
if num % 3 == 0]
print(result)

#   立方
cubes = [value**3 for value in range(1,11)]
print(cubes)
for cube in cubes:
    print(cube)

#   切片
players = ['A','B','C','D']
print(players[:3])
print(players[-3:])

#   遍历切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

#   复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)