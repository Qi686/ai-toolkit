message = input("Tell me something, and I will repeat it back to you: ") 
print(message)

name = input("Please enter your name: ") 
print("Hello, " + name + "!")


prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("Hello, " + name + "!")


age = input("How old are you? ") 
age = int(age)
if age >= 18:
    print('\nture')


4 % 3


number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0: 
    print("\nThe number " + str(number) + " is even.")
else: 
    print("\nThe number " + str(number) + " is odd.")


#   动手试一试

# 获取用户输入车型
car_type = input("What kind of car would you like to rent? ")
# 输出提示语句
print(f"Let me see if I can find you a {car_type.title()}.")

# input获取的是字符串，需要转成整数
guest_num = int(input("How many people will be dining? "))

if guest_num > 8:
    print("Sorry, we don't have an empty table for your group.")
else:
    print("We have an empty table available for you.")

num = int(input("Please enter a number: "))

# 取模 %，余数为0代表能整除10
if num % 10 == 0:
    print(f"{num} is a multiple of 10.")
else:
    print(f"{num} is not a multiple of 10.")


current_number = 1 
while current_number <= 5: 
    print(current_number) 
    current_number += 1


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)
     
    if message == 'quit':
        active = False
    else: 
        print(message)


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
while True: 
    city = input(prompt) 
     
    if city == 'quit': 
        break
    else: 
        print("I'd love to go to " + city.title() + "!")


current_number = 4
while current_number < 10:
    current_number += 1 
    if current_number % 2 == 0: 
        continue 

    print(current_number)


x = 1 
while x <= 5: 
    print(x) 
    x += 1


#   动手试一试

# 持续输入配料，输入quit停止
while True:
    topping = input("Please enter a pizza topping, enter 'quit' to stop: ")
    if topping == 'quit':
        break
    print(f"We will add {topping} to your pizza.")

while True:
    age_input = input("Please enter your age, type 'quit' to exit: ")
    if age_input == 'quit':
        break
    age = int(age_input)
    if age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("The ticket price is 10 dollars.")
    else:
        print("The ticket price is 15 dollars.")

active = True  # 控制循环开关的变量
while active:
    topping = input("Enter pizza topping, 'quit' to exit: ")
    # 方式1：break退出
    if topping == 'quit':
        active = False  # 方式2：修改active变量结束循环
        break
    # 方式3：条件判断控制是否执行打印
    if topping != 'quit':
        print(f"We will add {topping} to your pizza.")

while True:
    print("This is an endless loop! Press Ctrl+C to stop.")


#   首先，创建一个待验证用户列表 
#   和一个用于存储已验证用户的空列表 
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

#   验证每个用户，直到没有未验证用户为止 
#   将每个经过验证的列表都移到已验证用户列表中 
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title()) 
    confirmed_users.append(current_user)

#   显示所有已验证的用户 
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat'] 
print(pets) 
while 'cat' in pets: 
    pets.remove('cat') 
print(pets)


responses = {}
#   设置一个标志，指出调查是否继续
polling_active = True
while polling_active:
#   提示输入被调查者的名字和回答
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    #   将答卷存储在字典中
    responses[name] = response

    #   看看是否还有人要参与调查
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
#   调查结束，显示结果
print("\n--- Poll Results ---")
for name, response in responses.items():
        print(name + " would like to climb " + response + ".")


#   动手试一试

# 待制作的三明治订单
sandwich_orders = ['tuna', 'chicken', 'beef', 'egg']
# 存放做好的三明治
finished_sandwiches = []

# 循环制作，把订单转移到完成列表
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

# 打印全部做好的三明治
print("\nAll finished sandwiches:")
for s in finished_sandwiches:
    print(f"- {s}")

# 订单里多次出现 pastrami
sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'chicken', 'pastrami', 'beef']
finished_sandwiches = []

print("Sorry, we have run out of pastrami!")

# 删除所有 pastrami
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# 制作剩余三明治
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nAll finished sandwiches:")
print(finished_sandwiches)

survey_results = {}

while True:
    name = input("What's your name? ")
    place = input("If you could visit one place in the world, where would you go? ")
    survey_results[name] = place

    again = input("Would you like to let another person respond? (yes/no) ")
    if again == 'no':
        break

# 输出所有调查结果
print("\n--- Survey Results ---")
for name, place in survey_results.items():
    print(f"{name}'s dream vacation spot: {place}")