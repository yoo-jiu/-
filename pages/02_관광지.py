import streamlit as st
import folium
from streamlit_folium import st_folium
import math

st.set_page_config(page_title="Seoul Travel Planner", page_icon="🌆", layout="wide")

st.title("🌆 외국인이 좋아하는 서울 관광지 TOP 10")
st.write("서울의 대표 명소, 가까운 지하철역, 맛집, 그리고 일정까지 한눈에! 🚇🍜")

# 관광지 데이터
locations = [
    {"name": "경복궁 (Gyeongbokgung Palace)", 
     "desc": "조선시대의 중심 궁궐로, 한국 전통 건축의 아름다움을 느낄 수 있어요.", 
     "lat": 37.579617, "lon": 126.977041,
     "station": "3호선 경복궁역", "restaurant": "🍗 토속촌 삼계탕"},
    {"name": "명동 (Myeongdong Shopping Street)", 
     "desc": "외국인에게 가장 인기 있는 쇼핑 거리로, 맛집과 패션 브랜드가 가득해요!", 
     "lat": 37.563757, "lon": 126.982703,
     "station": "4호선 명동역", "restaurant": "🥟 명동교자 (칼국수)"},
    {"name": "남산타워 (N Seoul Tower)", 
     "desc": "서울의 전경을 한눈에 볼 수 있는 랜드마크! 야경이 특히 아름답답니다 💫", 
     "lat": 37.551169, "lon": 126.988227,
     "station": "4호선 명동역", "restaurant": "🍖 남산 돈까스거리"},
    {"name": "북촌한옥마을 (Bukchon Hanok Village)", 
     "desc": "전통 한옥이 모여 있는 예쁜 마을로, 사진 명소로 유명해요 📸", 
     "lat": 37.582604, "lon": 126.983998,
     "station": "3호선 안국역", "restaurant": "🍵 카페 온 (전통차)"},
    {"name": "인사동 (Insadong)", 
     "desc": "전통 공예품, 찻집, 갤러리가 가득한 문화 거리 🎨", 
     "lat": 37.574034, "lon": 126.984980,
     "station": "3호선 안국역", "restaurant": "🍱 오세계향 (비건 한식)"},
    {"name": "홍대 (Hongdae)", 
     "desc": "젊음과 예술의 거리! 거리공연, 카페, 쇼핑이 모두 한곳에 🎶", 
     "lat": 37.556327, "lon": 126.922951,
     "station": "2호선 홍대입구역", "restaurant": "🍔 망원동 티라미수 카페"},
    {"name": "동대문디자인플라자 (DDP)", 
     "desc": "독특한 건축물과 야시장으로 유명한 서울의 디자인 중심지 💡", 
     "lat": 37.566536, "lon": 127.009050,
     "station": "2·4·5호선 동대문역사문화공원역", "restaurant": "🥘 진주식당 (불고기)"},
    {"name": "롯데월드타워 (Lotte World Tower)", 
     "desc": "555m 높이의 초고층 빌딩! 전망대와 쇼핑몰, 아쿠아리움까지 한 번에 🏙️", 
     "lat": 37.513068, "lon": 127.102493,
     "station": "2·8호선 잠실역", "restaurant": "🍣 스시효 잠실점"},
    {"name": "남대문시장 (Namdaemun Market)", 
     "desc": "서울에서 가장 오래된 전통시장! 먹거리와 쇼핑 천국 🍜", 
     "lat": 37.559642, "lon": 126.978149,
     "station": "4호선 회현역", "restaurant": "🍲 우래옥 (평양냉면)"},
    {"name": "청계천 (Cheonggyecheon Stream)", 
     "desc": "도심 속 시원한 휴식 공간 🌊 산책하기 딱 좋아요!", 
     "lat": 37.570176, "lon": 126.979480,
     "station": "5호선 광화문역", "restaurant": "☕ 광화문 미진 (메밀국수)"}
]

# 지도 생성
m = folium.Map(location=[37.5665, 126.9780], zoom_start=12)

for loc in locations:
    popup_html = f"<b>{loc['name']}</b><br>{loc['desc']}<br><i>🚇 {loc['station']}</i><br>{loc['restaurant']}"
    folium.Marker(
        location=[loc["lat"], loc["lon"]],
        popup=popup_html,
        tooltip=loc["name"],
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)

# 지도 표시
st_folium(m, width=840, height=420)

st.markdown("---")
st.subheader("📖 관광지 상세 정보")

for i, loc in enumerate(locations, 1):
    with st.container():
        st.markdown(
            f"""
            <div style='background-color:#f9f9f9;padding:15px;border-radius:12px;margin-bottom:10px;
                        box-shadow:2px 2px 5px #ddd;'>
                <b>{i}. {loc['name']}</b><br>
                <span style='color:#444;'>{loc['desc']}</span><br>
                <span style='color:#666;'>🚇 {loc['station']}</span><br>
                <span style='color:#888;'>{loc['restaurant']}</span>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("---")
st.subheader("🗓️ 여행 일정 만들기")

days = st.slider("여행할 일수를 선택하세요 (1~3일)", 1, 3, 2)
st.write(f"👉 {days}일 동안 서울을 여행하는 일정이에요!")

# 일정 자동 분배
places_per_day = math.ceil(len(locations) / days)

# 기본 시간대
time_slots = ["09:30", "11:00", "12:30(점심)", "14:00", "16:00", "18:30(저녁)", "20:00"]

st.markdown("### ✨ 추천 일정 (시간 + 맛집 포함)")
for day in range(days):
    start = day * places_per_day
    end = start + places_per_day
    daily_plan = locations[start:end]

    st.markdown(f"#### 🗓️ Day {day+1}")
    for i, loc in enumerate(daily_plan):
        time = time_slots[i % len(time_slots)]
        if "점심" in time or "저녁" in time:
            st.markdown(f"- ⏰ **{time}** — 🍽️ 식사: {loc['restaurant']} ({loc['station']})")
        else:
            st.markdown(f"- ⏰ **{time}** — 🏞️ 방문: **{loc['name']}** ({loc['station']}) — {loc['desc']}")
    st.markdown("---")
