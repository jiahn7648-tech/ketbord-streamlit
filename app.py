import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Typing Game", layout="centered")

st.title("🔠 한 글자 타자 연습")

html_code = """
<style>
.keyboard {
    display: grid;
    grid-template-columns: repeat(10, 40px);
    gap: 8px;
    justify-content: center;
    margin-top: 20px;
}

.key {
    width: 40px;
    height: 40px;
    border: 2px solid #555;
    border-radius: 6px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 20px;
    user-select: none;
    background: #f0f0f0;
    transition: 0.1s;
}

.key.active {
    background: #4da3ff;
    color: white;
}

.key.flash {
    background: yellow !important;
}
.target {
    font-size: 40px;
    text-align: center;
    margin-top: 15px;
    font-weight: bold;
}
</style>

<div class="target" id="target">A</div>

<div class="keyboard">
    <!-- JS가 각 버튼 innerText를 알파벳으로 읽도록 구성 -->
    <div class="key">A</div><div class="key">B</div><div class="key">C</div>
    <div class="key">D</div><div class="key">E</div><div class="key">F</div>
    <div class="key">G</div><div class="key">H</div><div class="key">I</div>
    <div class="key">J</div><div class="key">K</div><div class="key">L</div>
    <div class="key">M</div><div class="key">N</div><div class="key">O</div>
    <div class="key">P</div><div class="key">Q</div><div class="key">R</div>
    <div class="key">S</div><div class="key">T</div><div class="key">U</div>
    <div class="key">V</div><div class="key">W</div><div class="key">X</div>
    <div class="key">Y</div><div class="key">Z</div>
</div>

<script>
let targetEl = document.getElementById("target");

// 다음 글자를 무작위로 생성
function getNextLetter() {
    const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    return letters[Math.floor(Math.random() * letters.length)];
}

document.addEventListener("keydown", function(event) {
    let key = event.key.toUpperCase();
    let keys = document.querySelectorAll(".key");

    keys.forEach(k => {
        if (k.innerText === key) {
            // 눌린 키 표시
            k.classList.add("active");
            setTimeout(() => k.classList.remove("active"), 150);

            // 정답 체크
            if (key === targetEl.innerText) {
                k.classList.add("flash");

                setTimeout(() => {
                    k.classList.remove("flash");
                    targetEl.innerText = getNextLetter();  // 다음 글자 넘김
                }, 120);
            }
        }
    });
});
</script>
"""

components.html(html_code, height=420)
