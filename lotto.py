import random
import streamlit as st

st.title("🍀 로또 번호 생성기")
st.markdown("버튼을 누를 때마다 최대 5개까지 로또 번호 세트가 누적됩니다.")

# 세션 상태에 생성된 번호 리스트 초기화
if "lotto_sets" not in st.session_state:
  st.session_state.lotto_sets = []


# 번호별 색상 설정 (배경색, 글자색)
def get_ball_style(num):
  if num <= 10:
    bg, fg = "#fbc400", "black"
  elif num <= 20:
    bg, fg = "#69c8ff", "black"
  elif num <= 30:
    bg, fg = "#ff7272", "white"
  elif num <= 40:
    bg, fg = "#aaaaaa", "white"
  else:
    bg, fg = "#b0d840", "black"
  return bg, fg


# 생성 버튼
if st.button("로또번호 생성"):
  new_numbers = sorted(random.sample(range(1, 46), 6))
  st.session_state.lotto_sets.append(new_numbers)
  if len(st.session_state.lotto_sets) > 5:
    st.session_state.lotto_sets.pop(0)

# 초기화 버튼
if st.button("초기화"):
  st.session_state.lotto_sets = []
  st.rerun()

# 저장된 로또 번호 세트 화면에 출력
if st.session_state.lotto_sets:
  st.write("---")
  for idx, lotto_set in enumerate(st.session_state.lotto_sets):
    cols = st.columns([1, 6])
    with cols[0]:
      st.markdown(f"**#{idx+1} 세트**")
    with cols[1]:
      # HTML 태그 오류를 방지하기 위해 st.html 활용
      html_content = (
          '<div style="display: flex; gap: 6px; align-items: center;">'
      )
      for num in lotto_set:
        bg, fg = get_ball_style(num)
        html_content += f"""
                <div style="
                    width: 36px;
                    height: 36px;
                    border-radius: 50%;
                    background-color: {bg};
                    color: {fg};
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-weight: bold;
                    font-size: 14px;
                    box-shadow: inset -2px -2px 4px rgba(0,0,0,0.3);
                ">{num:02d}</div>
                """
      html_content += "</div>"
      st.html(html_content)