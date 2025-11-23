import streamlit as st
import pandas as pd
import plotly.express as px
import io

st.set_page_config(layout="wide", page_title="반려동물 등록 데이터 분석")
st.title("📊 반려동물 등록 데이터 분석")

# CSV 문자열

csv_data = """년도,읍면동,등록주체,RFID,등록수,위도,경도
2023,강남구,주인,마이크로칩,150,37.4979,127.0276
2023,서초구,주인,마이크로칩,120,37.4831,127.0324
2023,송파구,주인,마이크로칩,100,37.5143,127.1059
2023,강남구,동물병원,마이크로칩,80,37.4979,127.0276
2024,강남구,주인,마이크로칩,160,37.4979,127.0276
2024,서초구,주인,마이크로칩,130,37.4831,127.0324
2024,송파구,주인,마이크로칩,110,37.5143,127.1059
2024,강남구,동물병원,마이크로칩,90,37.4979,127.0276
"""

# CSV 읽기

df = pd.read_csv(io.StringIO(csv_data))

# 사이드바 필터

year_selected = st.sidebar.multiselect("년도 선택", sorted(df['년도'].unique()), default=sorted(df['년도'].unique()))
district_selected = st.sidebar.multiselect("읍면동 선택", sorted(df['읍면동'].unique()), default=sorted(df['읍면동'].unique()))
owner_selected = st.sidebar.multiselect("등록주체 선택", sorted(df['등록주체'].unique()), default=sorted(df['등록주체'].unique()))
rfid_selected = st.sidebar.multiselect("RFID 선택", sorted(df['RFID'].unique()), default=sorted(df['RFID'].unique()))

df_filtered = df[
(df['년도'].isin(year_selected)) &
(df['읍면동'].isin(district_selected)) &
(df['등록주체'].isin(owner_selected)) &
(df['RFID'].isin(rfid_selected))
]

st.markdown("### 필터링된 데이터")
st.dataframe(df_filtered)

# TOP10

st.markdown("### 📈 TOP10 등록수")
df_top10 = df_filtered.groupby('읍면동')['등록수'].sum().reset_index()
df_top10 = df_top10.sort_values(by='등록수', ascending=False).head(10)

# 색상: 1등 빨강, 나머지 점점 연한 파랑

blue_scale = px.colors.sequential.Blues
if len(df_top10) > 1:
n = len(df_top10) - 1
step = max(1, len(blue_scale)//n)
colors = ['red'] + [blue_scale[i*step] for i in range(n)]
else:
colors = ['red']

fig_bar = px.bar(
df_top10,
x='읍면동',
y='등록수',
text='등록수'
)
fig_bar.update_traces(marker_color=colors, textposition='outside')
st.plotly_chart(fig_bar, use_container_width=True)

# 지도

st.markdown("### 🗺 지도 시각화")
if not df_filtered.empty:
fig_map = px.scatter_mapbox(
df_filtered,
lat="위도",
lon="경도",
size="등록수",
color="등록수",
hover_name="읍면동",
size_max=30,
zoom=10,
color_continuous_scale=px.colors.sequential.Blues
)
fig_map.update_layout(mapbox_style="open-street-map")
st.plotly_chart(fig_map, use_container_width=True)
else:
st.info("선택된 조건에 맞는 데이터가 없습니다.")
