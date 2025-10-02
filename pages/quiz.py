import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import random

# NanumGothic 폰트 경로 지정
font_path = '/workspaces/25.09.25../fonts/NanumGothic-Regular.ttf'
fontprop = fm.FontProperties(fname=font_path)
plt.rc('font', family=fontprop.get_name())



st.markdown(
    '''
    <style>
    .quiz-card {
        background: white;
        border-radius: 18px;
        box-shadow: 0 4px 16px rgba(44,108,223,0.08);
        padding: 2.5rem 2rem 2rem 2rem;
        margin: 2rem auto 1.5rem auto;
        max-width: 650px;
    }
    .quiz-title {
        text-align: center;
        color: #2d6cdf;
        font-size: 2em;
        font-weight: bold;
        margin-bottom: 0.5em;
    }
    .quiz-emoji {
        font-size: 2.2em;
        text-align: center;
        margin-bottom: 0.5em;
    }
    .quiz-desc {
        text-align: center;
        font-size: 1.1em;
        color: #444;
        margin-bottom: 1.5em;
    }
    .quiz-btn-wrap {
        text-align: center;
        margin-bottom: 1em;
    }
    </style>
    <div class="quiz-card">
        <div class="quiz-emoji">🧩📊</div>
        <div class="quiz-title">함수 그래프 퀴즈</div>
        <div class="quiz-desc">함수식에 맞는 그래프를 골라보세요!<br>직관력과 관찰력을 키워봐요.</div>
        <div class="quiz-btn-wrap" id="quiz-btn-wrap"></div>
        <hr style="border:1px solid #eaeaea; margin:2em 0;">
    </div>
    ''', unsafe_allow_html=True)

# 퀴즈 시작 버튼을 카드 안에 표시
quiz_start = st.button('퀴즈 시작', key='quiz_start_btn')

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



# 문제 수 관리 및 중복 방지
MAX_QUIZ = 10
if 'quiz_started' not in st.session_state:
    st.session_state['quiz_started'] = False
if 'quiz_answer' not in st.session_state:
    st.session_state['quiz_answer'] = None
if 'quiz_choices' not in st.session_state:
    st.session_state['quiz_choices'] = []
if 'quiz_num' not in st.session_state:
    st.session_state['quiz_num'] = 1
if 'quiz_score' not in st.session_state:
    st.session_state['quiz_score'] = 0
if 'quiz_history' not in st.session_state:
    st.session_state['quiz_history'] = set()


if st.button('퀴즈 시작'):
    st.session_state['quiz_started'] = True
    st.session_state['quiz_num'] = 1
    st.session_state['quiz_score'] = 0
    st.session_state['quiz_history'] = set()
    # 중복 없는 정답 함수 선택
    available_funcs = [f for f in quiz_funcs if f[0] not in st.session_state['quiz_history']]
    answer_func = random.choice(available_funcs)
    st.session_state['quiz_history'].add(answer_func[0])
    # 오답 함수 3개 선택 (중복 없이)
    wrong_funcs = random.sample([f for f in quiz_funcs if f[0] != answer_func[0]], 3)
    # 섞기
    all_choices = wrong_funcs + [answer_func]
    random.shuffle(all_choices)
    st.session_state['quiz_answer'] = answer_func[0]
    st.session_state['quiz_choices'] = all_choices


if st.session_state['quiz_started']:
    st.markdown(f"**문제 {st.session_state['quiz_num']} / {MAX_QUIZ}**")
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
    selected = st.radio('정답 그래프를 선택하세요', options=[f'그래프 {i+1}' for i in range(4)], key=f'radio_{st.session_state["quiz_num"]}')
    if 'answer_checked' not in st.session_state:
        st.session_state['answer_checked'] = False
    if st.button('정답 확인') and not st.session_state['answer_checked']:
        answer_idx = [i for i, (fs, _) in enumerate(st.session_state['quiz_choices']) if fs == st.session_state['quiz_answer']][0]
        if selected == f'그래프 {answer_idx+1}':
            st.success('정답입니다!')
            st.session_state['quiz_score'] += 1
        else:
            st.error(f'오답입니다. 정답은 그래프 {answer_idx+1} 입니다.')
        st.session_state['answer_checked'] = True

    # 정답 확인 후에만 다음 문제 버튼 활성화
    if st.session_state['answer_checked']:
        if st.session_state['quiz_num'] < MAX_QUIZ:
            if st.button('다음 문제'):
                st.session_state['quiz_num'] += 1
                # 중복 없는 정답 함수 선택
                available_funcs = [f for f in quiz_funcs if f[0] not in st.session_state['quiz_history']]
                if available_funcs:
                    answer_func = random.choice(available_funcs)
                    st.session_state['quiz_history'].add(answer_func[0])
                else:
                    # 모든 함수가 출제되었으면 랜덤
                    answer_func = random.choice(quiz_funcs)
                wrong_funcs = random.sample([f for f in quiz_funcs if f[0] != answer_func[0]], 3)
                all_choices = wrong_funcs + [answer_func]
                random.shuffle(all_choices)
                st.session_state['quiz_answer'] = answer_func[0]
                st.session_state['quiz_choices'] = all_choices
                st.session_state['answer_checked'] = False
                st.rerun()
        else:
            st.session_state['quiz_started'] = False
            st.markdown(f'### 퀴즈 종료! 점수: {st.session_state["quiz_score"]} / {MAX_QUIZ}')
