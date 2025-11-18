with tab2:

    mbti_type = st.selectbox("MBTI 유형을 선택하세요:", df.columns[1:])

    sorted_df = df.sort_values(by=mbti_type, ascending=False)
    top10 = sorted_df.head(10).copy()

    # South Korea 자동 포함
    if "South Korea" not in top10["Country"].values:
        sk = df[df["Country"] == "South Korea"]
        if not sk.empty:
            top10 = pd.concat([top10, sk], ignore_index=True)

    # 🔵 진한 파랑 → 적당히 연한 파랑 (너무 연해지지 않게 설정)
    # alpha 값: 0.90 → 0.55
    gradient_blue = [
        f"rgba(0, 60, 255, {0.90 - i*0.035})"
        for i in range(len(top10))
    ]

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
