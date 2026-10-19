import streamlit as st
from openai import OpenAI
import os

api_key = os.environ.get("DEEPSEEK_API_KEY")
system_content = """
    你叫%s，现在是用户的真实伴侣，请完全代入伴侣角色。
    规则：
        1、每次只回复一条消息。
        2、禁止任何场景或状态描述性文字。
        3、匹配用户的语言。
        4、回复简短，像微信聊天一样。
        5、有需要的话可以使用emoji表情。
        6、用符合伴侣性格的方式对话。
        7、回复的内容，要充分体现伴侣的性格特征。
    伴侣性格：
        %s
    你必须严格遵守上述的规则来回复用户。
"""

# 初始化内存变量
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat_name" not in st.session_state:
    st.session_state.chat_name = "小团团"
if "chat_personality" not in st.session_state:
    st.session_state.chat_personality = "活泼可爱的台湾姑娘"

# for backward compatibility, you can still use `https://api.deepseek.com/v1` as `base_url`.
client = OpenAI(
    api_key=api_key, 
    base_url="https://api.deepseek.com",
    timeout=60
)

st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🧸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 设置页面标题和描述
st.logo("🧸", size="large")
st.title("AI智能伴侣")
st.write("欢迎使用AI智能伴侣，这是一个可以与您进行自然语言交流的AI助手。")

# 设置侧边栏
with st.sidebar:
    st.subheader("AI控制面板")
    st.button("新建会话")
    st.write("历史会话")
    st.subheader("伴侣信息")
    chat_name = st.text_input("昵称", placeholder="请输入伴侣昵称", value=st.session_state.chat_name)
    chat_personality = st.text_area("性格", placeholder="请输入伴侣性格", value=st.session_state.chat_personality)

# 更新伴侣信息
if chat_name:
    st.session_state.chat_name = chat_name
if chat_personality:
    st.session_state.chat_personality = chat_personality

# 遍历历史聊天记录并显示
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

# 聊天输入
prompt = st.chat_input("请输入您的聊天内容")
# 聊天输出
if prompt:
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})   # 将用户输入添加到聊天记录中

    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=[
            {
                "role": "system",
                "content": system_content % (st.session_state.chat_name, st.session_state.chat_personality),
            },
            *st.session_state.messages,        # 将历史聊天记录解包添加到消息中（上面已经将本次用户输入添加到聊天记录中）
        ],
        max_tokens=1024,    # 生成文本的最大长度
        temperature=0.7,    # 生成文本的随机性，值越大越随机
        stream=True,        # 流式输出
    )
    # 非流式输出的数据结构（response.choices[0].message.content）
    # st.chat_message("assistant").write(response.choices[0].message.content)
    # st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})   # 将AI助手的回复添加到聊天记录中
    # 流式输出的数据结构（response -> chunk.choices[0].delta.content）
    message_placeholder = st.empty() # 创建一个空组件，用于显示AI助手的流式回复
    full_content = ""
    for chunk in response:
        if chunk.choices and len(chunk.choices) > 0:
            content = chunk.choices[0].delta.content
            if content:
                full_content += content
                message_placeholder.chat_message("assistant").write(full_content)
    st.session_state.messages.append({"role": "assistant", "content": full_content})   # 将AI助手的回复添加到聊天记录中
