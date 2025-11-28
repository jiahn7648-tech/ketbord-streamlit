import streamlit as st
import streamlit.components.v1 as components
import random
import string

st.set_page_config(page_title="Keyboard Test", layout="centered")

# 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
if "current_char" not in st.session_state:
    st.session_state.current_char = random.choice(string.ascii_uppercase)
if "last_key" not in st.session_state:
    st.session_state.last_key = ""

st.title("🔵 키보드 반응 + 영어 타자 게임")

st.markdown(
    f"""
    <h1 style="font-size:80px; text-align:center; margin:10px;">
        {st.session_state.current_char}
    </h1>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------
# 네가 만든 키보드 + 파이썬으로 값 전달 기능 추가
# ---------------------------------------
html_code = f"""
<style>
.key {{
    width: 40px;
    height: 40px;
    border: 2px solid #555;
    border-radius: 8px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    margin: 5px;
    font-size: 18px;
    font-weight: bold;
    transition: 0.2s;
}}
.key.active {{
    background: yellow;
    transform: scale(1.2);
}}
</style>

<div id="keyboard">
    <div>
        <div class="key" id="Q">Q</div>
        <div class="key" id="W">W</div>
        <div class="key" id="E">E</div>
        <div class="key" id="R">R</div>
        <div class="key" id="T">T</div>
        <div class="key" id="Y">Y</div>
        <div class="key" id="U">U</div>
        <div class="key" id="I">I</div>
        <div class="key" id="O">O</div>
        <div class="key" id="P">P</div>
    </div>
    <div>
        <div class="key" id="A">A</div>
        <div class="key" id="S">S</div>
        <div class="key" id="D">D</div>
        <div class="key" id="F">F</div>
        <div class="key" id="G">G</div>
        <div class="key" id="H">H</div>
        <div class="key" id="J">J</div>
        <div class="key" id="K">K</div>
        <div class="key" id="L">L</div>
    </div>
    <div>
        <div class="key" id="Z">Z</div>
        <div class="key" id="X">X</div>
        <div class="key" id="C">C</div>
        <div class="key" id="V">V</div>
        <div class="key" id="B">B</div>
        <div class="key" id="N">N</div>
        <div class="key" id="M">M</div>
    </div>
</div>

<script>
// 키보드 반응
document.addEventListener("keydown", function(event) {{
    let key = event.key.toUpperCase();
    let element = document.getElementById(key);
    if (element) {{
        element.classList.add("active");
        setTimeout(() => {{
            element.classList.remove("active");
        }}, 150);
    }}

    // Python으로 key 보내기
    const msg = {{
        isStreamlitMessage: true,
        type: "streamlit:setComponentValue",
        value: key
    }};
    window.parent.postMessage(msg, "*");
}});
</script>
"""

pressed = components.html(html_code, height=350)

# ---------------------------------------
# Python에서 키 처리
# ---------------------------------------
if pressed:
    key = pressed.upper()
    st.session_state.last_key = key

    # 알파벳이면 점수 판정
    if len(key) == 1 and key in string.ascii_uppercase:
        if key == st.session_state.current_char:
            st.session_state.score += 1
        else:
            st.session_state.score -= 1

        # 다음 문제 생성
        st.session_state.current_char = random.choice(string.ascii_uppercase)

# 점수
st.markdown(
    f"""
    <h2 style="text-align:center; margin-top:20px;">
        점수: {st.session_state.score}
    </h2>
    """,
    unsafe_allow_html=True,
)
