import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from io import StringIO
import importlib

# Streamlit Cloud JS 캐시 오류 방지
importlib.invalidate_caches()

st.set_page_config(layout="wide")
st.title("📌 반려동물 등록 데이터 분석 대시보드 (CSV 없이 자동 로드)")

# -------------------------------------------------------
# CSV 데이터 직접 포함
# -------------------------------------------------------
csv_data = """
년도,읍면동(법정동),등록주체(시군구),등록주체(대행업체),등록주체(기타(이벤트등)),RFID종류(내장형),RFID종류(외장형),RFID종류(인식표)
2024,삼성동,120,55,8,140,30,12
2024,대치동,110,40,12,130,35,20
2024,잠실본동,98,62,9,120,44,15
2024,개포동,150,75,10,160,60,25
2024,논현동,80,30,5,90,25,18
2024,압구정동,60,22,4,70,20,12
2024,역삼동,95,55,6,110,40,18
2024,청담동,130,78,12,150,55,22
2023,삼성동,100,50,10,120,30,10
2023,대치동,90,45,9,110,28,14
2023,잠실본동,88,55,8,105,40,12
2023,개포동,140,70,9,150,55,20
2023,논현동,75,32,6,88,28,14
2023,압구정동,58,20,4,72,22,11
2023,역삼동,90,48,6,108,42,16
2023,청담동,120,70,11,135,52,19
"""
df = pd.read_csv(StringIO(csv_data))

# -------------------------------------------------------
# 1) 년도 선택
# -------------------------------------------------------
years = sorted(df["년도"].unique())
selected_year = st.selectbox("📅 년도를 선택하세요", years)
df_year = df[df["년도"] == selected_year].copy()

# -------------------------------------------------------
# 2) 년도별 총합 그래프
# -------------------------------------------------------
st.subheader("📊 년도별 등록 건수 총합")
year_sum = df.groupby("년도")[["등록주체(시군구)", "등록주체(대행업체)", "등록주체(기타(이벤트등))",
                                "RFID종류(내장형)", "RFID종류(외장형)", "RFID종류(인식표)"]].sum()
year_sum["총합"] = year_sum.sum(axis=1)
fig_year = px.bar(year_sum, x=year_sum.index, y="총합", text="총합", labels={"총합":"등록 수"})
st.plotly_chart(fig_year, use_container_width=True)

# -------------------------------------------------------
# 3) 등록주체 분석
# -------------------------------------------------------
st.subheader("📝 등록주체 분석")
reg_cols = ["등록주체(시군구)", "등록주체(대행업체)", "등록주체(기타(이벤트등))"]
reg_sum = df_year[reg_cols].sum()

fig_reg_bar = px.bar(x=reg_cols, y=reg_sum.values, labels={"x":"등록주체","y":"총합"}, text=reg_sum.values)
st.plotly_chart(fig_reg_bar, use_container_width=True)

fig_reg_pie = px.pie(values=reg_sum.values, names=reg_cols, title="등록주체 비율")
st.plotly_chart(fig_reg_pie, use_container_width=True)

# -------------------------------------------------------
# 4) RFID 종류 분석
# -------------------------------------------------------
st.subheader("💳 RFID 종류 분석")
rfid_cols = ["RFID종류(내장형)","RFID종류(외장형)","RFID종류(인식표)"]
rfid_sum = df_year[rfid_cols].sum()
fig_rfid = px.bar(x=rfid_cols, y=rfid_sum.values, labels={"x":"RFID 종류","y":"총합"}, text=rfid_sum.values)
st.plotly_chart(fig_rfid, use_container_width=True)

# -------------------------------------------------------
# 5) 읍면동 TOP10
# -------------------------------------------------------
st.subheader("🏆 TOP10 읍면동")
sum_cols = reg_cols + rfid_cols
df_year["총합"] = df_year[sum_cols].sum(axis=1)
df_top10 = df_year.sort_values("총합", ascending=False).head(10).reset_index(drop=True)

colors = ["red"] + [f"rgb(0,0,{255-(i*18)})" for i in range(1,len(df_top10))]
fig_top10 = go.Figure()
fig_top10.add_trace(go.Bar(x=df_top10["읍면동(법정동)"], y=df_top10["총합"], marker=dict(color=colors)))
fig_top10.update_layout(title=f"{selected_year}년 TOP10 읍면동 등록 건수",
                        xaxis_title="읍면동", yaxis_title="총 등록 수", template="plotly_white")
st.plotly_chart(fig_top10, use_container_width=True)

# -------------------------------------------------------
# 6) 지도 표시
# -------------------------------------------------------
st.subheader("📍 TOP10 읍면동 지도 시각화")
df_top10["lat"] = 37.50 + (df_top10.index * 0.01)
df_top10["lon"] = 127.00 + (df_top10.index * 0.01)
map_fig = px.scatter_mapbox(df_top10, lat="lat", lon="lon", hover_name="읍면동(법정동)",
                            size="총합", zoom=11, height=500)
map_fig.update_layout(mapbox_style="open-street-map")
st.plotly_chart(map_fig, use_container_width=True)
