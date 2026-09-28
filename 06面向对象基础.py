# ---------- 类与对象 ---------
# -- 类：抽象的模板，用来描述具有相同属性和方法的对象集合
# -- 对象：是类的实例，通过类定义出来的一个具体的东西
# -- 类的创建：class 类名：
# -- 类的命名规范：首字母大写，多个单词用大驼峰命名法
# -- 类的属性：类中的变量，用来描述类的特征
# -- 类的方法：类中的函数，用来描述类的行为
# -- 类的实例化：创建对象的过程，使用类名()来创建对象
# -- 示例：
# class Student:
#     # 类的属性
#     name = "张三"
#     age = 18
#     # 类的方法
#     def study(self):      # self表示对象本身，在调用时不需要传入，由Python解释器自动传入
#         print(f"{self.name}正在学习")
# # 创建对象
# student1 = Student()
# # 访问对象的属性和方法
# print(student1.name)   # 访问对象的属性
# print(student1.age)    # 访问对象的属性
# student1.study()       # 调用对象的方法
# print(student1.__class__)   # 查看对象所属的类
# student1.sex = "男"   # 动态添加对象的属性
# print(student1.__dict__)    # 查看对象的属性字典（不包含类属性）

# ---------- __init__方法（构造方法）---------
# -- __init__方法是类的构造方法，对象创建后自动调用，用于在创建对象时初始化对象的属性
# -- __init__方法的第一个参数必须是self，表示对象本身，self参数在调用时不需要传入，由Python解释器自动传入
# -- 示例：
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def study(self):
#         print(f"{self.name}正在学习")
#     def studyLocation(self, location):
#         print(f"{self.name}正在{location}学习")
# student2 = Student("李四", 20)   # 创建对象时传入参数，自动调用__init__方法
# print(student2.name)   # 访问对象的属性
# print(student2.age)    # 访问对象的属性
# student2.study()       # 调用对象的方法
# student2.studyLocation("教室")   # 调用对象的方法，并传入参数
# print(student2.__dict__)    # 查看对象的属性字典（包含实例属性）

# ---------- 魔法方法 ---------
# -- 魔法方法：以双下划线开头和结尾的方法，具有特殊的功能
# -- 魔法方法不需要我们手动调用，在特定的情况下Python会自动调用
# -- __init__方法：构造方法，在创建对象时自动调用
# -- __str__方法：当使用print函数打印对象时，会自动调用该方法，返回一个字符串，作为对象的字符串表示
# -- __del__方法：析构方法，在对象被销毁时自动调用
# -- __eq__方法：比较两个对象是否相等，返回一个布尔值
# -- __len__方法：返回对象的长度
# -- 示例：
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"姓名：{self.name}，年龄：{self.age}"
    def __del__(self):
        print(f"{self.name}对象被销毁！")
    def __eq__(self, other):   # 比较两个对象否相等，对比内容可以通过该方法自定义，若不定义（重写）则默认比较两个对象的内存地址
        return self.name == other.name and self.age == other.age
    def __len__(self):
        return len(self.name)
student3 = Student("王五", 22)
student4 = Student("王五", 22)
print(student3)                 # 调用__str__方法
print(student3 == student4)     # 调用__eq__方法
print(len(student3))            # 调用__len__方法
del student4                    # 调用__del__方法



