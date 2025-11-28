import streamlit as st
import streamlit.components.v1 as components
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

st.title("🎮 영어 타자 연습 (작동 안정화 버전)")
st.write("화면을 클릭한 뒤 키보드를 누르세요. (브라우저 포커스 필요)")

# 표시되는 큰 문자
st.markdown(
    f"""
    <div style="font-size:100px; text-align:center; font-weight:bold; margin:20px;">
        {st.session_state.current_char.upper()}
    </div>
    """,
    unsafe_allow_html=True,
)

# -------------------------
# JS로 키 이벤트를 잡아 Python으로 전달하는 invisible component
# -------------------------
# components.html은 window.parent.postMessage로 'streamlit:setComponentValue' 타입의 메시지를 보내면
# 그 값을 반환값으로 Python에서 받을 수 있음.
js_code = """
<div></div>
<script>
  // 브라우저에서 키를 누르면 부모 Streamlit 앱으로 전달
  document.addEventListener("keydown", function(e) {
    // e.key 값을 그대로 보냄
    const k = e.key;
    const msg = {
      isStreamlitMessage: true,
      type: "streamlit:setComponentValue",
      value: k
    };
    window.parent.postMessage(msg, "*");
  });
</script>
"""

# 이 호출은 사용자가 키를 누를 때마다 해당 키 값을 반환(return)함
pressed = components.html(js_code, height=0)  # 보이지 않게 높이 0

# -------------------------
# 키 처리 로직
# -------------------------
if pressed:
    key = pressed  # raw key string from JS, 예: "a", "Shift", " "
    key_lower = key.lower()

    # normalize for space/shift/enter
    if key == " ":
        key_norm = "space"
    elif key_lower == "shift":
        key_norm = "shift"
    elif key_lower == "enter":
        key_norm = "enter"
    else:
        key_norm = key_lower

    st.session_state.last_key = key_norm

    # 알파벳 정답 처리: 한 글자 문제이므로 소문자 알파벳만 정답/오답 판정
    if len(key_norm) == 1 and key_norm in string.ascii_lowercase:
        if key_norm == st.session_state.current_char:
            st.session_state.score += 1
        else:
            st.session_state.score -= 1

        # 다음 문제로 바로 교체
        st.session_state.current_char = random.choice(string.ascii_lowercase)

    # 스페이스/엔터/쉬프트는 점수 변동 없이 다음 문제로 넘어가지 않음(원하면 변경 가능)

# -------------------------
# 점수 표시
# -------------------------
st.markdown(
    f"""
    <div style="font-size:28px; font-weight:bold; text-align:center; margin-top:10px;">
        점수: {st.session_state.score}
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("---")
st.subheader("가상 키보드 (키보드 입력만 반응)")

# 키보드 레이아웃 (실제 배치에 가깝게)
keyboard_rows = [
    list("qwertyuiop"),
    list("asdfghjkl"),
    list("zxcvbnm")
]

def key_bg(k):
    # highlight 조건 (space/enter/shift 별명 처리)
    if st.session_state.last_key == k:
        return "#ffd54f"
    if st.session_state.last_key == "space" and k == " ":
        return "#ffd54f"
    if st.session_state.last_key == "enter" and k.lower() == "enter":
        return "#ffd54f"
    if st.session_state.last_key == "shift" and k.lower() == "shift":
        return "#ffd54f"
    return "#eeeeee"

# 출력: 문자 키들
for row in keyboard_rows:
    cols = st.columns(len(row))
    for i, ch in enumerate(row):
        with cols[i]:
            st.markdown(
                f"""
                <div style="
                    border:1px solid #999;
                    width:46px;
                    padding:10px;
                    margin:4px;
                    text-align:center;
                    border-radius:6px;
                    background:{key_bg(ch)};
                    font-weight:700;
                ">
                    {ch.upper()}
                </div>
                """,
                unsafe_allow_html=True
            )

# 특수키 줄 (Shift, Enter, Space)
cols = st.columns([1,1,4])
with cols[0]:
    st.markdown(
        f"""
        <div style="
            border:1px solid #999;
            width:100%;
            padding:10px;
            margin:4px;
            text-align:center;
            border-radius:6px;
            background:{key_bg('shift')};
            font-weight:700;
        ">
            SHIFT
        </div>
        """,
        unsafe_allow_html=True
    )
with cols[1]:
    st.markdown(
        f"""
        <div style="
            border:1px solid #999;
            width:100%;
            padding:10px;
            margin:4px;
            text-align:center;
            border-radius:6px;
            background:{key_bg('enter')};
            font-weight:700;
        ">
            ENTER
        </div>
        """,
        unsafe_allow_html=True
    )
with cols[2]:
    st.markdown(
        f"""
        <div style="
            border:1px solid #999;
            width:100%;
            padding:12px;
            margin:4px;
            text-align:center;
            border-radius:6px;
            background:{key_bg('space')};
            font-weight:700;
        ">
            SPACE
        </div>
        """,
        unsafe_allow_html=True
    )
