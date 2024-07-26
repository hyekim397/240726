import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import os

# 파일 경로 설정
file_path = 'score_refined.csv'  # Update this path

# 데이터 읽기
try:
    data = pd.read_csv(file_path, encoding='euc-kr')  # 인코딩을 euc-kr로 지정
except UnicodeDecodeError:
    st.error('파일을 읽는 도중 인코딩 문제 발생. 파일 인코딩을 확인하세요.')
    st.stop()

# 점수 변화 계산
data['영어 점수 변화'] = data['기말 영어 점수'] - data['중간 영어 점수']
data['수학 점수 변화'] = data['기말 수학 점수'] - data['중간 수학 점수']

# 영어 점수 변화
most_improved_english = data.loc[data['영어 점수 변화'].idxmax()]
most_declined_english = data.loc[data['영어 점수 변화'].idxmin()]

# 수학 점수 변화
most_improved_math = data.loc[data['수학 점수 변화'].idxmax()]
most_declined_math = data.loc[data['수학 점수 변화'].idxmin()]

# Streamlit 앱 설정
st.title('점수 변화 분석 📊')

# 가장 많이 향상된 학생
st.header('가장 많이 향상된 학생 🎉')
st.subheader('영어')
st.write(f"학생 이름: {most_improved_english['이름']}")
st.write(f"중간 영어 점수: {most_improved_english['중간 영어 점수']}")
st.write(f"기말 영어 점수: {most_improved_english['기말 영어 점수']}")
st.write(f"점수 변화: {most_improved_english['영어 점수 변화']}점 증가")

st.subheader('수학')
st.write(f"학생 이름: {most_improved_math['이름']}")
st.write(f"중간 수학 점수: {most_improved_math['중간 수학 점수']}")
st.write(f"기말 수학 점수: {most_improved_math['기말 수학 점수']}")
st.write(f"점수 변화: {most_improved_math['수학 점수 변화']}점 증가")

# 가장 많이 하향된 학생
st.header('가장 많이 하향된 학생 😢')
st.subheader('영어')
st.write(f"학생 이름: {most_declined_english['이름']}")
st.write(f"중간 영어 점수: {most_declined_english['중간 영어 점수']}")
st.write(f"기말 영어 점수: {most_declined_english['기말 영어 점수']}")
st.write(f"점수 변화: {most_declined_english['영어 점수 변화']}점 감소")

st.subheader('수학')
st.write(f"학생 이름: {most_declined_math['이름']}")
st.write(f"중간 수학 점수: {most_declined_math['중간 수학 점수']}")
st.write(f"기말 수학 점수: {most_declined_math['기말 수학 점수']}")
st.write(f"점수 변화: {most_declined_math['수학 점수 변화']}점 감소")
