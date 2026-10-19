#  ---------读文件---------
# 1、打开文件
# 2、读取文件内容
# 3、关闭文件
f = open("./res/望庐山瀑布.txt", "r", encoding="utf-8")

# read() 读取文件全部内容
# content = f.read()
# print(content)

# readlines() 读取文件的每一行，返回一个列表
contents = f.readlines()
for content in contents:
    print(content.strip())    # strip() 去掉字符串两端的空格和换行符

f.close()               # 关闭文件，注意：文件操作完成后一定要关闭文件，不关闭文件会一直占用资源

#  ---------写文件---------
# 写文件，若文件不存在则创建，若文件存在则覆盖
f = open("./res/静夜思.txt", "w", encoding="utf-8")

f.write("静夜思（李白）\n\n")
f.write("床前明月光\n")
f.write("疑是地上霜\n")
f.write("举头望明月\n")
f.write("低头思故乡\n")

f.close()