import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Seoul Top 10 Attractions", page_icon="🌆", layout="wide")

st.title("🌆 외국인이 좋아하는 서울 관광지 TOP 10")
st.write("서울의 대표 명소를 지도로 한눈에 볼 수 있어요! 📍")

# 관광지 데이터 (이름, 설명, 좌표)
locations = [
    {"name": "경복궁 (Gyeongbokgung Palace)", 
     "desc": "조선시대의 중심 궁궐로, 한국 전통 건축의 아름다움을 느낄 수 있어요.", 
     "lat": 37.579617, "lon": 126.977041},
    {"name": "명동 (Myeongdong Shopping Street)", 
     "desc": "외국인에게 가장 인기 있는 쇼핑 거리로, 맛집과 패션 브랜드가 가득해요!", 
     "lat": 37.563757, "lon": 126.982703},
    {"name": "남산타워 (N Seoul Tower)", 
     "desc": "서울의 전경을 한눈에 볼 수 있는 랜드마크! 야경이 특히 아름답답니다 💫", 
     "lat": 37.551169, "lon": 126.988227},
    {"name": "북촌한옥마을 (Bukchon Hanok Village)", 
     "desc": "전통 한옥이 모여 있는 예쁜 마을로, 사진 명소로 유명해요 📸", 
     "lat": 37.582604, "lon": 126.983998},
    {"name": "인사동 (Insadong)", 
     "desc": "전통 공예품, 찻집, 갤러리가 가득한 문화 거리 🎨", 
     "lat": 37.574034, "lon": 126.984980},
    {"name": "홍대 (Hongdae)", 
     "desc": "젊음과 예술의 거리! 거리공연, 카페, 쇼핑이 모두 한곳에 🎶", 
     "lat": 37.556327, "lon": 126.922951},
    {"name": "동대문디자인플라자 (DDP)", 
     "desc": "독특한 건축물과 야시장으로 유명한 서울의 디자인 중심지 💡", 
     "lat": 37.566536, "lon": 127.009050},
    {"name": "롯데월드타워 (Lotte World Tower)", 
     "desc": "555m 높이의 초고층 빌딩! 전망대와 쇼핑몰, 아쿠아리움까지 한 번에 🏙️", 
     "lat": 37.513068, "lon": 127.102493},
    {"name": "남대문시장 (Namdaemun Market)", 
     "desc": "서울에서 가장 오래된 전통시장! 먹거리와 쇼핑 천국 🍜", 
     "lat": 37.559642, "lon": 126.978149},
    {"name": "청계천 (Cheonggyecheon Stream)", 
     "desc": "도심 속 시원한 휴식 공간 🌊 산책하기 딱 좋아요!", 
     "lat": 37.570176, "lon": 126.979480}
]

# 지도 생성
m = folium.Map(location=[37.5665, 126.9780], zoom_start=12)

# 마커 표시
for loc in locations:
    folium.Marker(
        location=[loc["lat"], loc["lon"]],
        popup=f"<b>{loc['name']}</b><br>{loc['desc']}",
        tooltip=loc["name"],
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)

# 지도 출력
st_data = st_folium(m, width=1200, height=600)
