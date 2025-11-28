import streamlit as st
import random
import string

st.set_page_config(page_title="영어 타자 연습", layout="centered")

# 세션 상태 초기화
if "score" not in st.session_state:
    st.session_state.score = 0
if "current_char" not in st.session_state:
    st.session_state.current_char = random.choice(string.ascii_lowercase)
if "last_key" not in st.session_state:
    st.session_state.last_key = None

st.title("🎮 영어 타자 연습 (한컴타자 미니)")
st.write("아래에 보이는 영어 한 글자를 키보드로 입력하세요!")

# 현재 문제 표시
st.markdown(
    f"""
    <div style="font-size:80px; text-align:center; font-weight:bold; margin:20px;">
        {st.session_state.current_char.upper()}
    </div>
    """,
    unsafe_allow_html=True,
)

# 맞았는지 처리 함수
def check_key(key):
    if key == st.session_state.current_char:
        st.session_state.score += 1
    else:
        st.session_state.score -= 1

    st.session_state.current_char = random.choice(string.ascii_lowercase)
    st.session_state.last_key = key

# 키 입력 받기
key = st.text_input("입력하세요 (화면에 표시 안됨)", label_visibility="collapsed")
if key:
    check_key(key[-1].lower())  # 마지막 글자만 받음

# 점수 표시
st.markdown(
    f"""
    <div style="font-size:30px; font-weight:bold; text-align:center; margin-top:20px;">
        점수 : {st.session_state.score}
    </div>
    """,
    unsafe_allow_html=True,
)

# 가상 키보드 레이아웃
keyboard_rows = [
    list("qwertyuiop"),
    list("asdfghjkl"),
    list("zxcvbnm"),
]

special_keys = ["SPACE", "ENTER", "SHIFT"]

st.write("---")
st.subheader("가상 키보드 (누른 키 표시)")

# 키보드 스타일 함수
def key_style(key):
    if st.session_state.last_key == key.lower():
        return "background-color:#ffd54f; font-weight:bold;"
    return "background-color:#eeeeee;"

# 실제 키보드 UI 표시
for row in keyboard_rows:
    cols = st.columns(len(row))
    for i, k in enumerate(row):
        with cols[i]:
            st.markdown(
                f"""
                <div style="border:1px solid #999;
                            border-radius:6px;
                            padding:10px;
                            margin:2px;
                            text-align:center;
                            width:40px;
                            {key_style(k)}">
                    {k.upper()}
                </div>
                """,
                unsafe_allow_html=True,
            )

# 특수키
cols = st.columns(len(special_keys))
for i, k in enumerate(special_keys):
    display = k
    if k == "SPACE":
        width = "200px"
    else:
        width = "80px"

    match_key = {
        "SPACE": " ",
        "ENTER": "\r",
        "SHIFT": "shift"
    }

    highlight = False
    if st.session_state.last_key == " " and k == "SPACE":
        highlight = True
    if st.session_state.last_key == "shift" and k == "SHIFT":
        highlight = True

    bg = "#ffd54f" if highlight else "#eeeeee"

    with cols[i]:
        st.markdown(
            f"""
            <div style="border:1px solid #999;
                        border-radius:6px;
                        padding:10px;
                        margin:2px;
                        text-align:center;
                        width:{width};
                        background-color:{bg};">
                {display}
            </div>
            """,
            unsafe_allow_html=True,
        )
