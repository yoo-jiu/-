import plotly.graph_objects as go

with tab2:
    st.subheader("🧠 MBTI 유형별 국가 순위")
    st.write("MBTI 유형을 선택하면 해당 유형 비율이 높은 10개국을 볼 수 있습니다.")

    mbti_types = [c for c in df.columns if c != "Country"]
    selected_type = st.selectbox("MBTI 유형을 선택하세요", mbti_types, key="mbti_type")

    # 상위 10개국 + South Korea 포함
    top10_df = df[["Country", selected_type]].sort_values(by=selected_type, ascending=False).head(10)
    if "South Korea" not in top10_df["Country"].values:
        sk_row = df[df["Country"] == "South Korea"]
        if not sk_row.empty:
            top10_df = pd.concat([top10_df, sk_row[["Country", selected_type]]])

    # 색상 기본값 (1등: 빨강, 나머지: 파랑 계열)
    colors = []
    for i, country in enumerate(top10_df["Country"].values):
        if i == 0:
            colors.append("#FF3B30")
        elif country == "South Korea":
            colors.append("gradient")  # 나중에 커스텀 처리
        else:
            alpha = 0.3 + 0.7 * (1 - i / len(top10_df))
            colors.append(f"rgba(0,102,255,{alpha:.2f})")

    # 그래프 객체 생성
    fig = go.Figure()

    for i, (country, value, color) in enumerate(zip(top10_df["Country"], top10_df[selected_type], colors)):
        if color != "gradient":
            # 일반 막대
            fig.add_trace(go.Bar(
                x=[country],
                y=[value],
                text=[f"{value*100:.1f}%"],
                textposition="outside",
                marker_color=color,
                name=country
            ))
        else:
            # South Korea 전용 그라데이션 (빨강 → 파랑)
            fig.add_trace(go.Bar(
                x=[country],
                y=[value],
                text=[f"{value*100:.1f}%"],
                textposition="outside",
                marker=dict(
                    color=[0, 1],  # 그라데이션 정의용
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
