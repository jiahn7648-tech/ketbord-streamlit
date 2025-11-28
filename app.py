import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Keyboard Demo", layout="centered")
st.title("⌨️ 키보드 반응 데모 (키보드 입력만 반응)")

html_code = """
<style>
.key {
    height: 40px;
    border: 2px solid #555;
    border-radius: 8px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    margin: 5px;
    font-size: 18px;
    font-weight: bold;
    transition: 0.15s;
    user-select: none;
    padding: 0 10px;
}

.key.small { width: 40px; }
.key.medium { width: 80px; }
.key.large { width: 200px; }

.key.active {
    background: yellow;
    transform: scale(1.15);
}
</style>

<div id="keyboard">

    <!-- 1줄 -->
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

    <!-- 2줄 -->
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

    <!-- 3줄 -->
    <div>
        <div class="key medium" id="SHIFT">Shift</div>
        <div class="key small" id="Z">Z</div>
        <div class="key small" id="X">X</div>
        <div class="key small" id="C">C</div>
        <div class="key small" id="V">V</div>
        <div class="key small" id="B">B</div>
        <div class="key small" id="N">N</div>
        <div class="key small" id="M">M</div>
        <div class="key medium" id="ENTER">Enter</div>
    </div>

    <!-- Spacebar -->
    <div>
        <div class="key large" id=" ">Space</div>
    </div>

</div>

<script>
// ✔ 키보드 입력만 반응
document.addEventListener("keydown", function(event) {
    let key = event.key;

    // Shift는 이름이 event.key = "Shift" 로 옴
    if (key === "Shift") key = "SHIFT";
    if (key === "Enter") key = "ENTER";
    if (key === " ") key = " ";

    let element = document.getElementById(key.toUpperCase()) 
                || document.getElementById(key);

    if (element) {
        element.classList.add("active");
        setTimeout(() => {
            element.classList.remove("active");
        }, 150);
    }
});
</script>
"""

components.html(html_code, height=450)
