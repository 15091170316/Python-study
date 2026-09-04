# ---------if条件语句---------
# age = int(input("请输入你的年龄："))
# if age < 18:
#     print("你还未成年！")
#     print("请好好学习，天天向上！")     # python是通过缩进来表示代码块的，缩进的空格数可以是任意的，但必须保持一致
# elif 18 <= age < 60:       # 这是连续比较运算符，相当于age >= 18 and age < 60
#     print("你是成年人！")
#     print("请好好工作，努力赚钱！")
# else:
#     print("你是老年人！")
#     print("请好好享受，安度晚年！")

# ---------match模式匹配---------
# --从上往下进行匹配，匹配到第一个符合条件的case分支就执行，不会继续往下匹配
# day = input("请输入今天是周几：")
# match day:
#     case "1":
#         print("今天是周一！")
#     case "2":
#         print("今天是周二！")
#     case "3":
#         print("今天是周三！")
#     case "4":
#         print("今天是周四！")
#     case "5":
#         print("今天是周五！")
#     case "6" | "7":                # | 表示或的关系
#         print("今天是周末！")
#     case _:                        # _ 表示默认情况，即没有匹配到任何一种情况
#         print("输入有误！")

# num1 = float(input("请输入第一个数字："))
# num2 = float(input("请输入第二个数字："))
# operator = input("请输入运算符（+ - * /）：")
# match operator:
#     case "+":
#         result = num1 + num2
#     case "-":
#         result = num1 - num2
#     case "*":
#         result = num1 * num2
#     case "/" if (num2 != 0):   # case后面可以添加条件判断(3.10版本新增的功能)
#         result = num1 / num2
#     case "/" if (num2 == 0):
#         result = "除数不能为零！"
#     case _:
#         result = "输入的运算符有误！"
# print(f"{num1} {operator} {num2} = {result}")

# ---------while循环语句---------
# n = 0
# while n < 5:
#     print(f"当前的值为：{n}")
#     n += 1
# else:       # while循环还可以有一个else分支，当循环条件正常结束时执行else分支的代码（else是可选的、非正常结束不会执行）
#     print("循环结束！")

# ---------for循环语句---------
# str = "hello world！"
# for i in str:
#     print(i)
# else:       # for循环还可以有一个else分支，当循环正常结束时执行else分支的代码（else是可选的）
#     print("循环结束！")

# range()函数可以生成一个整数序列，常用于for循环中（参数可以为1个、2个或3个，具有特定的起始、结束和步长值）
# sum = 0
# for i in range(1, 101):
#     if(i % 2 == 1):
#         sum += i
# print(f"1到100之间的奇数的和为：{sum}") 

# sum2 = 0
# for i in range(1, 101, 2):   # 通过设置步长为2，可以直接生成1到100之间的奇数序列
#     sum2 += i
# print(f"1到100之间的奇数的和为：{sum2}")

# ---------嵌套循环---------
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print(f"{j} x {i} = {i*j}", end="\t")   # end参数可以指定print函数的结尾字符，默认为换行符\n，这里设置为制表符\t，使得输出在同一行
#     print()     # 每次内层循环结束后，输出一个换行符，使得每一行输出一个乘法表的结果

# ---------break和continue语句---------
# import random
# random_num = random.randint(1, 100)   # 生成一个1到100之间的随机整数(包含1和100)
# while True:
#     guess_num = int(input("请输入一个1到100之间的整数："))
#     if guess_num == random_num:
#         print("恭喜你，猜对了！")
#         break   # 退出循环
#     elif guess_num < random_num:
#         print("你猜的数字太小了！")
#     else:
#         print("你猜的数字太大了！")
