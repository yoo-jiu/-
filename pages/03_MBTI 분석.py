import streamlit as st
import pandas as pd
import plotly.express as px

# 페이지 기본 설정
st.set_page_config(page_title="세계 MBTI 비율 시각화 🌍", page_icon="🧠", layout="centered")

# 제목 및 설명
st.title("🌍 나라별 MBTI 비율 시각화")
st.markdown("국가를 선택하면 해당 나라의 MBTI 유형별 비율을 한눈에 볼 수 있어요!")

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

# 국가 선택
country_list = sorted(df["Country"].unique())
selected_country = st.selectbox("국가를 선택하세요 🌎", country_list)

# 선택한 국가 데이터 추출
country_row = df[df["Country"] == selected_country].iloc[0, 1:]
country_df = pd.DataFrame({
    "MBTI": country_row.index,
    "비율": country_row.values
}).sort_values(by="비율", ascending=False)

# 색상 설정: 1등은 빨강, 나머지는 파란색 그라데이션
top_mbti = country_df.iloc[0]["MBTI"]
colors = []
n = len(country_df)
for i, mbti in enumerate(country_df["MBTI"]):
    if mbti == top_mbti:
        colors.append("#FF3B30")  # 빨간색
    else:
        opacity = 0.3 + 0.7 * (1 - i / n)  # 점점 옅어지는 파랑
        colors.append(f"rgba(0, 102, 255, {opacity})")

# Plotly 막대 그래프 생성
fig = px.bar(
    country_df,
    x="MBTI",
    y="비율",
    text=country_df["비율"].apply(lambda x: f"{x*100:.1f}%")
)

fig.update_traces(
    marker_color=colors,
    textposition="outside",
    hovertemplate="<b>%{x}</b><br>비율: %{y:.2%}<extra></extra>"
)

fig.update_layout(
    title=dict(text=f"🇺🇳 {selected_country}의 MBTI 비율", x=0.5, font=dict(size=20)),
    xaxis_title="MBTI 유형",
    yaxis_title="비율",
    template="simple_white",
    showlegend=False,
    margin=dict(l=40, r=40, t=80, b=40)
)

# 그래프 표시
st.plotly_chart(fig, use_container_width=True)

# 하단 문구
st.caption("📊 데이터 출처: countriesMBTI_16types.csv — 158개국 MBTI 분포 데이터")
st.markdown("---")
st.markdown("👨‍💻 **Made with ❤️ using Streamlit + Plotly**")
