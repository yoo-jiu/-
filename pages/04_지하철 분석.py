import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date

# 1. 페이지 기본 설정
# ------------------------------------
st.set_page_config(
    page_title="서울 지하철 승하차 순위 분석",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.title("🚇 지하철 역별 혼잡도 분석 (2025년 10월 데이터)")
st.markdown("---")

# 2. 데이터 로드 함수 (캐싱)
# ------------------------------------
@st.cache_data
def load_data(file_path):
    """CSV 파일을 로드하고 필요한 전처리 수행"""
    try:
        # 실제 파일명 사용 및 인코딩 지정
        df = pd.read_csv(file_path, encoding='utf-8')

        # 컬럼명 변경: '노선명' -> '호선명', '역명' -> '지하철역'
        df.rename(columns={
            '노선명': '호선명', 
            '역명': '지하철역'
        }, inplace=True)

        # '사용일자' 컬럼을 datetime 객체로 변환 (형식: YYYYMMDD)
        df['사용일자'] = pd.to_datetime(df['사용일자'], format='%Y%m%d', errors='coerce')
        df = df.dropna(subset=['사용일자']) 

        # 2025년 11월 데이터만 사용하는 요청에 맞춰, 데이터에서 사용 가능한 '월'을 추출
        available_months = sorted(df['사용일자'].dt.to_period('M').unique().tolist(), reverse=True)
        
        # 2025년 11월에 해당하는 날짜만 필터링
        # (제공된 데이터가 2025년 10월이므로, 11월에 해당하는 데이터가 없으면 오류가 발생하므로, 
        # 일단 10월 데이터 전체를 사용하고, 11월 날짜는 임의로 설정하는 로직을 유지하거나, 
        # 실제 데이터의 날짜 범위 내에서 선택하도록 수정합니다. 여기서는 **10월 데이터 내에서 선택**하도록 수정)
        
        # 필요한 컬럼 타입 변환
        df['승차총승객수'] = pd.to_numeric(df['승차총승객수'], errors='coerce').fillna(0).astype(int)
        df['하차총승객수'] = pd.to_numeric(df['하차총승객수'], errors='coerce').fillna(0).astype(int)

        # 총 승하차 인원 합산 컬럼 생성
        df['총_승하차수'] = df['승차총승객수'] + df['하차총승객수']

        # '호선명'을 기준으로 필터링을 위한 고유 호선 목록 추출
        lines = sorted(df['호선명'].unique().tolist())
        
        return df, lines
    
    except FileNotFoundError:
        st.error(f"⚠️ **에러 발생!** 루트 폴더에 '{file_path}' 파일을 찾을 수 없습니다. 파일을 확인해주세요.")
        return pd.DataFrame(), []
    except Exception as e:
        st.error(f"데이터 로드 및 처리 중 에러가 발생했습니다: {e}")
        return pd.DataFrame(), []


# 3. 사이드바 사용자 입력
# ------------------------------------
DATA_FILE = "subway.csv" # 실제 업로드된 파일명 사용
df_all, lines_list = load_data(DATA_FILE)

selected_date = None
selected_line = None

if not df_all.empty:
    
    # 데이터에 포함된 사용 가능한 날짜 목록
    available_dates = sorted(df_all['사용일자'].dt.date.unique().tolist())
    
    with st.sidebar:
        st.header("📊 분석 조건 설정")

        # 1) 날짜 선택 (데이터의 실제 날짜 범위 내에서 선택)
        # 요청은 11월이었지만, 실제 데이터는 10월이므로 10월 날짜를 보여줍니다.
        st.caption(f"ℹ️ 업로드된 데이터({available_dates[0]} ~ {available_dates[-1]} 범위)에서 선택해주세요.")
        
        # 가장 최근 날짜를 기본값으로 설정
        default_index = len(available_dates) - 1
        
        selected_date = st.selectbox(
            "📅 **분석할 날짜를 선택해주세요:**",
            options=available_dates,
            index=default_index
        )

        # 2) 호선 선택
        selected_line = st.selectbox(
            "🚉 **분석할 호선을 선택해주세요:**",
            options=lines_list
        )

# 4. 데이터 필터링 및 집계
# ------------------------------------
if not df_all.empty and selected_date and selected_line:
    
    # 선택된 날짜와 호선으로 필터링
    df_filtered = df_all[
        (df_all['사용일자'].dt.date == selected_date) & 
        (df_all['호선명'] == selected_line)
    ].copy() 

    # 역별로 총 승하차수 집계
    df_rank = df_filtered.groupby('지하철역')['총_승하차수'].sum().reset_index()
    df_rank = df_rank.sort_values(by='총_승하차수', ascending=False)
    
    # 5. 플로틀리 막대 그래프 생성 (인터랙티브 + 색상 그라데이션)
    # -----------------------------------------------------------
    
    if df_rank.empty:
        st.warning(f"선택하신 날짜({selected_date})와 호선({selected_line})에 해당하는 데이터가 없습니다.")
    else:
        st.subheader(f"🥇 {selected_date} '{selected_line}' 승하차 총합 순위")
        
        # Plotly 그라데이션 색상 설정
        n_bars = len(df_rank)
        
        # 1등은 빨간색
        final_colors = ['red']
        
        # 2등부터는 파란색 계열의 그라데이션 적용
        if n_bars > 1:
            n_other_bars = n_bars - 1
            # Plotly의 Blues 팔레트에서 N-1개 색상을 추출 (옅은 파랑부터 진한 파랑으로)
            blue_gradient = px.colors.sequential.Blues
            
            if n_other_bars > 1:
                # 색상 스케일에서 N-1개 샘플링
                step = len(blue_gradient) // n_other_bars 
                # 파란색 계열을 2등부터 꼴찌까지 차례대로 적용 (진해지는 방향)
                other_colors = [blue_gradient[i * step] for i in range(n_other_bars)]
            else:
                 # 2위 하나만 있는 경우, 중간 파란색 계열 지정
                 other_colors = [blue_gradient[len(blue_gradient) // 2]] 
                 
            final_colors.extend(other_colors)
            
        # 막대 그래프 (Plotly Express)
        fig = px.bar(
            df_rank,
            x='지하철역',
            y='총_승하차수',
            title=f"**{selected_date} {selected_line}** 역별 총 승하차객 수",
            labels={'지하철역': '지하철 역명', '총_승하차수': '총 승하차객 수 (명)'},
            # 색상을 막대별로 지정하기 위해 '지하철역'을 color로 사용 후, color_discrete_map 지정
            color='지하철역', 
            color_discrete_map={
                station: color for station, color in zip(df_rank['지하철역'], final_colors)
            },
            height=600
        )
        
        # 그래프 레이아웃 및 툴팁 커스터마이징
        fig.update_layout(
            xaxis_title=None,
            yaxis_title='총 승하차객 수',
            hovermode="x unified",
        )
        
        fig.update_traces(
            hovertemplate="<b>%{x}</b><br>총 승하차수: %{y:,}명<extra></extra>"
        )

        # Plotly 그래프를 스트림릿에 표시
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("---")
        st.subheader("📚 상위 10개 역 상세 데이터")
        # 상위 10개 데이터를 표로도 보여줍니다.
        st.dataframe(df_rank.head(10).style.format({'총_승하차수': "{:,}"}), use_container_width=True)

# 6. 참고 사항 안내 (데이터가 없을 경우)
# ------------------------------------
else:
    if df_all.empty:
        st.info("데이터 로드에 문제가 발생했습니다. 파일명('subway.csv')과 파일 구조를 확인해주세요.")
