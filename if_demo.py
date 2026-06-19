cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

car = 'bmw'
if car == 'bmw':
    print('True')
else:
    print('false')

car = 'audi'
if car == 'bmw':
    print('ture')
else:
    print('false')

car = 'AUDI'
if car.lower() == 'audi':
    print('\nture')
else:
    print('false')

requested_topping = 'mushrooms'
if requested_topping != 'anchovie':
    print('\nhold the anchovies!')

age = 18
if age > 17:
    print('\nThat is not the correct age.Please try again')
else:
    print('true')

age_0 = 22
age_1 = 18
if (age_0 >= 21) and (age_1 >= 21):
    print('\nture')
else:
    print('\nfalse')

age_0 = 22
age_1 = 22
if (age_0 >= 21) and (age_1 >= 21):
    print('\nture')
else:
    print('\nfalse')

age_0 = 22
age_1 = 18
if (age_0 >= 21) or (age_1 >= 21):
    print('\nture')
else:
    print('\nfalse')

age_0 = 18
age_1 = 18
if (age_0 >= 21) or (age_1 >= 21):
    print('\nture')
else:
    print('\nfalse')

fruits = ['apple','banana','grape']
if 'apple' in fruits:
    print('\nture')
else:
        print('\nture')
if 'pineapple' in fruits:
    print('\nIt is ture')
else:
    print('\nIt is false')

banned_users = ['andrew', 'carolina', 'david'] 
user = 'marie'
if user not in banned_users: 
    print("\n"+user.title() + ", you can post a response if you wish.")

num = 0
print("\nIs num == 0?I predit ture")
print(num == 0)

print("\nIs num == 1? I predict False.")
print(num == 1)

age = 17
if age >= 18:
    print('\nYou are old enough to vote!')
    print('Have you registered to vote yet?')
else:
    print("Sorry, you are too young to vote.") 
    print("Please register to vote as soon as you turn 18!")

age = 12 
if age < 4: 
    print("\nYour admission cost is $0.") 
elif age < 18: 
    print("\nYour admission cost is $5.") 
else: 
    print("\nYour admission cost is $10.")

age = 12 
if age < 4: 
    price = 0
elif age < 18: 
    price = 5
else: 
    price = 10
print("\nYour admission cost is $" + str(price) + ".")

age = 30 
if age < 4: 
    price = 0
elif age < 18: 
    price = 5
elif age < 65: 
    price = 10
else: 
    price = 5
print("\nYour admission cost is $" + str(price) + ".")

age = 70 
if age < 4: 
    price = 0
elif age < 18: 
    price = 5
elif age < 65: 
    price = 10
elif age >= 65: 
    price = 5
print("\nYour admission cost is $" + str(price) + ".")

requested_toppings = ['mushrooms', 'extra cheese'] 
if 'mushrooms' in requested_toppings: 
    print("\nAdding mushrooms.") 
if 'pepperoni' in requested_toppings: 
    print("\nAdding pepperoni.") 
if 'extra cheese' in requested_toppings: 
    print("\nAdding extra cheese.") 
print("\nFinished making your pizza!")

#   动手试一试

#   外星人颜色#1
alien_color = 'green'
if alien_color == 'green':
    print("You earned 5 points!")

alien_color = 'red'
if alien_color == 'green':
    print("You earned 5 points!")

#   外星人颜色#2
alien_color = 'green'
if alien_color == 'green':
    print("You earned 5 points for shooting the green alien!")
else:
    print("You earned 10 points!")

alien_color = 'yellow'
if alien_color == 'green':
    print("You earned 5 points for shooting the green alien!")
else:
    print("You earned 10 points!")

#    外星人颜色#3
alien_color = 'green'
if alien_color == 'green':
    print("You get 5 points!")
elif alien_color == 'yellow':
    print("You get 10 points!")
else:
    print("You get 15 points!")

alien_color = 'yellow'
if alien_color == 'green':
    print("You get 5 points!")
elif alien_color == 'yellow':
    print("You get 10 points!")
else:
    print("You get 15 points!")

alien_color = 'red'
if alien_color == 'green':
    print("You get 5 points!")
elif alien_color == 'yellow':
    print("You get 10 points!")
else:
    print("You get 15 points!")

#   人生的不同阶段
age = 25
if age < 2:
    print("He is a baby.")
elif age < 4:
    print("He is a toddler.")
elif age < 13:
    print("He is a kid.")
elif age < 20:
    print("He is a teenager.")
elif age < 65:
    print("He is an adult.")
else:
    print("He is an elder.")
#   喜欢的水果
favorite_fruits = ['apple', 'banana', 'grape']

if 'banana' in favorite_fruits:
    print("You really like bananas!")
if 'apple' in favorite_fruits:
    print("You really like apples!")
if 'orange' in favorite_fruits:
    print("You really like oranges!")
if 'grape' in favorite_fruits:
    print("You really like grapes!")
if 'peach' in favorite_fruits:
    print("You really like peaches!")

#   动手试一试

#   以特殊方式跟管理员打招呼
usernames = ['admin', 'eric', 'tom', 'lily', 'jack']
for user in usernames:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again")

#   处理没有用户的情形
usernames = ['admin', 'eric', 'tom', 'lily', 'jack']
if usernames:
    for user in usernames:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again")
else:
    print("We need to find some users!")

usernames = []
if usernames:
    for user in usernames:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again")
else:
    print("We need to find some users!")

#   检查用户名
current_users = ['John', 'Eric', 'Tom', 'Lily', 'Jack']
new_users = ['john', 'Lucy', 'Mike', 'TOM', 'Sam']
current_lower = [name.lower() for name in current_users]
for new_name in new_users:
    if new_name.lower() in current_lower:
        print(f"Username {new_name} has been taken, please enter another name.")
    else:
        print(f"Username {new_name} is available.")

#   序数
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in numbers:
    if num == 1:
        print(f"{num}st")
    elif num == 2:
        print(f"{num}nd")
    elif num == 3:
        print(f"{num}rd")
    else:
        print(f"{num}th")