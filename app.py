import streamlit as st
import random
import streamlit.components.v1 as components

st.set_page_config(page_title="Keyboard Typing Game", layout="centered")
st.title("⌨️ 한 글자 타자 연습 (입력창 없음)")

# ---------------------------------------------------
# 랜덤 글자 생성
# ---------------------------------------------------
if "current_letter" not in st.session_state:
    st.session_state.current_letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

if "message" not in st.session_state:
    st.session_state.message = ""

# 화면에 제시된 글자 표시
st.markdown(
    f"<h1 style='font-size: 100px; text-align:center;'>{st.session_state.current_letter}</h1>",
    unsafe_allow_html=True
)

# 판정 메시지 표시
if st.session_state.message:
    st.write(st.session_state.message)


# ---------------------------------------------------
# HTML + JS : 키 입력 감지 → Streamlit으로 전송
# ---------------------------------------------------
html_code = f"""
<script>
// Streamlit으로 메시지 보내는 함수
function sendKeyToStreamlit(key) {{
    const data = {{"pressed_key": key}};
    window.parent.postMessage({{"isStreamlitMessage": true, "type": "streamlit:componentValue", "value": data}}, "*");
}}

// 키보드 입력 감지
document.addEventListener("keydown", function(event) {{
    let key = event.key.toUpperCase();

    // 가상 키보드 반응 처리
    let element = document.getElementById(key);
    if (element) {{
        element.classList.add("active");
        setTimeout(() => element.classList.remove("active"), 150);
    }}

    // Streamlit에게 key 전달
    sendKeyToStreamlit(key);
}});
</script>

<style>
.key {{
    height: 45px;
    border: 2px solid #444;
    border-radius: 6px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    margin: 4px;
    font-size: 18px;
    font-weight: bold;
    transition: 0.12s;
    user-select: none;
}}

.key.small {{ width: 45px; }}
.key.active {{
    background: yellow;
    transform: scale(1.13);
}}
</style>

<div id="keyboard">
    <div>
        <div class="key small" id="Q">Q</div>
        <div class="key small" id="W">W</div>
        <div class="key small" id="E">E</div>
        <div class="key small" id="R">R</div>
        <div class="key small" id="T">T</div>
        <div class="key small" id="Y">Y</div>
        <div class="key small" id="U">U</div>
        <div class="key small" id="I">I</div>
        <div class="key small" id="O">O</div>
        <div class="key small" id="P">P</div>
    </div>

    <div>
        <div class="key small" id="A">A</div>
        <div class="key small" id="S">S</div>
        <div class="key small" id="D">D</div>
        <div class="key small" id="F">F</div>
        <div class="key small" id="G">G</div>
        <div class="key small" id="H">H</div>
        <div class="key small" id="J">J</div>
        <div class="key small" id="K">K</div>
        <div class="key small" id="L">L</div>
    </div>

    <div>
        <div class="key small" id="Z">Z</div>
        <div class="key small" id="X">X</div>
        <div class="key small" id="C">C</div>
        <div class="key small" id="V">V</div>
        <div class="key small" id="B">B</div>
        <div class="key small" id="N">N</div>
        <div class="key small" id="M">M</div>
    </div>
</div>
"""

# JS에서 눌린 키 수신
pressed = components.html(html_code, height=400)


# ---------------------------------------------------
# Streamlit에서 키 판정
# ---------------------------------------------------
# pressed에 key 값이 들어옴
if isinstance(pressed, dict) and "pressed_key" in pressed:
    key = pressed["pressed_key"]

    if key == st.session_state.current_letter:
        st.session_state.message = "✅ 정답!"
        st.session_state.current_letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    else:
        st.session_state.message = f"❌ 오답! (입력: {key})"

    st.rerun()
