# streamlit_app.py
import streamlit as st
import pandas as pd
import plotly.express as px
import os
import traceback

st.set_page_config(page_title="세계 MBTI 비율 시각화 🌍", page_icon="🧠", layout="centered")

st.title("🌍 나라별 MBTI 비율 시각화")
st.markdown("국가를 선택하면 해당 나라의 MBTI 유형별 비율을 보여줍니다.")

DEBUG = os.getenv("DEBUG", "false").lower() in ("1", "true", "yes")

@st.cache_data
def load_data(path="countriesMBTI_16types.csv"):
    # 파일 존재 확인
    if not os.path.exists(path):
        raise FileNotFoundError(f"CSV 파일을 찾을 수 없습니다: {path}")
    # 읽기 시 인코딩 문제가 나면 utf-8-sig로 재시도
    try:
        df = pd.read_csv(path)
    except UnicodeDecodeError:
        df = pd.read_csv(path, encoding="utf-8-sig")
    return df

try:
    df = load_data()
except Exception as e:
    st.error("데이터 로드 중 오류가 발생했습니다.")
    st.exception(e)
    if DEBUG:
        st.text(traceback.format_exc())
    st.stop()

# 기본 검증
required_cols = {"Country"}
required_cols.update([  # 16 MBTI types 예상
    "INFJ","ISFJ","INTP","ISFP","ENTP","INFP","ENTJ","ISTP",
    "INTJ","ESFP","ESTJ","ENFP","ESTP","ISTJ","ENFJ","ESFJ"
])
missing = required_cols - set(df.columns)
if missing:
    st.error(f"CSV에 필요한 열이 누락되었습니다: {sorted(list(missing))}")
    st.stop()

# 사이드바: 디버그 토글(앱 실행 중간에도 확인용)
with st.sidebar:
    st.header("설정")
    debug_toggle = st.checkbox("디버그 모드 출력", value=DEBUG)
    if debug_toggle and not DEBUG:
        st.warning("디버그는 환경변수 DEBUG=true 또는 여기 체크로 활성화됩니다 (출력 제한).")

# 국가 선택 UI
country_list = sorted(df["Country"].dropna().unique().tolist())
if len(country_list) == 0:
    st.error("Country 열에 값이 없습니다.")
    st.stop()

selected_country = st.selectbox("국가를 선택하세요 🌎", country_list)

# 안전하게 행 추출
country_rows = df[df["Country"] == selected_country]
if country_rows.empty:
    st.error(f"선택한 국가({selected_country})의 데이터가 없습니다.")
    st.stop()

# MBTI 컬럼만 추출 (Country 제외)
mbti_cols = [c for c in df.columns if c != "Country"]
country_series = country_rows.iloc[0][mbti_cols]

# 숫자가 아닌 값이 있으면 변환 시도
try:
    country_series = pd.to_numeric(country_series)
except Exception:
    # 변환 안되면 에러 표시
    st.error("해당 국가의 MBTI 컬럼 중 숫자로 변환할 수 없는 값이 있습니다.")
    st.write(country_series)
    st.stop()

country_df = (
    country_series.rename("비율")
    .reset_index()
    .rename(columns={"index": "MBTI"})
    .sort_values("비율", ascending=False)
    .reset_index(drop=True)
)

# 안전: 비율 합계 체크 (100% 근처인지)
total = country_df["비율"].sum()
st.write(f"선택한 국가: **{selected_country}** — 비율 합계: {total:.4f}")
if not (0.95 <= total <= 1.05):
    st.info("비율 합계가 1(100%)에서 많이 벗어나면 데이터 스케일이 다를 수 있습니다. (예: 이미 %*100 되어있음)")

# 색상 생성 (1위 빨강, 나머지는 파란 그라데이션)
top_mbti = country_df.loc[0, "MBTI"]
n = len(country_df)
colors = []
# 색상 불변 포맷 사용 (hex for 1위, rgba for 그라데이션)
for rank, mbti in enumerate(country_df["MBTI"], start=1):
    if mbti == top_mbti:
        colors.append("#FF3B30")  # 강한 빨강
    else:
        # rank 2..n -> opacity 감소 (0.9 -> 0.3)
        # rank normalized: (rank-1)/(n-1) in [0,1]
        if n > 1:
            norm = (rank-1) / (n-1)
        else:
            norm = 0
        opacity = 0.9 - 0.6 * norm
        colors.append(f"rgba(0,102,255,{opacity:.3f})")

# Plotly 그래프 생성
try:
    fig = px.bar(
        country_df,
        x="MBTI",
        y="비율",
        text=country_df["비율"].apply(lambda x: f"{x*100:.1f}%" if x<=1.5 else f"{x:.1f}"),
        labels={"비율": "비율"},
    )
    fig.update_traces(marker_color=colors, textposition="outside",
                      hovertemplate="<b>%{x}</b><br>비율: %{y:.4f}<extra></extra>")
    fig.update_layout(
        title=dict(text=f"{selected_country}의 MBTI 비율", x=0.5),
        xaxis_title="MBTI 유형",
        yaxis_title="비율 (0-1 또는 스케일된 값)",
        template="simple_white",
        showlegend=False,
        margin=dict(l=40, r=40, t=80, b=40),
    )
    # y축이 0..1일 때 %틱 표시
    if country_df["비율"].max() <= 1.0:
        fig.update_yaxes(tickformat=".0%")
except Exception as e:
    st.error("그래프 생성 중 오류가 발생했습니다.")
    st.exception(e)
    if debug_toggle:
        st.text(traceback.format_exc())
    st.stop()

st.plotly_chart(fig, use_container_width=True)

# 디버그 출력 (선택 시)
if debug_toggle:
    st.markdown("### 디버그: 선택한 국가 Raw 데이터")
    st.write(country_rows)
    st.markdown("### 디버그: country_df (정렬된 비율)")
    st.write(country_df)
