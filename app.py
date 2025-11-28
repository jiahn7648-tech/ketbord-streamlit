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

st.title("🎮 영어 타자 연습 (작동 완벽 버전)")

# 현재 문제
st.markdown(
    f"""
    <div style="font-size:80px; text-align:center; font-weight:bold; margin:20px;">
        {st.session_state.current_char.upper()}
    </div>
    """,
    unsafe_allow_html=True,
)

# 자바스크립트로 키보드 이벤트 받기
key = st.experimental_js(
    """
    () => {
        let pressed = "";
        document.onkeydown = (e) => {
            pressed = e.key;
            window.streamlitAPI.setComponentValue(pressed);
        };
        return pressed;
    }
"""
)

# 키 입력 처리
if key:
    last = key.lower()

    # 스페이스 처리
    if last == " ":
        last = "space"

    # 쉬프트
    if last == "shift":
        last = "shift"

    st.session_state.last_key = last

    # 정답 체크
    if last == st.session_state.current_char:
        st.session_state.score += 1
    elif len(last) == 1 and last in string.ascii_lowercase:
        st.session_state.score -= 1

    # 다음 문제
    st.session_state.current_char = random.choice(string.ascii_lowercase)

# 점수 표시
st.markdown(
    f"""
    <div style="font-size:30px; font-weight:bold; text-align:center; margin-top:20px;">
        점수 : {st.session_state.score}
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("---")
st.subheader("가상 키보드 (키 반응 표시)")

# 키보드 레이아웃
keyboard_rows = [
    list("qwertyuiop"),
    list("asdfghjkl"),
    list("zxcvbnm")
]

# 키 스타일
def key_style(key):
    if st.session_state.last_key == key:
        return "background:#ffd54f;"
    return "background:#eee;"

# 화면에 키보드 출력
for row in keyboard_rows:
    cols = st.columns(len(row))
    for i, k in enumerate(row):
        with cols[i]:
            st.markdown(
                f"""
                <div style="
                    border:1px solid #999;
                    width:40px;
                    padding:10px;
                    margin:4px;
                    text-align:center;
                    border-radius:5px;
                    {key_style(k)}
                ">
                    {k.upper()}
                </div>
                """,
                unsafe_allow_html=True
            )

# 스페이스 / 엔터 / 쉬프트
cols = st.columns(3)
special_keys = ["space", "enter", "shift"]
labels = ["SPACE", "ENTER", "SHIFT"]

for i, k in enumerate(special_keys):
    bg = "#ffd54f" if st.session_state.last_key == k else "#eee"
    width = "200px" if k == "space" else "80px"

    with cols[i]:
        st.markdown(
            f"""
            <div style="
                border:1px solid #999;
                width:{width};
                padding:10px;
                margin:4px;
                text-align:center;
                border-radius:5px;
                background:{bg};
            ">
                {labels[i]}
            </div>
            """,
            unsafe_allow_html=True
        )
