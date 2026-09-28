# ---------- 异常 ---------
# -- 异常是程序在运行过程中发生的错误，Python 提供了异常处理机制，可以捕获和处理异常，避免程序崩溃。
# -- 异常处理机制使用 try-except 语句实现，try 语句块中的代码是可能发生异常的代码，except 语句块中的代码是处理异常的代码。
# -- 异常处理机制的基本语法如下：
# try:
#     # 可能发生异常的代码
# except [异常类型 as 变量名]:
#     # 处理异常的代码
# [finally:
#     # 无论是否发生异常，都会执行的代码，是可选的]
# -- 异常类型是可选的，如果不指定异常类型，则表示捕获所有类型的异常。
# -- 变量名是可选的，如果不指定变量名，则表示不保存异常信息。
# -- 异常处理机制可以嵌套使用，即在一个 try 语句块中嵌套另一个 try 语句块。
# -- 示例：
# try:
#     # 可能发生异常的代码
#     num1 = int(input("请输入一个整数："))
#     num2 = int(input("请输入另一个整数："))
#     result = num1 / num2
#     print("结果：", result)
#     print("未知异常代码：", unknown_code)
# except ValueError:
#     print("输入的不是整数")
# except ZeroDivisionError:
#     print("除数不能为0")
# except Exception as e:      # 捕获所有类型的异常
#     print("发生了未知异常：", e)
# finally:
#     print("无论是否发生异常，都会执行的代码")

# ---------- 抛出异常raise ---------
# -- 异常传递机制：当一个函数发生异常时，会将异常传递给调用该函数的函数，直到被捕获为止。
# -- 异常处理机制还可以使用 raise 语句手动抛出异常。
# -- raise 语句的基本语法：raise [异常类型]([异常信息])
# -- 异常类型是可选的，如果不指定异常类型，则表示抛出默认的异常类型。
# -- 异常信息是可选的，如果不指定异常信息，则表示使用默认的异常信息。
try:
    num1 = int(input("请输入一个整数："))
    num2 = int(input("请输入另一个整数："))
    if num2 == 0:
        raise ZeroDivisionError("除数不能为0")
    result = num1 / num2
    print("结果：", result)
except ValueError:
    print("输入的不是整数")
except ZeroDivisionError as e:
    print("发生了除数为0的异常：", e)

