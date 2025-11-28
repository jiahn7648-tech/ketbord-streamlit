import streamlit as st
import random
import streamlit.components.v1 as components

st.set_page_config(page_title="Typing Game", layout="centered")
st.title("⌨️ 한 글자 타자 연습")

# 랜덤 글자 상태
if "current_letter" not in st.session_state:
    st.session_state.current_letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

if "flash" not in st.session_state:
    st.session_state.flash = False


# -----------------------------
# 글자 표시 (정답 시 반짝)
# -----------------------------
flash_class = "flash" if st.session_state.flash else ""

st.markdown(
    f"""
    <style>
    .letter {{
        font-size: 100px;
        text-align: center;
        transition: 0.1s;
    }}

    .flash {{
        background: yellow;
        border-radius: 12px;
    }}
    </style>

    <div class="letter {flash_class}">
        {st.session_state.current_letter}
    </div>
    """,
    unsafe_allow_html=True
)

# 🔻 반짝 효과는 1회성으로 사용 후 바로 끄기
if st.session_state.flash:
    st.session_state.flash = False


# -----------------------------
# JS + HTML (키 감지 → Streamlit 전달)
# -----------------------------
html_code = """
<script>
// Streamlit으로 key 보내기
function sendKeyToStreamlit(key) {
    const data = { pressed_key: key };
    window.parent.postMessage(
        {isStreamlitMessage: true, type: "streamlit:componentValue", value: data},
        "*"
    );
}

// 키보드 감지
document.addEventListener("keydown", function(event) {
    let key = event.key.toUpperCase();

    // 가상키보드 반응
    let el = document.getElementById(key);
    if (el) {
        el.classList.add("active");
        setTimeout(() => el.classList.remove("active"), 150);
    }

    // Streamlit 전달
    sendKeyToStreamlit(key);
});
</script>

<style>
.key {
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
}
.key.small { width: 45px; }

.key.active {
    background: yellow;
    transform: scale(1.15);
}
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

pressed = components.html(html_code, height=350)


# -----------------------------
# Python에서 키 처리
# -----------------------------
if isinstance(pressed, dict) and "pressed_key" in pressed:
    key = pressed["pressed_key"]

    if key == st.session_state.current_letter:
        st.session_state.flash = True
        st.session_state.current_letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    else:
        pass  # 틀리면 아무 변화 없음

    st.rerun()
