

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# NanumGothic 폰트 경로 지정
font_path = '/workspaces/25.09.25../fonts/NanumGothic-Regular.ttf'
fontprop = fm.FontProperties(fname=font_path)

plt.rc('font', family=fontprop.get_name())


st.title('함수 그래프 그리기')

st.write('아래에 함수를 입력하세요. 예: sin(x), x**2, exp(-x)')

func_str = st.text_input('함수 입력', value='sin(x)')
x_min = st.number_input('x 최소값', value=-10.0)
x_max = st.number_input('x 최대값', value=10.0)
num_points = st.slider('샘플 포인트 수', min_value=100, max_value=2000, value=500)

if func_str:
	try:
		x = np.linspace(x_min, x_max, num_points)
		# 안전하게 eval을 사용하기 위해 numpy 함수만 허용
		allowed_names = {k: getattr(np, k) for k in dir(np) if not k.startswith('_')}
		allowed_names['x'] = x
		y = eval(func_str, {"__builtins__": {}}, allowed_names)
		fig, ax = plt.subplots()
		ax.plot(x, y)
		ax.set_xlabel('x', fontproperties=fontprop)
		ax.set_ylabel('f(x)', fontproperties=fontprop)
		ax.set_title(f'f(x) = {func_str}', fontproperties=fontprop)
		st.pyplot(fig)
	except Exception as e:
		st.error(f'그래프를 그릴 수 없습니다: {e}')
