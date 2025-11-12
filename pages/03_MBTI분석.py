import streamlit as st
import pandas as pd
import plotly.express as px

# 앱 기본 설정
st.set_page_config(page_title="세계 MBTI 비율 시각화", page_icon="🌍", layout="centered")

st.title("🌍 나라별 MBTI 비율 시각화")
st.write("국가를 선택하면 각 MBTI 유형의 비율을 확인할 수 있어요!")

# CSV 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

# 국가 선택
country_list = sorted(df["Country"].unique())
selected_country = st.selectbox("국가를 선택하세요 🌎", country_list)

# 선택한 국가의 MBTI 비율 추출
country_data = df[df["Country"] == selected_country].iloc[0, 1:]
country_df = pd.DataFrame({
    "MBTI": country_data.index,
    "비율": country_data.values
}).sort_values(by="비율", ascending=False)

# 1위 MBTI 확인
top_type = country_df.iloc[0]["MBTI"]

# 색상 설정 (1등은 빨강, 나머지는 파랑 그라데이션)
colors = ["#FF4B4B" if mbti == top_type else f"rgba(0, 102, 255, {0.2 + 0.8*(1-i/len(country_df))})"
          for i, mbti in enumerate(country_df["MBTI"])]

# Plotly 막대 그래프 생성
fig = px.bar(
    country_df,
    x="MBTI",
    y="비율",
    text=country_df["비율"].apply(lambda x: f"{x*100:.1f}%"),
)
fig.update_traces(marker_color=colors, textposition="outside")
fig.update_layout(
    title=f"🇨🇭 {selected_country}의 MBTI 유형 비율",
    xaxis_title="MBTI 유형",
    yaxis_title="비율",
    template="simple_white",
    showlegend=False
)

st.plotly_chart(fig, use_container_width=True)

# 부가정보
st.caption("💡 데이터: countriesMBTI_16types.csv — 158개국 MBTI 분포")
