import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Typing Game", layout="centered")

st.title("⌨️ 한 글자 타자 연습 (QWERTY 버전)")

html_code = """
<style>
body {
    font-family: 'Segoe UI', sans-serif;
}

.game-wrapper {
    text-align: center;
    margin-top: 10px;
}

.target {
    font-size: 60px;
    font-weight: 900;
    margin-top: 10px;
    margin-bottom: 25px;
    color: #333;
    transition: 0.15s;
}

/* 정답/오답 반짝 효과 */
.target.flash-correct {
    color: #ffe34d !important;
    transform: scale(1.15);
}

.target.flash-wrong {
    color: #ff4d4d !important;
    transform: scale(1.15);
}

/* 키보드 전체 묶음 */
.keyboard {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
}

/* 한 줄 */
.key-row {
    display: flex;
    justify-content: center;
    gap: 8px;
}

/* 키 디자인 */
.key {
    width: 50px;
    height: 50px;
    background: #f3f3f3;
    border-radius: 8px;
    border: 1px solid #ccc;
    font-size: 20px;
    font-weight: 600;
    display: flex;
    justify-content: center;
    align-items: center;
    transition: 0.1s;
    box-shadow: 0 2px 4px rgba(0,0,0,0.15);
    user-select: none;
}

.key.active {
    background: #4da3ff;
    color: white;
    transform: scale(1.05);
}
</style>

<div class="game-wrapper">
    <div class="target" id="target">A</div>

    <div class="keyboard">
        <div class="key-row">
            <div class="key">Q</div><div class="key">W</div><div class="key">E</div><div class="key">R</div>
            <div class="key">T</div><div class="key">Y</div><div class="key">U</div><div class="key">I</div>
            <div class="key">O</div><div class="key">P</div>
        </div>

        <div class="key-row">
            <div class="key">A</div><div class="key">S</div><div class="key">D</div><div class="key">F</div>
            <div class="key">G</div><div class="key">H</div><div class="key">J</div><div class="key">K</div>
            <div class="key">L</div>
        </div>

        <div class="key-row">
            <div class="key">Z</div><div class="key">X</div><div class="key">C</div><div class="key">V</div>
            <div class="key">B</div><div class="key">N</div><div class="key">M</div>
        </div>
    </div>
</div>

<script>
let targetEl = document.getElementById("target");

function getNextLetter() {
    const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    return letters[Math.floor(Math.random() * letters.length)];
}

document.addEventListener("keydown", function(event) {
    let key = event.key.toUpperCase();
    let keys = document.querySelectorAll(".key");

    // 가상 키보드 반응
    keys.forEach(k => {
        if (k.innerText === key) {
            k.classList.add("active");
            setTimeout(() => k.classList.remove("active"), 130);
        }
    });

    // 정답 여부 판단
    if (key === targetEl.innerText) {
        // 정답 → 노란색 반짝
        targetEl.classList.add("flash-correct");

        setTimeout(() => {
            targetEl.classList.remove("flash-correct");
            targetEl.innerText = getNextLetter();  // 다음 글자로 변경
        }, 150);

    } else {
        // 오답 → 빨간색 반짝
        targetEl.classList.add("flash-wrong");

        setTimeout(() => {
            targetEl.classList.remove("flash-wrong");
        }, 150);
    }
});
</script>
"""

components.html(html_code, height=550)
