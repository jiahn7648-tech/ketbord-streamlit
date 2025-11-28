import streamlit as st
import random
import streamlit.components.v1 as components

st.set_page_config(page_title="Typing Practice + Virtual Keyboard", layout="centered")
st.title("⌨️ 알파벳 한 글자 타자 연습")

st.write("화면에 나오는 영어 알파벳 한 글자를 입력하세요!")

# -------------------------
# 랜덤 알파벳 1글자 생성
# -------------------------
if "current_letter" not in st.session_state:
    st.session_state.current_letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

st.write("## 🔠 현재 글자:")
st.markdown(
    f"<h1 style='font-size: 90px; text-align:center;'>{st.session_state.current_letter}</h1>",
    unsafe_allow_html=True
)

# -------------------------
# 입력창
# -------------------------
typed = st.text_input("여기에 입력하세요 (1글자)", max_chars=1)

if typed:
    if typed.upper() == st.session_state.current_letter:
        st.success("정답! 다음 글자로 넘어갑니다.")
        st.session_state.current_letter = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    else:
        st.error("❌ 오답입니다. 다시 시도하세요!")

# -------------------------
# 가상 키보드
# -------------------------
html_code = """
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
    user-select: none;
}

.key.small { width: 45px; }
.key.medium { width: 70px; }
.key.large { width: 250px; }
.key.enter { width: 90px; }
.key.shift { width: 100px; }

.key.active {
    background: yellow;
    transform: scale(1.13);
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
        <div class="key shift" id="SHIFT">Shift</div>
        <div class="key small" id="Z">Z</div>
        <div class="key small" id="X">X</div>
        <div class="key small" id="C">C</div>
        <div class="key small" id="V">V</div>
        <div class="key small" id="B">B</div>
        <div class="key small" id="N">N</div>
        <div class="key small" id="M">M</div>
        <div class="key enter" id="ENTER">Enter</div>
    </div>

    <div style="text-align:center;">
        <div class="key large" id=" ">Space</div>
    </div>

</div>

<script>
document.addEventListener("keydown", function(event) {
    let key = event.key;

    if (key === "Shift") key = "SHIFT";
    if (key === "Enter") key = "ENTER";
    if (key === " ") key = " ";

    let element =
        document.getElementById(key.toUpperCase()) ||
        document.getElementById(key);

    if (element) {
        element.classList.add("active");
        setTimeout(() => {
            element.classList.remove("active");
        }, 150);
    }
});
</script>
"""

components.html(html_code, height=500)

