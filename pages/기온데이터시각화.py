import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load and clean the data
file_path = 'daily_temp.csv'
data = pd.read_csv(file_path)
data.columns = data.columns.str.strip()
data['날짜'] = data['날짜'].str.strip()
data['날짜'] = pd.to_datetime(data['날짜'], format='%Y-%m-%d')
data['연도'] = data['날짜'].dt.year

# Calculate yearly statistics
yearly_stats = data.groupby('연도').agg({
    '평균기온(℃)': 'mean',
    '최저기온(℃)': 'min',
    '최고기온(℃)': 'max'
}).reset_index()

yearly_stats.rename(columns={'평균기온(℃)': '평균기온', '최저기온(℃)': '최저기온', '최고기온(℃)': '최고기온'}, inplace=True)

# Streamlit app
st.title('연도별 평균, 최저, 최고 기온 변화 추이')

# User selection for graph type
graph_type = st.selectbox('그래프 유형을 선택하세요', ('꺾은선 그래프', '막대 그래프'))

if graph_type == '꺾은선 그래프':
    # Plot line graph
    fig, ax = plt.subplots()
    ax.plot(yearly_stats['연도'], yearly_stats['평균기온'], label='평균기온')
    ax.plot(yearly_stats['연도'], yearly_stats['최저기온'], label='최저기온')
    ax.plot(yearly_stats['연도'], yearly_stats['최고기온'], label='최고기온')
    ax.set_xlabel('연도')
    ax.set_ylabel('기온 (℃)')
    ax.set_title('연도별 평균, 최저, 최고 기온 꺾은선 그래프')
    ax.legend()
    st.pyplot(fig)
elif graph_type == '막대 그래프':
    # Plot bar graph
    fig, ax = plt.subplots()
    bar_width = 0.25
    index = yearly_stats['연도']

    ax.bar(index - bar_width, yearly_stats['평균기온'], bar_width, label='평균기온')
    ax.bar(index, yearly_stats['최저기온'], bar_width, label='최저기온')
    ax.bar(index + bar_width, yearly_stats['최고기온'], bar_width, label='최고기온')

    ax.set_xlabel('연도')
    ax.set_ylabel('기온 (℃)')
    ax.set_title('연도별 평균, 최저, 최고 기온 막대 그래프')
    ax.legend()
    st.pyplot(fig)
