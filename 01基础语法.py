# ---------字面量---------
# print("Hello world!!!")
# print("Hello python3!!!")
# print("")
# print(" ")
# print(True)
# print(False)
# print(10)
# print(3.14)
# print(None)
# print(True + 1)
# print(False - 1)

# ---------变量(动态类型语言)----------
# num = 3.14
# print(num)
# num = num + 1
# print(num)
# num = "string"
# print(num)
# num1, str1 = 10, "20"
# print(num1, str1)
# a,b,c = 1,2,3
# print(a,b,c)
# c,b,a = a,b,c
# print(a,b,c)

# ---------数据类型---------
# print(type(1), type(1.31), type("hello"), type(True), type(None))
# print(isinstance(1, int))
# print(isinstance(1.31, str))
# print(isinstance(True, int), isinstance(False, bool))
# print(isinstance(None, type(None)))

# ---------str字符串定义---------
# s1 = "hello world"
# s2 = 'hello world'
# s3 = """
#     python中的三引号字符串定义法，
#     是可以直接换行的
#     ！！！！！！！！
# """
# s4 = '''
# hello
#     world
# '''
# print(s1)
# print(s2)
# print(s3)
# print(s4)
"""
    若三引号字符串不赋值，则表示多行注释
"""
# s5 = "hello \"world\""  # \"是转义符，表示字符串中的双引号
# s6 = 'hello \'world\''  # \是转义符
# s7 = "hello \tworld"    # \t是制表符
# s8 = "hello \nworld"    # \n是换行符
# print(s5)
# print(s6)
# print(s7)
# print(s8)

# ---------字符串拼接---------
# string = "hello" + "world1"
# print(string)
# string = "hello" "world2"
# print(string)
# # string = "helloworld3" + 3     # python3中+号两边必须是字符串类型
# # print(string)
# string = "hello" + str(3)     # str()函数可以将数字转换为字符串
# print(string)

# ---------字符串格式化---------
# name = "张三"
# age = 18
# print("我的名字是%s，今年%s岁了。" %(name, age))    # %s是可以自动转化数据类型的
# print("我的名字是%s，今年%d岁了。" %(name, age))    # %s是字符串占位符，%d是整数占位符
# # 也可以通过 f"内容{变量/表达式}" 的方式进行字符串格式化（企业开发中的推荐使用方法）
# print(f"我的名字是{name}, 今年{age}岁了。")

# ---------输入输出---------
# --input()函数可以获取用户输入的内容，默认返回字符串类型
# --print()函数可以输出内容到控制台，默认以空格分隔多个参数，并以换行结尾
# name = input("请输入你的姓名：")
# age = input("请输入你的年龄：")
# print(f"你好，{name}，你今年{age}岁了!")

# ---------运算符---------
# --算术运算符：+ - * / // % **
# --算术运算符的优先级：** > * / // % > + -
# print(10 / 3)   # /是除法，返回商的浮点数结果
# print(10 // 3)  # //是整数除法，返回商的整数部分
# print(10 % 3)   # %是取余运算，返回除法的余数部分
# print(2 ** 3)   # **是指数运算，返回底数的指数次方
# --赋值运算符：= += -= *= /= //= %= **=
# --比较运算符：== != > < >= <=
# print(10 == "10")   # False，类型不同则返回False
# --逻辑运算符：and or not
# n = 13
# print("n是否在10-20之间：", n >= 10 and n <= 20)
# print("n是否在10-20之间：", 10 <= n <= 20)  # python可以使用连续比较运算符

