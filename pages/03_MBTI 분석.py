import streamlit as st
import pandas as pd
import plotly.express as px

# 페이지 기본 설정
st.set_page_config(page_title="세계 MBTI 비율 시각화 🌍", page_icon="🧠", layout="wide")

# 제목
st.title("🌍 세계 MBTI 데이터 분석 대시보드")

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

# 탭 구성
tab1, tab2 = st.tabs(["📊 나라별 MBTI 분석", "🧠 MBTI 유형별 국가 비교"])

# ========== [탭 1] 나라별 분석 ==========
with tab1:
    st.subheader("📊 나라별 MBTI 비율")
    st.write("국가를 선택하면 해당 국가의 MBTI 유형 분포를 볼 수 있습니다.")

    # 국가 선택
    country_list = sorted(df["Country"].unique())
    selected_country = st.selectbox("국가를 선택하세요 🌎", country_list, key="country")

    # 선택한 국가 데이터 추출
    country_data = df[df["Country"] == selected_country].iloc[0, 1:]
    country_df = pd.DataFrame({
        "MBTI": country_data.index,
        "비율": country_data.values
    }).sort_values(by="비율", ascending=False)

    # 색상 설정
    top_type = country_df.iloc[0]["MBTI"]
    n = len(country_df)
    colors = [
        "#FF3B30" if mbti == top_type else f"rgba(0,102,255,{0.3+0.7*(1-i/n):.2f})"
        for i, mbti in enumerate(country_df["MBTI"])
    ]

    # Plotly 그래프
    fig = px.bar(
        country_df,
        x="MBTI",
        y="비율",
        text=country_df["비율"].apply(lambda x: f"{x*100:.1f}%")
    )
    fig.update_traces(marker_color=colors, textposition="outside")
    fig.update_layout(
        title=f"🇺🇳 {selected_country}의 MBTI 유형 비율",
        xaxis_title="MBTI 유형",
        yaxis_title="비율",
        template="simple_white",
        showlegend=False
    )

    st.plotly_chart(fig, use_container_width=True)

# ========== [탭 2] MBTI별 분석 ==========
with tab2:
    st.subheader("🧠 MBTI 유형별 국가 순위")
    st.write("MBTI 유형을 선택하면 해당 유형 비율이 높은 10개국을 볼 수 있습니다.")

    # MBTI 리스트
    mbti_types = [c for c in df.columns if c != "Country"]
    selected_type = st.selectbox("MBTI 유형을 선택하세요", mbti_types, key="mbti_type")

    # 선택한 MBTI 기준 상위 10개국
    top10_df = df[["Country", selected_type]].sort_values(by=selected_type, ascending=False).head(10)

    # South Korea 포함 여부 확인
    if "South Korea" not in top10_df["Country"].values:
        sk_row = df[df["Country"] == "South Korea"]
        if not sk_row.empty:
            top10_df = pd.concat([top10_df, sk_row[["Country", selected_type]]])

    # 색상 설정 (1등 빨강, 나머지 파랑)
    n = len(top10_df)
    colors = [
        "#FF3B30" if i == 0 else f"rgba(0,102,255,{0.3+0.7*(1-i/n):.2f})"
        for i in range(n)
    ]

    # 막대그래프 생성
    fig2 = px.bar(
        top10_df,
        x="Country",
        y=selected_type,
        text=top10_df[selected_type].apply(lambda x: f"{x*100:.1f}%"),
    )
    fig2.update_traces(marker_color=colors, textposition="outside")
    fig2.update_layout(
        title=f"🌐 {selected_type} 비율이 높은 국가 TOP 10 (+South Korea)",
        xaxis_title="국가",
        yaxis_title="비율",
        template="simple_white",
        showlegend=False
    )

    st.plotly_chart(fig2, use_container_width=True)

st.caption("📊 데이터: countriesMBTI_16types.csv — 158개국 MBTI 분포 데이터")
