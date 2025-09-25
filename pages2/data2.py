import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import random

# NanumGothic 폰트 경로 지정
font_path = '/workspaces/25.09.25../fonts/NanumGothic-Regular.ttf'
fontprop = fm.FontProperties(fname=font_path)
plt.rc('font', family=fontprop.get_name())

st.title('함수 그래프 퀴즈')

quiz_funcs = [
    ('sin(x)', lambda x: np.sin(x)),
    ('cos(x)', lambda x: np.cos(x)),
    ('x**2', lambda x: x**2),
    ('exp(x)', lambda x: np.exp(x)),
    ('log(x+2)', lambda x: np.log(x+2)),
    ('abs(x)', lambda x: np.abs(x)),
    ('tanh(x)', lambda x: np.tanh(x)),
    ('1/(x+1)', lambda x: 1/(x+1)),
]

if 'quiz_started' not in st.session_state:
    st.session_state['quiz_started'] = False
if 'quiz_answer' not in st.session_state:
    st.session_state['quiz_answer'] = None
if 'quiz_choices' not in st.session_state:
    st.session_state['quiz_choices'] = []

if st.button('퀴즈 시작'):
    st.session_state['quiz_started'] = True
    # 정답 함수 선택
    answer_idx = random.randint(0, len(quiz_funcs)-1)
    answer_func = quiz_funcs[answer_idx]
    # 오답 함수 3개 선택 (중복 없이)
    wrong_funcs = random.sample([f for i, f in enumerate(quiz_funcs) if i != answer_idx], 3)
    # 섞기
    all_choices = wrong_funcs + [answer_func]
    random.shuffle(all_choices)
    st.session_state['quiz_answer'] = answer_func[0]
    st.session_state['quiz_choices'] = all_choices

if st.session_state['quiz_started']:
    st.subheader('아래 함수식에 맞는 그래프를 고르세요:')
    st.markdown(f"**f(x) = {st.session_state['quiz_answer']}**")
    x = np.linspace(-5, 5, 300)
    cols = st.columns(4)
    for i, (func_str, func) in enumerate(st.session_state['quiz_choices']):
        fig, ax = plt.subplots()
        try:
            y = func(x)
            ax.plot(x, y)
            ax.axhline(0, color='gray', linewidth=1)
            ax.axvline(0, color='gray', linewidth=1)
            ax.set_xlabel('x', fontproperties=fontprop)
            ax.set_ylabel('f(x)', fontproperties=fontprop)
            ax.set_title(f'그래프 {i+1}', fontproperties=fontprop)
        except Exception:
            ax.text(0.5, 0.5, '그래프 오류', ha='center', va='center')
        cols[i].pyplot(fig)
    selected = st.radio('정답 그래프를 선택하세요', options=[f'그래프 {i+1}' for i in range(4)])
    if st.button('정답 확인'):
        answer_idx = [i for i, (fs, _) in enumerate(st.session_state['quiz_choices']) if fs == st.session_state['quiz_answer']][0]
        if selected == f'그래프 {answer_idx+1}':
            st.success('정답입니다!')
        else:
            st.error(f'오답입니다. 정답은 그래프 {answer_idx+1} 입니다.')
