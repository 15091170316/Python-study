# --------- 函数定义 ---------
# -- 函数是组织好的、可重复使用的，用来实现单一，或相关联功能的代码段。
# -- 函数能提高应用的模块性和代码的重复利用率。
# -- 函数定义语法：
# def 函数名(参数列表):
#     函数体...
#     return [返回值]
# -- 函数调用语法：
# 函数名(参数列表)
# -- 注：函数必须先定义，后调用；
# --     形参和实参的个数必须一致，类型要匹配；
# --     可以有多个返回值，中间用逗号隔开，接收时返回值的类型为元组（也可以解包接收）；
# 函数的定义和调用：
# def out_line():
#     print("函数定义和调用")
#     print("------------")
# out_line()   # 调用函数
# out_line()   # 调用函数
# 定义一个函数，计算圆的面积
# def circle_area(radius):
#     area = 3.14 * radius * radius
#     return area
# print(f"圆的面积是：{circle_area(5)}")   # 调用函数，传入参数5，返回圆的面积

# --------- 函数说明文档 ---------
# -- 函数说明文档是对函数的功能、参数、返回值等进行说明的文档字符串，通常用于函数的注释和帮助信息。
# -- 函数说明文档的语法为：在函数定义的第一行使用三引号（"""）包裹的字符串，作为函数的文档字符串。
# -- 函数说明文档可以通过函数的__doc__属性访问，也可以使用help()函数查看，或鼠标悬停在函数上查看。
# def sum_and_diff(a, b):
#     """
#     计算两个数的和与差
#     Args:
#         a (int/float): 第一个数
#         b (int/float): 第二个数
#     Returns:
#         int/float: 两数之和
#         int/float: 两数之差
#     """
#     sum = a + b
#     diff = a - b
#     return sum, diff   # 返回两个值，类型为元组
# result = sum_and_diff(5, 3)   # 调用函数，传入参数5和3，返回两个值
# print(type(result))   # 返回值的类型为元组
# print(f"和为：{result[0]}，差为：{result[1]}")   # 通过索引访问返回
# sum, diff = sum_and_diff(5, 3)   # 解包接收返回值
# print(f"和为：{sum}，差为：{diff}")

# --------- global全局关键字 ---------
# -- global关键字用于在函数内部声明全局变量，使得函数内部可以访问和修改全局变量的值。
# -- global关键字只能在函数内部使用，不能在函数外部使用。
# -- 注：尽量避免使用global关键字，因为它会破坏函数的封装性和可维护性，建议使用函数参数和返回值来传递数据。
# num = 10   # 全局变量
# def change_num():
#     global num   # 声明函数中使用全局变量的num
#     num = 20   # 修改全局变量的值，若不使用global关键字，则会在函数内部创建一个新的局部变量num，函数外部的num不会被修改
#     print(f"函数内部的num值为：{num}")  # 20
# change_num()
# print(f"函数外部的num值为：{num}")   # 20

# --------- 函数参数 ---------
# -- 函数参数是函数定义时用于接收外部传入数据的变量，可以分为位置参数、默认参数、可变参数和关键字参数。
# -- 位置参数：
# def greet(name, age):
#     print(f"你好，我叫{name}，今年{age}岁。")
# greet("张三", 18)   # 位置参数，按照参数定义的顺序传入
# -- 默认参数/缺省参数：默认参数必须放在位置参数的后面，否则会报错。可以有多个默认参数，但也必须放在位置参数的后面
# def greet(name, age=18):      
#     print(f"你好，我叫{name}，今年{age}岁。")
# greet("李四")   # 默认参数，age未传入，使用默认值
# -- 可变参数/不定长参数：用于接收不确定数量的参数，使用*args表示可变参数，接收的是一个元组，可以通过索引访问
# def greet(*names):
#     print(type(names))   # <class 'tuple'>
#     for name in names:
#         print(f"你好，我叫{name}。")
# greet("王五", "赵六", "孙七")   # 可变参数
# -- 关键字参数：
# def greet(**kwargs):          # kwargs是一个字典，可以通过key访问value
#     print(type(kwargs))   # <class 'dict'>
#     for key, value in kwargs.items():
#         print(f"{key}：{value}")
# greet(name="周八", age=20, gender="男")   # 关键字参数，传入的参数名必须与函数定义中的参数名一致，或者在函数定义中使用不定长参数**kwargs接收

# --------- 匿名函数 ---------
# -- 匿名函数是没有名字的函数，使用lambda关键字定义，通常用于简单的函数操作。
# -- 匿名函数的语法为：lambda 参数列表: 函数体表达式(单行)
# -- 匿名函数可以赋值给变量，也可以作为参数传递给其他函数。
# -- 匿名函数的使用场景：当函数体较简单（单行表达式），且只在某个地方使用一次时，可以使用匿名函数，避免定义一个完整的函数（通常作为高阶函数的参数使用）。
# lambda: print("Hello, World!")   # 定义一个匿名函数，没有参数，没有返回值，函数体为print("Hello, World!")
# lambda x,y: x + y   # 定义一个匿名函数，有两个参数，返回两个参数的和
# add = lambda x, y: x + y   # 将匿名函数赋值给变量add，就可以通过add调用匿名函数了
# print(add(5, 3))   # 调用匿名函数
# 匿名函数案例：列表根据元素长度排序
# language = ['Python', 'Java', 'C++', 'JavaScript', 'Go']
# language.sort(key = lambda item: len(item))   # 使用匿名函数作为key参数，按照元素长度排序
# print(language)
# language.sort(key = lambda item: len(item), reverse=True)   # 使用匿名函数作为key参数，按照元素长度降序排序
# print(language)

# --------- 函数递归 ---------
# -- 函数递归是指函数在函数体内调用自身的编程技巧，通常用于解决具有重复性和分治性质的问题。
# -- 注意：递归函数必须有终止条件，否则会导致无限递归，最终引发栈溢出错误。
# 案例：计算n的阶乘
# def jc(n):
#     if n == 1:
#         return 1
#     else:
#         return n * jc(n - 1)    # 递归调用自身，直到n等于1
# print(jc(10))   # 计算10的阶乘

# ---------- 类型注解 ---------
# -- 类型注解是Python中的一种语法特性，用于明确标识变量、函数参数和返回值的数据类型，增强代码的可读性和可维护性。
# -- 类型注解只是提供类型提示，并不会影响代码的运行，也不会进行类型检查，Python仍然是动态类型语言。
# -- 类型注解的语法为：变量名: 类型 = 值
# num: int = 10   # 变量num的类型为int
# no: None = None   # 变量no的类型为None
# name: str = "Alice"   # 变量name的类型为str
# arr1: list = [1, 2, 3]   # 变量arr1的类型为list
# arr2: list[int] = [1, 2, 3]   # 变量arr2的类型为list，且列表中的元素类型为int
# arr3: list[str | int] = ["Alice", 1, "Bob", 2]   # 变量arr3的类型为list，且列表中的元素类型为str或int
# ids: set[str] = {"id1", "id2", "id3"}   # 变量ids的类型为set，且集合中的元素类型为str
# options: dict[str, int] = {"add": 1, "sub": 2}   # 变量options的类型为dict，且字典中的键类型为str，值类型为int
# goods: tuple[str, int, float] = ("apple", 10, 5.5)   # 变量goods的类型为tuple，且元组中的元素类型为str、int和float
# anything: Any = "Hello"   # 变量anything的类型为Any，表示可以是任意类型

# ---------- 函数的类型注解 ---------
# -- 函数的类型注解用于标识函数参数和返回值的数据类型，增强代码的可读性和可维护性。
# -- 函数的类型注解语法为：def 函数名(参数名: 类型, ...) -> 返回值类型:
# 语法案例：
# def add(x: int, y: int) -> int:
#     return x + y
# def calc_data(data: list[int]) -> tuple[int, float]:    # 注意：函数有多个返回值时，返回值类型为元组，元组中每个元素的类型用逗号隔开
#     total = sum(data)
#     avg = total / len(data)
#     return total, avg

