# pages/subway_analysis.py

import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.colors import get_colorscale, n_colors

# Streamlit 페이지 설정
st.set_page_config(layout="wide", page_title="지하철 일별/노선별 승하차 분석", initial_sidebar_state="expanded")

# --- 데이터 로드 및 전처리 함수 ---
@st.cache_data
def load_and_preprocess_data(file_path):
    """CSV 파일을 로드하고 전처리합니다."""
    try:
        # CP949 인코딩으로 시도 (Windows 환경에서 자주 사용되는 한글 인코딩)
        df = pd.read_csv(file_path, encoding='cp949')
    except UnicodeDecodeError:
        # 실패 시 EUC-KR로 시도
        df = pd.read_csv(file_path, encoding='euc-kr')
    except FileNotFoundError:
        st.error(f"⚠️ 파일 경로를 찾을 수 없습니다: {file_path}. 파일을 루트 폴더에 넣어주세요.")
        return pd.DataFrame()

    # 컬럼 이름 정리
    df.columns = ['사용일자', '노선명', '역명', '승차총승객수', '하차총승객수']

    # '사용일자'를 날짜 형식으로 변환
    df['사용일자'] = df['사용일자'].astype(str) # 먼저 문자열로 변환
    df['사용일자'] = pd.to_datetime(df['사용일자'], format='%Y%m%d')

    # '총승하차인원' 컬럼 생성
    df['총승하차인원'] = df['승차총승객수'] + df['하차총승객수']

    return df

# 파일 경로: 루트 폴더에 'subway.csv'가 있다고 가정
FILE_PATH = "subway.csv"
df = load_and_preprocess_data(FILE_PATH)

# 데이터 로드 성공 시에만 진행
if not df.empty:
    st.header("🚇 지하철 일별/노선별 승하차 분석 (2025년 10월)")
    st.markdown("---")

    # --- 사이드바 필터 설정 ---
    with st.sidebar:
        st.title("필터 선택")

        # 1. 날짜 선택 (2025년 11월 데이터는 없으므로 10월 데이터로 진행)
        # 데이터가 2025년 10월이므로, 해당 월의 날짜를 선택하도록 처리
        min_date = df['사용일자'].min().date()
        max_date = df['사용일자'].max().date()
        
        # 기본값으로 가장 최근 날짜를 설정
        selected_date = st.date_input(
            "📅 분석할 날짜를 선택하세요",
            value=max_date,
            min_value=min_date,
            max_value=max_date
        )
        
        # 2. 노선 선택
        available_lines = sorted(df['노선명'].unique().tolist())
        selected_line = st.selectbox(
            "🗺️ 분석할 노선을 선택하세요",
            options=available_lines
        )

    # --- 데이터 필터링 ---
    # 선택된 날짜와 노선으로 데이터 필터링
    filtered_df = df[
        (df['사용일자'].dt.date == selected_date) & 
        (df['노선명'] == selected_line)
    ].sort_values(by='총승하차인원', ascending=False).reset_index(drop=True)

    
    # --- 시각화 실행 ---
    if not filtered_df.empty:
        st.subheader(f"✅ {selected_date} **{selected_line}** 총 승하차 인원 순위")
        
        # 1. 랭킹 데이터 프레임 준비 (상위 50개만 표시하여 그래프 가독성 확보)
        rank_df = filtered_df.head(50)
        
        # 2. 색상 설정: 1위 빨간색, 나머지는 파란색 그라데이션
        # 파란색 그라데이션을 생성 (선두 빨간색 제외한 나머지 개수만큼)
        num_others = len(rank_df) - 1
        
        if num_others > 0:
            # Blues 색상 스케일에서 색상 추출 (진한 파랑->연한 파랑)
            blue_colors = n_colors('rgb(0, 0, 255)', 'rgb(173, 216, 230)', num_others, colortype='rgb')
            colors = ['rgb(255, 0, 0)'] + list(blue_colors) # 1위는 빨간색(Red)
        else:
            colors = ['rgb(255, 0, 0)'] # 데이터가 1개 이하일 경우

        # 3. Plotly 막대 그래프 생성 (인터랙티브)
        fig = px.bar(
            rank_df,
            x='역명',
            y='총승하차인원',
            title=f"{selected_date} {selected_line} 역별 총 승하차 인원",
            labels={'역명': '지하철 역명', '총승하차인원': '총 승하차 인원 (승차 + 하차)'},
            color=rank_df.index, # 색상을 인덱스 순서에 따라 매핑
            color_discrete_sequence=colors, # 사용자 정의 색상 적용
            hover_data=['승차총승객수', '하차총승객수'] # 마우스 오버 시 상세 정보 표시
        )
        
        # 그래프 레이아웃 커스터마이징
        fig.update_layout(
            xaxis={'categoryorder': 'total descending'}, # X축 순서를 Y값 기준으로 정렬
            hovermode="x unified",
            margin=dict(l=20, r=20, t=50, b=20)
        )
        
        # Streamlit에 그래프 표시
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("---")
        st.caption("ℹ️ 데이터 테이블")
        st.dataframe(rank_df[['역명', '총승하차인원', '승차총승객수', '하차총승객수']], use_container_width=True)

    else:
        st.warning(f"⚠️ **{selected_date}** 날짜에는 **{selected_line}** 노선의 데이터가 없습니다. 다른 날짜나 노선을 선택해 주세요.")

# --- 데이터 저작권 표시 (선택 사항)
st.sidebar.caption("데이터 출처: 서울시 교통정보 데이터")
