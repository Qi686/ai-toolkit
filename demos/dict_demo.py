aline_0 = {'color': 'greee','points': 5}

print(aline_0['color'])
print(aline_0['points'])

new_points = aline_0['points']
print('\nYou just eared ' + str(new_points) + ' pointss!')


aline_0 = {'color': 'greee','points': 5}
print(aline_0)

aline_0['x_position'] = 0
aline_0['y_position'] = 25
print(aline_0)


aline_0 = {}

aline_0['color'] = 'green'
aline_0['points'] = 5
print(aline_0)


alien_0 = {'color': 'green'} 
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")


alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'} 
print("\nOriginal x-position: " + str(alien_0['x_position']))

#   向右移动外星人
#   据外星人当前速度决定将其移动多远
if alien_0['speed'] == 'slow': 
    x_increment = 1 
elif alien_0['speed'] == 'medium': 
    x_increment = 2 
else: 
    # 这个外星人的速度一定很快 
    x_increment = 3

# 新位置等于老位置加上增量 
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("\nNew x-position: " + str(alien_0['x_position']))


alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
alien_0['speed'] = 'fast'
if alien_0['speed'] == 'slow': 
    x_increment = 1 
elif alien_0['speed'] == 'medium': 
    x_increment = 2 
else: 
    # 这个外星人的速度一定很快 
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("\nNew x-position: " + str(alien_0['x_position']))


alien_0 = {'color': 'green', 'points': 5} 
print(alien_0)

del alien_0['points']
print(alien_0)


favorite_languages = {
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python', 
    }

print("\nSarah's favorite language is " + 
    favorite_languages['sarah'].title() + 
    ".")


#   动手试一试
people = {
    'first_name': 'H',
    'last_name': ' QW',
    'age': 24,
    'city': 'ShangHai'
    }
print(people)

peoples_favorite = {
    'Anana': 5,
    'Banus': 4,
    'Copti': 3,
    'David': 9
    }
print(peoples_favorite)
for name,num in peoples_favorite.items():
    answer = input(f'{name},Do you like {num}?please input yes or no:')
    if answer == 'yes':
        print(f'OK,{name} just like {num}')
    elif answer == 'no':
        print(f'Of course {name} does likes {num}!')
    else:
        print('Just input yes or no')
print("END")


favorite_languages = { 
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python', 
    }

for name in favorite_languages.keys(): 
    print(name.title())

favorite_languages = { 
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python', 
    }
friends = ['phil', 'sarah'] 
for name in favorite_languages.keys(): 
    print(name.title())

    if name in friends: 
        print("  Hi " + name.title() + 
            ", I see your favorite language is " +        
            favorite_languages[name].title() + "!")
        
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")


favorite_languages = { 
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python', 
    }
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

favorite_languages = { 
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python', 
    }
print("The following languages have been mentioned:")
for language in favorite_languages.values(): 
    print(language.title())

favorite_languages = { 
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python', 
    }
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())


#   动手试一试

#   词汇表2
# 定义python词汇字典，先写几个，后面新增5个
vocabulary = {
    'print': '输出内容到控制台',
    'list': '有序可变序列列表',
    'dict': '键值对存储的字典',
    'for': '用于循环遍历的关键字',
    'if': '条件判断语句'
    }

# 新增5个术语
vocabulary['int'] = '整数数字类型'
vocabulary['str'] = '字符串文本类型'
vocabulary['input'] = '获取用户输入'
vocabulary['def'] = '定义函数关键字'
vocabulary['else'] = '条件不成立时执行分支'

# 循环遍历键值对，代替多条print
for word, explain in vocabulary.items():
    print(f"{word}: {explain}")

#   河流
# 河流-国家字典
rivers = {
    'nile': 'egypt',
    'yangtze': 'china',
    'amazon': 'brazil'
    }

# 1. 打印完整句子
print("===河流流经国家===")
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# 2. 只打印所有河流名称
print("\n===所有河流名称===")
for river in rivers.keys():
    print(river.title())

# 3. 只打印所有国家
print("\n===所有流经国家===")
for country in rivers.values():
    print(country.title())

#   调查
# 已参与调查的人和喜欢的语言
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

# 需要调查的人员名单（部分在字典里，部分不在）
people = ['jen', 'sarah', 'tom', 'edward', 'jack', 'phil']

# 遍历名单，区分已调查/未调查
for name in people:
    if name in favorite_languages.keys():
        print(f"Thank you, {name.title()}, for taking the survey!")
    else:
        print(f"{name.title()}, please join our language survey!")

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print("...")

print("Total number of aliens: " + str(len(aliens)))


aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]: 
    if alien['color'] == 'green': 
        alien['color'] = 'yellow' 
        alien['speed'] = 'medium' 
        alien['points'] = 10

for alien in aliens[:5]:
    print(alien)
print("...")

print("Total number of aliens: " + str(len(aliens)))


aliens = []

for alien_number in range(30):
    new_alien = {'color': 'yellow', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    
for alien in aliens[0:3]: 
    if alien['color'] == 'green': 
        alien['color'] = 'yellow' 
        alien['speed'] = 'medium' 
        alien['points'] = 10
    elif alien['color'] == 'yellow': 
        alien['color'] = 'red' 
        alien['speed'] = 'fast' 
        alien['points'] = 15

for alien in aliens[:5]:
    print(alien)
print("...")

print("Total number of aliens: " + str(len(aliens)))


pizza = { 
    'crust': 'thick', 
    'toppings': ['mushrooms', 'extra cheese'], 
    }

print("You ordered a " + pizza['crust'] + "-crust pizza " +
    "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)


favorite_languages = { 
    'jen': ['python', 'ruby'], 
    'sarah': ['c'], 
    'edward': ['ruby', 'go'], 
    'phil': ['python', 'haskell'], 
    }

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())


users = { 
    'aeinstein': { 
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },

    }
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())


#   动手试一试

# 三个独立人字典
person1 = {
    "first_name": "li",
    "last_name": "hua",
    "age": 18,
    "city": "shanghai"
}
person2 = {
    "first_name": "wang",
    "last_name": "ming",
    "age": 20,
    "city": "beijing"
}
person3 = {
    "first_name": "zhang",
    "last_name": "hong",
    "age": 19,
    "city": "guangzhou"
}

# 存放所有字典的列表
people = [person1, person2, person3]

# 遍历列表打印所有人信息
for person in people:
    print(person)

# 多个宠物字典
cat = {"type": "cat", "owner": "Tom"}
dog = {"type": "dog", "owner": "Lily"}
rabbit = {"type": "rabbit", "owner": "Jack"}

# 列表存储所有宠物字典
pets = [cat, dog, rabbit]

# 循环输出
for pet in pets:
    print(pet)

favorite_places = {
    "Tom": ["park", "library"],
    "Lily": ["sea", "mountain", "cafe"],
    "Jack": ["gym"]
    }

# 遍历每个人
for name, places in favorite_places.items():
    print(f"{name} likes these places: {places}")

favorite_numbers = {
    "Anana": [5, 12],
    "Banus": [4, 7, 9],
    "Copti": [3],
    "David": [9, 1, 6]
    }

for name, nums in favorite_numbers.items():
    print(f"{name}'s favorite numbers: {nums}")

cities = {
    "beijing": {
        "country": "china",
        "population": 22000000,
        "fact": "the capital of China"
    },
    "paris": {
        "country": "france",
        "population": 2100000,
        "fact": "famous for Eiffel Tower"
    },
    "tokyo": {
        "country": "japan",
        "population": 37000000,
        "fact": "one of the largest cities in the world"
    }
    }

# 循环打印城市信息
for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"Country: {info['country'].title()}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}")

rivers = {
    'nile': 'egypt',
    'yangtze': 'china',
    'amazon': 'brazil',
    'yellow': 'china',
    'mississippi': 'usa'
}

print("===== All Rivers Information =====")
for river, country in rivers.items():
    r = river.title()
    c = country.title()
    print(f"- {r}: Flows through {c}")

# 单独打印中国河流
print("\n===== Rivers in China =====")
for river, country in rivers.items():
    if country == "china":
        print(river.title())