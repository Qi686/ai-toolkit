def greet_user():
    """显示简单的问候语"""
    print("hello!")

greet_user()


def greet_user(username):
    """显示简单的问候语"""
    print("hello, " + username.title() + "!")

greet_user('jesse')
greet_user('sarah')


#   动手试一试

# 定义函数
def display_message():
    print("本章我学习了Python中函数的定义、调用以及函数基础用法。")

# 调用函数
display_message()


# 定义带形参title的函数
def favorite_book(title):
    print(f"One of my favorite books is {title}.")

# 调用函数，传入实参
favorite_book("Alice in Wonderland")
# 也可以换其他书籍测试
favorite_book("三国演义")


def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
describe_pet(animal_type='hamster', pet_name='harry')


def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='willie')
describe_pet(pet_name='harry', animal_type='hamster')


def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

#   一条名为Willie的小狗 
describe_pet('willie')
describe_pet(pet_name='willie')

#   一只名为Harry的仓鼠 
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')


#   动手试一试

# 定义函数
def make_shirt(size, word):
    print(f"这件T恤尺码是{size}，印的文字是：{word}")

# 位置实参调用
make_shirt("L", "Hello World")
# 关键字实参调用
make_shirt(word="Keep Going", size="M")


# size默认大号L，文字默认I love Python
def make_shirt(size="L", word="I love Python"):
    print(f"这件T恤尺码是{size}，印的文字是：{word}")

# 默认大号、默认文字
make_shirt()
# 中号、默认文字
make_shirt(size="M")
# 任意尺码，自定义文字
make_shirt(size="S", word="I love Coding")


# 国家默认值设为China
def describe_city(city, country="China"):
    print(f"{city} is in {country}.")

# 三座城市，至少一座不属于默认国家
describe_city("Beijing")
describe_city("Shanghai")
describe_city("Tokyo", "Japan")


def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)


def get_formatted_name(first_name,middle_name,last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi','lee','hendrix')
print(musician)


def get_formatted_name(first_name, last_name, middle_name=""):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)


def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)


def build_person(first_name, last_name, age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age: 
        person['age'] = age
    return person
    
musician = build_person('jimi', 'hendrix', age=27)
print(musician)


def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

# 这是一个无限循环! 
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break 
     
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")


#   动手试一试

def city_country(city, country):
    # 返回指定格式字符串
    return f'"{city}, {country}"'

# 三组城市国家调用
print(city_country("Santiago", "Chile"))
print(city_country("Beijing", "China"))
print(city_country("Paris", "France"))


# 新增可选参数song_num，默认None
def make_album(singer, album_name, song_num=None):
    album = {"singer": singer, "album": album_name}
    # 如果传入歌曲数量则加入字典
    if song_num:
        album["song_count"] = song_num
    return album

# 3个专辑，其中1个指定歌曲数
album1 = make_album("周杰伦", "七里香")
album2 = make_album("林俊杰", "江南")
album3 = make_album("Taylor Swift", "1989", 13)

print(album1)
print(album2)
print(album3)


def make_album(singer, album_name, song_num=None):
    album = {"singer": singer, "album": album_name}
    if song_num:
        album["song_count"] = song_num
    return album

print("=== 专辑录入系统 ===")
print("输入'q'可随时退出程序\n")

while True:
    # 获取歌手名
    singer_input = input("请输入歌手名字：")
    if singer_input.lower() == "q":
        print("程序退出！")
        break
    
    # 获取专辑名
    album_input = input("请输入专辑名称：")
    if album_input.lower() == "q":
        print("程序退出！")
        break
    
    # 询问是否输入歌曲数量
    num_input = input("输入专辑歌曲数量（无需则直接回车）：")
    if num_input.lower() == "q":
        print("程序退出！")
        break
    
    if num_input:
        album_info = make_album(singer_input, album_input, int(num_input))
    else:
        album_info = make_album(singer_input, album_input)
    
    print("生成专辑信息：", album_info)
    print("-" * 30)


def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)


# 首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
 
# 模拟打印每个设计，直到没有未打印的设计为止
#  打印每个设计后，都将其移到列表completed_models中
while unprinted_designs:
    current_design = unprinted_designs.pop()
     
    #模拟根据设计制作3D打印模型的过程
    print("Printing model: " + current_design)
    completed_models.append(current_design)
     
# 显示打印好的所有模型
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)


def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其移到列表completed_models中
    """ 
    while unprinted_designs:
        current_design = unprinted_designs.pop()
     
        # 模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)


#   动手试一试

# 定义打印魔术师名单的函数
def show_magicians(magicians):
    for magician in magicians:
        print(magician)

# 创建魔术师列表
magician_names = ["大卫", "刘谦", "哈利"]
# 调用函数
show_magicians(magician_names)


def show_magicians(magicians):
    """打印所有魔术师名字"""
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """修改原列表，给每个名字加上 the Great"""
    # 倒着遍历，避免索引错乱
    for i in range(len(magicians)):
        magicians[i] = "the Great " + magicians[i]

# 原始名单
magician_names = ["大卫", "刘谦", "哈利"]
# 修改列表
make_great(magician_names)
# 打印验证
show_magicians(magician_names)


def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    # 新建空列表存放修改后的名字
    great_list = []
    for name in magicians:
        great_list.append("the Great " + name)
    # 返回新列表
    return great_list

# 原始列表
original_magicians = ["大卫", "刘谦", "哈利"]
# 传入副本，接收修改后的新列表
great_magicians = make_great(original_magicians[:])

print("=== 原始魔术师名单 ===")
show_magicians(original_magicians)

print("\n=== 加上 the Great 的名单 ===")
show_magicians(great_magicians)


def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


def make_pizza(*toppings):
    """概述要制作的比萨""" 
    print("\nMaking a pizza with the following toppings:") 
    for topping in toppings: 
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


def make_pizza(size, *toppings):  
    """概述要制作的比萨""" 
    print("\nMaking a " + str(size) +  
          "-inch pizza with the following toppings:")  
    for topping in toppings:  
        print("- " + topping)  
         
make_pizza(16, 'pepperoni')  
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


def build_profile(first, last, **user_info): 
    """创建一个字典，其中包含我们知道的有关用户的一切""" 
    profile = {} 
    profile['first_name'] = first 
    profile['last_name'] = last 
    for key, value in user_info.items():

        profile[key] = value 
    return profile 
user_profile = build_profile('albert', 'einstein', 
                            location='princeton', 
                            field='physics') 
print(user_profile)


#   动手试一试

# *toppings 收集所有传入的食材，打包成元组
def make_sandwich(*toppings):
    print("\n正在制作包含以下食材的三明治：")
    for topping in toppings:
        print(f"- {topping}")

# 三次调用，参数数量不同
make_sandwich("生菜")
make_sandwich("火腿", "芝士")
make_sandwich("牛肉", "番茄", "洋葱", "沙拉酱")


# 收集任意数量关键字实参到字典
def build_profile(first, last, **user_info):
    profile = {"first": first, "last": last}
    profile.update(user_info)
    return profile

# 传入名、姓 + 三组自定义键值对
me = build_profile("Zhang", "Wei", age=20, hobby="coding", city="Shanghai")
print(me)


def make_car(manufacturer, model, **extra_info):
    car_info = {"brand": manufacturer, "model": model}
    car_info.update(extra_info)
    return car_info

# 示例调用，必传品牌型号，外加color、tow_package
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)