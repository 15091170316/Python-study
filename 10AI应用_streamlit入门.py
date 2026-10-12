# ---------- streamlit入门 ----------
# streamlit是一个开源的Python库，可以让你轻松地创建和分享美观的Web应用程序，主要用于数据科学和机器学习项目。它允许你使用简单的Python代码来构建交互式的用户界面，而无需深入了解前端开发。
# streamlit的主要特点：
# 1. 简单易用：只需几行代码即可创建一个Web应用程序。
# 2. 实时更新：当你修改代码时，应用程序会自动更新，无需手动刷新。
# 3. 丰富的组件：提供了多种交互式组件，如按钮、滑块、文本输入框等，方便用户与应用程序进行交互。
# 4. 数据可视化：支持多种数据可视化库，如Matplotlib、Plotly、Altair等，可以轻松地将数据可视化
# 5. 部署方便：可以将应用程序部署到云端，方便与他人分享和访问。
# streamlit的使用步骤：
# 1. 安装streamlit：使用pip安装streamlit库，命令为：pip install streamlit
# 2. 创建Python脚本：创建一个Python脚本文件（如app.py），并在其中编写streamlit代码。
# 3. 在Python脚本中导入streamlit库：import streamlit as st
# 4. 基于streamlit文档中提供的Api来构建Web应用程序，如st.title()、st.write()、st.button()等。
# 5. 运行应用程序：在终端中运行命令：streamlit run app.py，启动应用程序。
# 6. 访问应用程序：在浏览器中打开http://localhost:8501，即可访问应用程序。
# streamlit的示例代码：
import streamlit as st

# 页面标题
st.title("Hello, Streamlit!")
st.header("这是一个Streamlit示例应用程序，一级标题")
st.subheader("这是一个Streamlit示例应用程序，二级标题")

# 文本（段落）
st.write("Streamlit是一个开源的Python库，可以让你轻松地创建和分享美观的Web应用程序。")

# 图片
st.image("https://www.streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", caption="Streamlit Logo")
st.logo("https://www.streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", size="large")

# 表格
student_data = {
    "姓名": ["张三", "李四", "王五"],
    "年龄": [18, 19, 20],
    "成绩": [90, 85, 95],
    "爱好": ["篮球、足球", "游泳、跑步", "乒乓球、羽毛球"],
}
st.table(student_data)

# 输入框
username = st.text_input("请输入你的用户名：")
password = st.text_input("请输入你的密码：", type="password")
st.write(f"你输入的用户名是：{username}，密码是：{password}")

# 单选按钮
gender = st.radio("请选择你的性别：", ["男", "女", "未知"])
st.write(f"你选择的性别是：{gender}")

# 页面配置
st.set_page_config(
    page_title="Streamlit示例应用程序",       # 页面标题
    page_icon="🍄",                         # 页面图标
    layout="centered",                      # 页面布局（wide、centered）wide表示宽屏布局，centered表示居中布局，默认为centered
    initial_sidebar_state="expanded",       # 侧边栏初始状态（expanded、collapsed）expanded表示展开，collapsed表示折叠，默认为expanded
)