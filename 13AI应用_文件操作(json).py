# ---------JSON文件操作---------
# JSON是软件开发中最常用的数据交换格式，而为了简化JSON数据的处理，在Python标准库中就提供了处理JSON数据的核心模块 json
# json模块中进行对象序列化和反序列化的函数分别是 json.dump() 和 json.load()
# json.dump() 函数用于将Python对象编码成JSON字符串并写入到文件对象中
# json.load() 函数用于从文件对象中读取JSON字符串并解码为Python对象

# 示例
import json

# 将Python对象写入JSON文件
# user = {
#     "name": "张三",
#     "age": 25,
#     "gender": "男",
#     "hobby": ["篮球", "足球", "羽毛球"]
# }
# with open("./res/user.json", "w", encoding="utf-8") as f:
#     json.dump(user, f, ensure_ascii=False, indent=4)
#     # ensure_ascii=False 表示不使用 ASCII 编码，在存储时保留中文字符
#     # indent=4 表示缩进为4个空格，便于阅读

# 从JSON文件读取Python对象
with open("./res/user.json", "r", encoding="utf-8") as f:
    user_data = json.load(f)
    print(user_data)
    print(type(user_data))