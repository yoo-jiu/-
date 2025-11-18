import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# CSV 경로 (루트 폴더)
DATA_PATH = "subway.csv"

def load_data():
    return pd.read_csv(DATA_PATH, encoding="cp949")

# 페이지 UI 시작
st.title("📊 지하철 승하차 데이터 분석 (2025년 11월)")

# 데이터 불러오기
df = load_data()

# 날짜 및 호선 선택
dates = sorted(df["사용일자"].unique())
selected_date = st.selectbox("📅 날짜 선택", dates)

lines = sorted(df["노선명"].unique())
selected_line = st.selectbox("🚇 호선 선택", lines)

# 필터링
df_filtered = df[(df["사용일자"] == selected_date) & (df["노선명"] == selected_line)].copy()

# 승하차 총합 계산
df_filtered["총이용객"] = df_filtered["승차총승객수"] + df_filtered["하차총승객수"]

df_sorted = df_filtered.sort_values("총이용객", ascending=False)

# 색상 설정: 1등 빨간색, 나머지는 파란색 계열 그라데이션
colors = ["red"]
blue_grad = [f"rgba(0,0,255,{0.9 - i*0.02})" for i in range(len(df_sorted) - 1)]
colors.extend(blue_grad)

# 그래프 생성
fig = go.Figure()
fig.add_trace(go.Bar(
    x=df_sorted["역명"],
    y=df_sorted["총이용객"],
    marker=dict(color=colors)
))

fig.update_layout(
    title=f"{selected_date} / {selected_line} 승하차 총이용객 순위",
    xaxis_title="역명",
    yaxis_title="총 승하차 인원",
    template="plotly_white"
)

# 그래프 출력
st.plotly_chart(fig, use_container_width=True)
