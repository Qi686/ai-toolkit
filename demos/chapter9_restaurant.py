class Dog():
    """一次模拟小狗的简单尝试"""
   
    def __init__(self, name, age):
        """初始化属性name和age""" 
        self.name = name
        self.age = age
         
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")
 
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")
my_dog = Dog('willie', 6)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.name



class Dog():
    """一次模拟小狗的简单尝试"""
   
    def __init__(self, name, age):
        """初始化属性name和age""" 
        self.name = name
        self.age = age
         
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")
 
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")
my_dog = Dog('willie', 6)
my_dog.sit() 
my_dog.roll_over()


class Dog():
    """一次模拟小狗的简单尝试"""
   
    def __init__(self, name, age):
        """初始化属性name和age""" 
        self.name = name
        self.age = age
         
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")
 
    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")
my_dog = Dog('willie', 6) 
your_dog = Dog('lucy', 3) 
 
print("My dog's name is " + my_dog.name.title() + ".") 
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit() 

print("\nYour dog's name is " + your_dog.name.title() + ".") 
print("Your dog is " + str(your_dog.age) + " years old.") 
your_dog.sit()


#   动手试一试

# 定义餐馆类
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        # 初始化餐馆名称、菜系
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        # 描述餐馆信息
        print(f"餐馆名称：{self.restaurant_name}")
        print(f"菜系类型：{self.cuisine_type}")

    def open_restaurant(self):
        # 营业提示
        print(f"{self.restaurant_name} 正在营业中！")

# 创建实例
restaurant = Restaurant("老四川火锅", "川菜")

# 直接打印两个属性
print("餐馆名字：", restaurant.restaurant_name)
print("菜系：", restaurant.cuisine_type)
print("-" * 20)

# 调用两个方法
restaurant.describe_restaurant()
restaurant.open_restaurant()


# 沿用上面定义的 Restaurant 类
# 创建3个不同餐馆实例
rest1 = Restaurant("肯德基", "西式快餐")
rest2 = Restaurant("兰州拉面", "西北面食")
rest3 = Restaurant("寿司屋", "日料")

# 分别调用描述方法
print("===== 第一家餐馆 =====")
rest1.describe_restaurant()
print("===== 第二家餐馆 =====")
rest2.describe_restaurant()
print("===== 第三家餐馆 =====")
rest3.describe_restaurant()


class User:
    def __init__(self, first_name, last_name, age, city, hobby):
        # 基础姓名 + 其他扩展属性
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.hobby = hobby

    def describe_user(self):
        # 打印用户完整信息
        full_name = f"{self.first_name}{self.last_name}"
        print(f"用户姓名：{full_name}")
        print(f"年龄：{self.age}，所在城市：{self.city}")
        print(f"兴趣爱好：{self.hobby}")

    def greet_user(self):
        # 个性化问候
        print(f"你好，{self.first_name}{self.last_name}，欢迎光临！")

# 创建多个用户实例
user1 = User("李", "华", 22, "上海", "打篮球")
user2 = User("张", "小美", 19, "杭州", "画画")
user3 = User("王", "子轩", 25, "成都", "旅游")

# 逐个调用两个方法
print("===== 用户1信息 =====")
user1.describe_user()
user1.greet_user()

print("\n===== 用户2信息 =====")
user2.describe_user()
user2.greet_user()

print("\n===== 用户3信息 =====")
user3.describe_user()
user3.greet_user()


class Car(): 
    """一次模拟汽车的简单尝试""" 
 
    def __init__(self, make, model, year): 
        """初始化描述汽车的属性""" 
        self.make = make 
        self.model = model 
        self.year = year 
         
    def get_descriptive_name(self): 
        """返回整洁的描述性信息""" 
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
        return long_name.title() 
     
my_new_car = Car('audi', 'a4', 2016) 
print(my_new_car.get_descriptive_name())


class Car(): 
     
    def __init__(self, make, model, year): 
        """初始化描述汽车的属性""" 
        self.make = make 
        self.model = model 
        self.year = year 
        self.odometer_reading = 0 
         
    def get_descriptive_name(self): 
        """返回整洁的描述性信息""" 
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
        return long_name.title()
     
    def read_odometer(self): 
        """打印一条指出汽车里程的消息""" 
        print("This car has " + str(self.odometer_reading) + " miles on it.") 
     
my_new_car = Car('audi', 'a4', 2016) 
print(my_new_car.get_descriptive_name()) 
my_new_car.read_odometer()


class Car(): 
     
    def __init__(self, make, model, year): 
        """初始化描述汽车的属性""" 
        self.make = make 
        self.model = model 
        self.year = year 
        self.odometer_reading = 0 
         
    def get_descriptive_name(self): 
        """返回整洁的描述性信息""" 
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
        return long_name.title()
     
    def read_odometer(self): 
        """打印一条指出汽车里程的消息""" 
        print("This car has " + str(self.odometer_reading) + " miles on it.") 
     
my_new_car = Car('audi', 'a4', 2016) 
print(my_new_car.get_descriptive_name()) 

my_new_car.odometer_reading = 23 
my_new_car.read_odometer()


class Car(): 
     
    def __init__(self, make, model, year): 
        """初始化描述汽车的属性""" 
        self.make = make 
        self.model = model 
        self.year = year 
        self.odometer_reading = 0 
         
    def get_descriptive_name(self): 
        """返回整洁的描述性信息""" 
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
        return long_name.title()
     
    def read_odometer(self): 
        """打印一条指出汽车里程的消息""" 
        print("This car has " + str(self.odometer_reading) + " miles on it.") 

    def update_odometer(self, mileage): 
        """将里程表读数设置为指定的值""" 
        self.odometer_reading = mileage

my_new_car = Car('audi', 'a4', 2016) 
print(my_new_car.get_descriptive_name()) 

my_new_car.update_odometer(23) 
my_new_car.read_odometer()


class Car(): 
     
    def __init__(self, make, model, year): 
        """初始化描述汽车的属性""" 
        self.make = make 
        self.model = model 
        self.year = year 
        self.odometer_reading = 0 
         
    def get_descriptive_name(self): 
        """返回整洁的描述性信息""" 
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
        return long_name.title()
     
    def read_odometer(self): 
        """打印一条指出汽车里程的消息""" 
        print("This car has " + str(self.odometer_reading) + " miles on it.") 

    def update_odometer(self, mileage): 
        """ 
        将里程表读数设置为指定的值 
        禁止将里程表读数往回调 
        """
        self.odometer_reading = mileage

        if mileage >= self.odometer_reading: 
            self.odometer_reading = mileage 
        else: 
            print("You can't roll back an odometer!")

my_new_car = Car('audi', 'a4', 2016) 
print(my_new_car.get_descriptive_name()) 

my_new_car.update_odometer(23) 
my_new_car.read_odometer()


class Car(): 
     
    def __init__(self, make, model, year): 
        """初始化描述汽车的属性""" 
        self.make = make 
        self.model = model 
        self.year = year 
        self.odometer_reading = 0 
         
    def get_descriptive_name(self): 
        """返回整洁的描述性信息""" 
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
        return long_name.title()
     
    def read_odometer(self): 
        """打印一条指出汽车里程的消息""" 
        print("This car has " + str(self.odometer_reading) + " miles on it.") 

    def update_odometer(self, mileage): 
        """ 
        将里程表读数设置为指定的值 
        禁止将里程表读数往回调 
        """
        self.odometer_reading = mileage
    def increment_odometer(self, miles): 
        """将里程表读数增加指定的量""" 
        self.odometer_reading += miles

my_used_car = Car('subaru', 'outback', 2013) 
print(my_used_car.get_descriptive_name()) 

my_used_car.update_odometer(23500) 
my_used_car.read_odometer() 

my_used_car.increment_odometer(100) 
my_used_car.read_odometer()


#   动手试一试

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        # 新增就餐人数属性，默认0
        self.number_served = 0

    def describe_restaurant(self):
        print(f"餐馆名称：{self.restaurant_name}")
        print(f"菜系：{self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} 正在营业！")

    # 设置就餐人数
    def set_number_served(self, num):
        self.number_served = num

    # 增加就餐人数
    def increment_number_served(self, add_num):
        self.number_served += add_num


# 创建实例
restaurant = Restaurant("湘味小馆", "湘菜")

# 1. 打印初始就餐人数
print(f"初始就餐人数：{restaurant.number_served}")

# 直接修改属性并打印
restaurant.number_served = 30
print(f"直接修改后就餐人数：{restaurant.number_served}")

# 调用set_number_served设置人数
restaurant.set_number_served(80)
print(f"调用set方法后就餐人数：{restaurant.number_served}")

# 调用递增方法，假设一天接待120人
restaurant.increment_number_served(120)
print(f"增加当日客流后总就餐人数：{restaurant.number_served}")


class User:
    def __init__(self, first_name, last_name, age, city, hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.hobby = hobby
        # 新增登录尝试次数，默认0
        self.login_attempts = 0

    def describe_user(self):
        full_name = self.first_name + self.last_name
        print(f"姓名：{full_name}，年龄：{self.age}，城市：{self.city}，爱好：{self.hobby}")

    def greet_user(self):
        print(f"你好，{self.first_name}{self.last_name}！")

    # 登录次数+1
    def increment_login_attempts(self):
        self.login_attempts += 1

    # 重置登录次数为0
    def reset_login_attempts(self):
        self.login_attempts = 0


# 创建用户实例
user = User("陈", "一诺", 21, "南京", "看书")

# 多次调用递增方法
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# 打印递增后的次数
print(f"当前登录尝试次数：{user.login_attempts}")

# 重置次数
user.reset_login_attempts()
print(f"重置后登录尝试次数：{user.login_attempts}")