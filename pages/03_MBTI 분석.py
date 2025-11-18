import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="MBTI 분석 대시보드", layout="wide")

# 데이터 불러오기
@st.cache_data
def load_data():
    return pd.read_csv("countriesMBTI_16types.csv")

df = load_data()

st.title("🌍 MBTI 국가별 분석 대시보드")

# 탭 구성
tab1, tab2 = st.tabs(["📌 국가별 MBTI 비율", "📌 MBTI별 상위 국가 분석"])


# ======================================================
# 📌 TAB 1 — "국가 선택 → MBTI 비율 시각화"
# ======================================================
with tab1:

    country = st.selectbox("국가를 선택하세요:", df["Country"].unique())

    selected = df[df["Country"] == country].iloc[0]
    mbti_cols = df.columns[1:]
    mbti_values = selected[mbti_cols]

    # 1등은 빨간색, 나머지는 파란색
    max_type = mbti_values.idxmax()
    colors = ["#FF0000" if col == max_type else "rgba(30,144,255,0.6)" for col in mbti_cols]

    fig1 = px.bar(
        x=mbti_cols,
        y=mbti_values,
        color=mbti_cols,
        color_discrete_sequence=colors,
        title=f"🇺🇳 {country} MBTI 비율"
    )

    fig1.update_layout(showlegend=False, xaxis_title="MBTI 유형", yaxis_title="비율(%)")
    st.plotly_chart(fig1, use_container_width=True)



# ======================================================
# 📌 TAB 2 — "MBTI 선택 → 해당 MBTI 높은 국가 TOP10"
# ======================================================
with tab2:

    mbti_type = st.selectbox("MBTI 유형을 선택하세요:", df.columns[1:])

    sorted_df = df.sort_values(by=mbti_type, ascending=False)
    top10 = sorted_df.head(10).copy()

    # South Korea 추가 여부 확인
    if "South Korea" not in top10["Country"].values:
        sk = df[df["Country"] == "South Korea"]
        if not sk.empty:
            top10 = pd.concat([top10, sk], ignore_index=True)

    # 🔥 파란색 그라데이션 생성
    #    밝 → 어둡 파랑 (10개)
    gradient_blue = [
        f"rgba(0, 100, 255, {0.35 + i*0.05})"
        for i in range(len(top10))
    ]

    # South Korea 초록색 + 나머지는 그라데이션
    bar_colors = []
    for idx, row in top10.iterrows():
        if row["Country"] == "South Korea":
            bar_colors.append("#00AA00")  # 초록색
        else:
            bar_colors.append(gradient_blue[idx])

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
