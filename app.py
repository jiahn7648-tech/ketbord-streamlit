import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Keyboard Demo", layout="centered")

st.title("🔵 키보드 반응 데모")
st.write("키보드를 누르면 아래 가상 키보드가 반응합니다!")

# HTML + CSS + JS 삽입
html_code = """
<style>
.key {
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
}
.key.active {
    background: yellow;
    transform: scale(1.2);
}
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
document.addEventListener("keydown", function(event) {
    let key = event.key.toUpperCase();
    let element = document.getElementById(key);
    if (element) {
        element.classList.add("active");
        setTimeout(() => {
            element.classList.remove("active");
        }, 150);
    }
});
</script>
"""

components.html(html_code, height=300)
