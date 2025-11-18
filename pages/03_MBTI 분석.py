import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="세계 MBTI 데이터 분석", page_icon="🧠", layout="wide")

st.title("🌍 세계 MBTI 데이터 분석 대시보드")

# --- 데이터 불러오기 ---
@st.cache_data
def load_data():
    return pd.read_csv("countriesMBTI_16types.csv")

df = load_data()

# --- 탭 생성 ---
tab1, tab2 = st.tabs(["📊 나라별 MBTI 분석", "🧠 MBTI 유형별 국가 비교"])

# ---------------------- [탭 1: 나라별 MBTI 분석] ----------------------
with tab1:
    st.subheader("📊 나라별 MBTI 비율")
    country_list = sorted(df["Country"].unique())
    selected_country = st.selectbox("국가를 선택하세요 🌎", country_list, key="country")

    country_data = df[df["Country"] == selected_country].iloc[0, 1:]
    country_df = pd.DataFrame({
        "MBTI": country_data.index,
        "비율": country_data.values
    }).sort_values(by="비율", ascending=False)

    top_type = country_df.iloc[0]["MBTI"]
    n = len(country_df)
    colors = [
        "#FF3B30" if mbti == top_type else f"rgba(0,102,255,{0.3+0.7*(1-i/n):.2f})"
        for i, mbti in enumerate(country_df["MBTI"])
    ]

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

# ---------------------- [탭 2: MBTI별 국가 비교] ----------------------
with tab2:
    st.subheader("🧠 MBTI 유형별 국가 순위")
    mbti_types = [c for c in df.columns if c != "Country"]
    selected_type = st.selectbox("MBTI 유형을 선택하세요", mbti_types, key="mbti_type")

    # 상위 10개국 + South Korea 포함
    top10_df = df[["Country", selected_type]].sort_values(by=selected_type, ascending=False).head(10)
    if "South Korea" not in top10_df["Country"].values:
        sk_row = df[df["Country"] == "South Korea"]
        if not sk_row.empty:
            top10_df = pd.concat([top10_df, sk_row[["Country", selected_type]]])

    # 색상 설정
    colors = []
    for i, country in enumerate(top10_df["Country"].values):
        if i == 0:
            colors.append("#FF3B30")
        elif country == "South Korea":
            colors.append("gradient")
        else:
            alpha = 0.3 + 0.7 * (1 - i / len(top10_df))
            colors.append(f"rgba(0,102,255,{alpha:.2f})")

    fig = go.Figure()

    for i, (country, value, color) in enumerate(zip(top10_df["Country"], top10_df[selected_type], colors)):
        if color != "gradient":
            fig.add_trace(go.Bar(
                x=[country],
                y=[value],
                text=[f"{value*100:.1f}%"],
                textposition="outside",
                marker_color=color,
                name=country
            ))
        else:
            # South Korea 전용 (위 빨강, 아래 파랑)
            fig.add_trace(go.Bar(
                x=[country],
                y=[value],
                text=[f"{value*100:.1f}%"],
                textposition="outside",
                marker=dict(
                    color=[0, 1],
                    colorscale=[[0, "#FF3B30"], [1, "#0066FF"]],
                    showscale=False
                ),
                name="South Korea"
            ))

    fig.update_layout(
        title=f"🌐 {selected_type} 비율이 높은 국가 TOP 10 (+South Korea 강조)",
        xaxis_title="국가",
        yaxis_title="비율",
        template="simple_white",
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)
