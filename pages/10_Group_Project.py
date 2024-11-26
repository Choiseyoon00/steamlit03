import streamlit as st
import folium
from streamlit_folium import st_folium
import openai
import json
from lib.tools import generate_image, SCHEMA_GENERATE_IMAGE
import tempfile

# 부경대 좌표와 지도에서 표시
pknu_latitude = 35.1329
pknu_longitude = 129.1038
center_coords = [pknu_latitude, pknu_longitude]
pknu = "Pukyong National University - Daeyeon Campus"

# 부경대학교 부지 경계선 좌표
pknu_boundary_coords = [
    [35.135406, 129.100878],  # 점 1
    [35.136015, 129.108573],  # 점 2
    [35.135002, 129.110104],  # 점 3
    [35.130434, 129.106197],  # 점 4
    [35.130731, 129.105941],  # 점 5
    [35.130585, 129.103985],  # 점 6
    [35.131797, 129.101350],  # 점 7
    [35.135406, 129.100878]   # 다시 시작점으로
]

# Folium 지도 생성
m = folium.Map(location=[pknu_latitude, pknu_longitude], zoom_start=15)

# Folium 지도 HTML로 저장하기
with tempfile.NamedTemporaryFile(suffix=".html", delete=False) as tmp_file:
    m.save(tmp_file.name)
    map_html_path = tmp_file.name


st.title("부동산 챗봇")


TOOL_FUNCTIONS = {
    "generate_image": generate_image
}

FUNCTION_TOOLS_SCHEMA = [
    SCHEMA_GENERATE_IMAGE
]

def show_message(msg):
    if msg['role'] == 'user' or msg['role'] == 'assistant':
        with st.chat_message(msg['role']):
            st.markdown(msg["content"])
    elif msg['role'] == 'code':
        with st.chat_message('assistant'):
            with st.expander("Show codes"):
                st.code(msg["content"], language='python')
    elif msg['role'] == 'image_url':
        with st.chat_message('assistant'):
            st.markdown(f"![]({msg['content']})")
    elif msg['role'] == 'image_file':
        with st.chat_message('assistant'):
            st.image(msg['content'])


# Initialization

client = st.session_state.get('openai_client', None)
if client is None:
    if st.button("API Key를 입력하세요."):
        st.switch_page("pages/1_Setting.py")
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "assistant" not in st.session_state:
    # 이제 HTML 경로를 `tool_resources`에 추가하여 전달
    st.session_state.assistant = client.beta.assistants.create(
        name="지도 전문가",
        instructions="당신은 지도를 통해 지도 내 장소를 파악하고 이를 편집하는 전문가 입니다.",
        model="gpt-4o-mini",
        tools=[{"type": "code_interpreter"}] + FUNCTION_TOOLS_SCHEMA,
        tool_resources={"map_html": map_html_path},
    )

if "thread" not in st.session_state:
    st.session_state.thread = client.beta.threads.create()


# Page

st.header("Chat")

col1, col2 = st.columns(2)
with col1:
    if st.button("Clear (Start a new chat)"):
        st.session_state.messages = []
        del st.session_state.thread
with col2:
    if st.button("Leave"):
        st.session_state.messages = []
        del st.session_state.thread
        del st.session_state.assistant

# previous chat
for msg in st.session_state.messages:
    show_message(msg)

# user prompt, assistant response
if prompt := st.chat_input("What is up?"):
    msg = {"role":"user", "content":prompt}
    show_message(msg)
    st.session_state.messages.append(msg)

    # assistant api - get response
    thread = st.session_state.thread
    assistant = st.session_state.assistant

    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=prompt
    )
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=assistant.id
    )

    while run.status == 'requires_action':
        tool_calls = run.required_action.submit_tool_outputs.tool_calls
        tool_outputs = []
        for tool in tool_calls:
            func_name = tool.function.name
            kwargs = json.loads(tool.function.arguments)
            output = None
            if func_name in TOOL_FUNCTIONS:
                output = TOOL_FUNCTIONS[func_name](**kwargs)
            tool_outputs.append(
                {
                    "tool_call_id": tool.id,
                    "output": str(output)
                }
            )
        run = client.beta.threads.runs.submit_tool_outputs_and_poll(
            thread_id=thread.id,
            run_id=run.id,
            tool_outputs=tool_outputs
        )
            
    # assistant messages - text, image_url, image_file
    if run.status == 'completed':
        api_response = client.beta.threads.messages.list(
            thread_id=thread.id,
            run_id=run.id,
            order="asc"
        )
        for data in api_response.data:
            for content in data.content:
                if content.type == 'text':
                    response = content.text.value
                    msg = {"role":"assistant","content":response}
                elif content.type == 'image_url':
                    url = content.image_url.url
                    msg = {"role":"image_url","content":url}
                elif content.type == 'image_file':
                    file_id = content.image_file.file_id
                    # load file
                    image_data = client.files.content(file_id)
                    msg = {"role":"image_file","content":image_data.read()}
                show_message(msg)
                st.session_state.messages.append(msg)

    # code interpreter tool call info
    run_steps = client.beta.threads.runs.steps.list(
        thread_id=thread.id,
        run_id=run.id,
        order='asc'
    )
    for run_step in run_steps.data:
        if run_step.step_details.type == 'tool_calls':
            for tool_call in run_step.step_details.tool_calls:
                if tool_call.type == 'code_interpreter':
                    code = tool_call.code_interpreter.input
                    msg = {"role":"code","content":code}
                    show_message(msg)
                    st.session_state.messages.append(msg)
