import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import importlib
import sys

# Streamlit Cloud에서 JS 파일 캐시 오류 방지
importlib.invalidate_caches()

st.set_page_config(layout="wide")
st.title("📌 반려동물 등록 데이터 분석 대시보드")

# -------------------------------------------------------
# 1) 파일 업로더
# -------------------------------------------------------
uploaded_file = st.file_uploader("📁 CSV 파일을 업로드하세요", type=["csv"])

if uploaded_file is not None:

    # CSV 파일 로드
    df = pd.read_csv(uploaded_file, encoding="cp949")

    # -------------------------------------------------------
    # 2) 년도 선택
    # -------------------------------------------------------
    years = sorted(df["년도"].unique())
    selected_year = st.selectbox("📅 년도를 선택하세요", years)

    df_year = df[df["년도"] == selected_year].copy()

    # -------------------------------------------------------
    # 3) 등록주체 + RFID 합산
    # -------------------------------------------------------
    sum_cols = [
        "등록주체(시군구)", "등록주체(대행업체)", "등록주체(기타(이벤트등))",
        "RFID종류(내장형)", "RFID종류(외장형)", "RFID종류(인식표)"
    ]

    df_year["총합"] = df_year[sum_cols].sum(axis=1)

    # -------------------------------------------------------
    # 4) TOP10 선정
    # -------------------------------------------------------
    df_top10 = df_year.sort_values("총합", ascending=False).head(10).reset_index(drop=True)

    # -------------------------------------------------------
    # 5) 막대그래프 색상 (1등=빨강, 나머지 파랑 그라데이션)
    # -------------------------------------------------------
    colors = ["red"]
    for i in range(1, len(df_top10)):
        blue_shade = int(255 - (i * 15))
        colors.append(f"rgb(0,0,{blue_shade})")

    # -------------------------------------------------------
    # 6) Plotly 막대그래프
    # -------------------------------------------------------
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df_top10["읍면동(법정동)"],
        y=df_top10["총합"],
        marker=dict(color=colors)
    ))

    fig.update_layout(
        title=f"🏆 {selected_year}년 TOP10 읍면동 등록 건수",
        xaxis_title="읍면동",
        yaxis_title="총 등록 수",
        template="plotly_white"
    )

    st.plotly_chart(fig, use_container_width=True)

    # -------------------------------------------------------
    # 7) 지도 표시 (실제 좌표 없어서 임시 생성)
    # -------------------------------------------------------
    st.subheader("📍 TOP10 지도 시각화")

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

else:
    st.info("📥 CSV 파일을 업로드하면 분석이 시작됩니다.")
