import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# -----------------------------
# 데이터 불러오기
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("/mnt/data/pat.csv.csv", encoding="cp949")

df = load_data()

st.title("📌 반려동물 등록 데이터 분석 대시보드")

# -----------------------------
# 년도 선택
# -----------------------------
years = sorted(df["년도"].unique())
selected_year = st.selectbox("📅 년도를 선택하세요", years)

df_year = df[df["년도"] == selected_year].copy()

# -----------------------------
# 등록주체 + RFID 종류 합산
# -----------------------------
target_cols = [
    "등록주체(시군구)", "등록주체(대행업체)", "등록주체(기타(이벤트등))",
    "RFID종류(내장형)", "RFID종류(외장형)", "RFID종류(인식표)"
]

df_year["총합"] = df_year[target_cols].sum(axis=1)

# -----------------------------
# TOP10 추출
# -----------------------------
df_top10 = df_year.sort_values("총합", ascending=False).head(10).reset_index(drop=True)

# -----------------------------
# 그래프 색상 제작 (1등 빨간색, 나머지 파란 그라데이션)
# -----------------------------
colors = ["red"]
for i in range(1, len(df_top10)):
    blue_val = int(255 - (i * (180 / 10)))  # 너무 연해지지 않는 범위
    colors.append(f"rgb(0,0,{blue_val})")

# -----------------------------
# Plotly 막대그래프
# -----------------------------
fig = go.Figure()
fig.add_trace(go.Bar(
    x=df_top10["읍면동(법정동)"],
    y=df_top10["총합"],
    marker=dict(color=colors)
))

fig.update_layout(
    title=f"{selected_year}년도 읍면동 TOP10 등록 현황",
    xaxis_title="읍면동",
    yaxis_title="등록 수 합계",
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# 지도 시각화
# (경도/위도 컬럼이 없으면 geopy로 검색하도록 확장 가능)
# -----------------------------

st.subheader("📍 TOP10 위치 지도")

# ※ 사용자가 만든 데이터에는 좌표 정보가 없으므로
#   예시용 임시 좌표를 생성함 → 실제 데이터 있을 경우 바꿔주기!
df_top10["lat"] = 37.55 + (df_top10.index * 0.01)
df_top10["lon"] = 126.98 + (df_top10.index * 0.01)

map_fig = px.scatter_mapbox(
    df_top10,
    lat="lat",
    lon="lon",
    size="총합",
    hover_name="읍면동(법정동)",
    zoom=10,
    height=500
)

map_fig.update_layout(mapbox_style="open-street-map")
st.plotly_chart(map_fig, use_container_width=True)

