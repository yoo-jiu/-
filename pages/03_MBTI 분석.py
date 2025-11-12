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
    colors = []
    for i, country in enumerate(top10_df["Country"].values):
        if i == 0:
            colors.append("#FF3B30")  # 1등 빨강
        elif country == "South Korea":
            # South Korea는 위 빨강 → 아래 파랑 느낌 (시각적으로 blend한 색상)
            colors.append("linear-gradient(180deg, #FF3B30 0%, #0066FF 100%)")
        else:
            alpha = 0.3 + 0.7 * (1 - i / len(top10_df))
            colors.append(f"rgba(0,102,255,{alpha:.2f})")

    # Plotly에서는 gradient 문자열을 직접 지원하지 않으므로
    # South Korea 전용 색상은 중간 보라빛 계열로 대체
    final_colors = [
        "#FF3B30" if i == 0 else
        "#7F3FFF" if c.startswith("linear-gradient") else
        c
        for i, c in enumerate(colors)
    ]

    # 막대그래프 생성
    fig2 = px.bar(
        top10_df,
        x="Country",
        y=selected_type,
        text=top10_df[selected_type].apply(lambda x: f"{x*100:.1f}%"),
    )

    fig2.update_traces(marker_color=final_colors, textposition="outside")
    fig2.update_layout(
        title=f"🌐 {selected_type} 비율이 높은 국가 TOP 10 (+South Korea 강조)",
        xaxis_title="국가",
        yaxis_title="비율",
        template="simple_white",
        showlegend=False
    )

    st.plotly_chart(fig2, use_container_width=True)
