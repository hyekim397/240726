import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import os

# 파일 경로 설정
file_path = 'score.csv'  # Update this path

# 데이터 읽기
data = pd.read_csv(file_path)

# Streamlit 앱 설정
st.title('학생별 중간 및 기말 점수 변화 추이 📈')

# 학생 선택
student_name = st.selectbox('학생 이름을 선택하세요', data['이름'].unique())

# 선택된 학생의 데이터 필터링
student_data = data[data['이름'] == student_name]

# 영어 점수 변화 시각화
fig, ax = plt.subplots()
ax.plot(['중간', '기말'], 
        [student_data['중간 영어 점수'].values[0], student_data['기말 영어 점수'].values[0]], 
        marker='o', label='영어', color='blue')
ax.set_xlabel('시험 종류')
ax.set_ylabel('점수')
ax.set_title(f'{student_name}의 영어 점수 변화 📘')
ax.legend()
st.pyplot(fig)

# 수학 점수 변화 시각화
fig, ax = plt.subplots()
ax.plot(['중간', '기말'], 
        [student_data['중간 수학 점수'].values[0], student_data['기말 수학 점수'].values[0]], 
        marker='o', label='수학', color='red')
ax.set_xlabel('시험 종류')
ax.set_ylabel('점수')
ax.set_title(f'{student_name}의 수학 점수 변화 📐')
ax.legend()
st.pyplot(fig)
