import streamlit as st


st.set_page_config(page_title='함수 학습 앱', page_icon='📈', layout='centered')

# 배경색 및 카드 스타일 적용
st.markdown(
	'''
	<style>
	body {
		background-color: #f6f8fa;
	}
	.main-card {
		background: white;
		border-radius: 18px;
		box-shadow: 0 4px 16px rgba(44,108,223,0.08);
		padding: 2.5rem 2rem 2rem 2rem;
		margin: 2rem auto;
		max-width: 600px;
	}
	.main-title {
		text-align: center;
		color: #2d6cdf;
		font-size: 2.3em;
		font-weight: bold;
		margin-bottom: 0.5em;
	}
	.main-desc {
		text-align: center;
		font-size: 1.25em;
		color: #444;
		margin-bottom: 1.5em;
	}
	.emoji {
		font-size: 2.5em;
		text-align: center;
		margin-bottom: 0.5em;
	}
	</style>
	<div class="main-card">
		<div class="emoji">📚✨</div>
		<div class="main-title">함수에 대해 알아보아요!</div>
		<div class="main-desc">오른쪽 목록을 클릭하여<br>함수를 그려보거나 퀴즈를 맞춰보세요.</div>
		<hr style="border:1px solid #eaeaea; margin:2em 0;">
		<div style="text-align:center; color:#888; font-size:1em;">수학적 직관을 키우는 첫걸음!</div>
	</div>
	''', unsafe_allow_html=True)

