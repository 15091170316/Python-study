#  ---------读文件---------
# 1、打开文件
# 2、读取文件内容
# 3、关闭文件
# 使用 try-finally 确保操作文件出错时也能关闭文件（但有点繁琐，项目中推荐使用如下的 with 语句）
f = open("./res/望庐山瀑布.txt", "r", encoding="utf-8")

try:
    # read() 读取文件全部内容
    # content = f.read()
    # print(content)

    # readlines() 读取文件的每一行，返回一个列表
    contents = f.readlines()
    for content in contents:
        print(content.strip())    # strip() 去掉字符串两端的空格和换行符

finally:
    f.close()               # 关闭文件，注意：文件操作完成后一定要关闭文件，不关闭文件会一直占用资源

#  ---------写文件---------
# 写文件，若文件不存在则创建，若文件存在则覆盖
f = open("./res/静夜思.txt", "w", encoding="utf-8")

try:
    f.write("静夜思（李白）\n\n")
    f.write("床前明月光\n")
    f.write("疑是地上霜\n")
    f.write("举头望明月\n")
    f.write("低头思故乡\n")

finally:
    f.close()

#  ---------with语句（安全释放资源文件）---------
# with语句（上下文管理器）的核心作用就是确保资源总是被正确获取和释放（即使发生异常也会释放资源），也是项目开发中的推荐做法
with open("./res/静夜思.txt", "r", encoding="utf-8") as f:
    contents = f.read()
    print(contents.strip())    # strip() 去掉字符串两端的空格和换行符