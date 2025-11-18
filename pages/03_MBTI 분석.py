import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="MBTI 분석 대시보드", layout="wide")

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

st.title("🌍 MBTI 국가별 분석 대시보드")

# 탭 생성
tab1, tab2 = st.tabs(["📌 국가별 MBTI 비율", "📌 MBTI별 상위 국가 분석"])

# ============================================
# 📌 TAB 1 — "국가를 선택하면 MBTI 비율 그래프"
# ============================================
with tab1:

    country = st.selectbox("국가를 선택하세요:", df["Country"].unique())

    selected = df[df["Country"] == country].iloc[0]

    mbti_cols = df.columns[1:]
    mbti_values = selected[mbti_cols]

    # 1등은 빨간색 / 나머지는 파란색 그라디언트
    max_type = mbti_values.idxmax()

    colors = [
        "#FF0000" if col == max_type else "rgba(30,144,255,0.6)"
        for col in mbti_cols
    ]

    fig1 = px.bar(
        x=mbti_cols,
        y=mbti_values,
        color=mbti_cols,
        color_discrete_sequence=colors,
        title=f"🇺🇳 {country} MBTI 비율"
    )

    fig1.update_layout(showlegend=False, xaxis_title="MBTI 유형", yaxis_title="비율(%)")
    st.plotly_chart(fig1, use_container_width=True)

# ============================================
# 📌 TAB 2 — "MBTI 선택 → 상위 10개 국가"
# ============================================
with tab2:

    mbti_type = st.selectbox("MBTI 유형을 선택하세요:", df.columns[1:])

    # 해당 MBTI 기준으로 정렬
    sorted_df = df.sort_values(by=mbti_type, ascending=False)

    # TOP10 나라 추출
    top10 = sorted_df.head(10).copy()

    # South Korea 포함 여부 체크
    if "South Korea" not in top10["Country"].values:
        sk_row = df[df["Country"] == "South Korea"]
        if not sk_row.empty:
            top10 = pd.concat([top10, sk_row], ignore_index=True)

    # 색상 설정
    bar_colors = []
    for country in top10["Country"]:
        if country == "South Korea":
            bar_colors.append("#00AA00")  # ★ 대한민국: 초록색
        else:
            bar_colors.append("rgba(30,144,255,0.8)")  # 기본 파란색

    fig2 = px.bar(
        top10,
        x="Country",
        y=mbti_type,
        color="Country",
        color_discrete_sequence=bar_colors,
        title=f"🌐 {mbti_type} 비율이 높은 국가 TOP10 (South Korea 자동 포함)"
    )

    fig2.update_layout(showlegend=False, xaxis_title="국가", yaxis_title="비율(%)")
    st.plotly_chart(fig2, use_container_width=True)
