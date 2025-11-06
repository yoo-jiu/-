import streamlit as st

st.set_page_config(page_title="MBTI 책 & 영화 추천 💫", page_icon="🎬")

st.title("💫 MBTI별 책 & 영화 추천 💫")
st.write("안녕! 😄 너의 MBTI를 알려주면 찰떡같이 어울리는 책이랑 영화 추천해줄게 🎥📚")

mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

user_mbti = st.selectbox("너의 MBTI를 골라줘 👇", mbti_list)

# 모든 MBTI별 데이터
recommendations = {
    "INTJ": {
        "books": [
            ("이기적 유전자 - 리처드 도킨스", "논리와 통찰을 중시하는 INTJ에게 어울리는 진화론 명저 🧬"),
            ("1984 - 조지 오웰", "권력과 감시 속 인간의 자유를 그린 고전적인 문제작 🔍")
        ],
        "movies": [
            ("인셉션", "꿈속의 세계를 설계하는 천재들의 이야기. 복잡하지만 완벽한 논리 구조! 🌀",
             "https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg"),
            ("인터스텔라", "시간, 우주, 사랑까지 모두 계산 가능한 SF 명작 🚀",
             "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg")
        ]
    },
    "INTP": {
        "books": [
            ("코스모스 - 칼 세이건", "호기심 넘치는 INTP에게 완벽한 과학 명저 🌌"),
            ("수학자의 낙서장 - 폴 로크하트", "수학과 창의력을 함께 즐길 수 있는 철학적 책 ✏️")
        ],
        "movies": [
            ("그녀 (Her)", "AI와 인간의 감정 교류를 다룬 독특한 SF 영화 💻❤️",
             "https://upload.wikimedia.org/wikipedia/en/4/44/Her2013Poster.jpg"),
            ("매트릭스", "현실이란 무엇인가? 철학적 고민 가득한 액션 걸작 🕶️",
             "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg")
        ]
    },
    "ENTJ": {
        "books": [
            ("원씽 - 게리 켈러", "목표 달성에 집중하는 리더형 ENTJ에게 딱이야 💪"),
            ("승자의 공부 - 짐 콜린스", "성공 전략을 과학적으로 분석한 비즈니스 필독서 📈")
        ],
        "movies": [
            ("다크 나이트", "혼란 속에서도 질서를 세우는 리더의 고뇌 🦇",
             "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg"),
            ("글래디에이터", "리더십과 용기의 진수를 보여주는 전설적인 영화 ⚔️",
             "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg")
        ]
    },
    "ENTP": {
        "books": [
            ("부의 인문학 - 브라운스톤", "아이디어와 전략을 좋아하는 ENTP에게 어울리는 경제 인문서 💡"),
            ("호밀밭의 파수꾼 - J.D. 샐린저", "세상에 도전하는 자유로운 영혼의 이야기 🙃")
        ],
        "movies": [
            ("아이언맨", "창의력 폭발! 천재 발명가의 화려한 모험 🤖",
             "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG"),
            ("캐치 미 이프 유 캔", "머리 좋은 사기꾼의 유쾌한 추격전 🎭",
             "https://upload.wikimedia.org/wikipedia/en/9/9c/Catch_Me_If_You_Can_2002_movie.jpg")
        ]
    },
    "INFJ": {
        "books": [
            ("데미안 - 헤르만 헤세", "자기 탐색과 성장을 그린 철학적 성장소설 🌙"),
            ("연금술사 - 파울로 코엘료", "삶의 의미를 찾는 여정, INFJ에게 찰떡 ✨")
        ],
        "movies": [
            ("어톤먼트", "사랑과 죄책감, 그리고 용서에 대한 섬세한 드라마 💔",
             "https://upload.wikimedia.org/wikipedia/en/6/6b/Atonement_UK_poster.jpg"),
            ("월-E", "고요하지만 따뜻한 메시지를 전하는 로봇의 사랑 이야기 🤖💞",
             "https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg")
        ]
    },
    "INFP": {
        "books": [
            ("모모 - 미하엘 엔데", "시간을 훔치는 세상에 맞서는 순수한 영혼 💕"),
            ("작별하지 않는다 - 한강", "기억과 아픔을 섬세하게 그린 감성 소설 🌧️")
        ],
        "movies": [
            ("어바웃 타임", "시간을 거슬러 진짜 사랑을 찾아가는 따뜻한 이야기 ⏳❤️",
             "https://upload.wikimedia.org/wikipedia/en/1/16/About_Time_poster.jpg"),
            ("이터널 선샤인", "기억을 지워도 남는 감정, 감성 폭발 🎈",
             "https://upload.wikimedia.org/wikipedia/en/6/62/Eternal_Sunshine_of_the_Spotless_Mind_poster.jpg")
        ]
    },
    "ENFJ": {
        "books": [
            ("사람은 어떻게 성장하는가 - 로버트 케이건", "사람을 이끄는 리더에게 필요한 깊은 통찰 🌱"),
            ("미움받을 용기 - 기시미 이치로", "다른 사람을 이해하고 나를 성장시키는 책 💫")
        ],
        "movies": [
            ("굿 윌 헌팅", "재능과 상처를 가진 청년을 감싸주는 따뜻한 이야기 🍀",
             "https://upload.wikimedia.org/wikipedia/en/5/52/Good_Will_Hunting.png"),
            ("인턴", "세대 차이를 넘어 협력과 배움을 보여주는 훈훈한 영화 👔",
             "https://upload.wikimedia.org/wikipedia/en/c/c9/The_Intern_poster.jpg")
        ]
    },
    "ENFP": {
        "books": [
            ("연금술사 - 파울로 코엘료", "자신의 꿈을 찾아 떠나는 여행 ✨"),
            ("달러구트 꿈 백화점 - 이미예", "꿈을 사고파는 따뜻한 판타지 🌙")
        ],
        "movies": [
            ("인사이드 아웃", "감정의 세계를 모험하는 밝고 따뜻한 이야기 🎨",
             "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg"),
            ("라라랜드", "꿈과 사랑 사이에서 흔들리는 두 사람의 이야기 🎶💛",
             "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png")
        ]
    },
    "ISTJ": {
        "books": [
            ("총, 균, 쇠 - 재레드 다이아몬드", "논리와 사실을 중시하는 ISTJ에게 찰떡 역사서 📘"),
            ("7가지 습관 - 스티븐 코비", "체계적이고 실용적인 자기계발서 📋")
        ],
        "movies": [
            ("쉰들러 리스트", "책임감과 정의감을 가진 사람의 진짜 용기 🕊️",
             "https://upload.wikimedia.org/wikipedia/en/3/38/Schindler%27s_List_movie.jpg"),
            ("캐스트 어웨이", "혼자서도 끝까지 해내는 생존의 의지 💪🏝️",
             "https://upload.wikimedia.org/wikipedia/en/a/a7/Cast_away_film_poster.jpg")
        ]
    },
    "ISFJ": {
        "books": [
            ("작은 아씨들 - 루이자 메이 올컷", "따뜻한 가족애와 성장을 그린 이야기 🩵"),
            ("나미야 잡화점의 기적 - 히가시노 게이고", "사람들의 고민을 해결해주는 마법 같은 이야기 🌟")
        ],
        "movies": [
            ("원더", "다름을 이해하고 포용하는 감동적인 가족 영화 🌈",
             "https://upload.wikimedia.org/wikipedia/en/0/0e/Wonder_%28film%29.png"),
            ("업", "잃어버린 꿈을 다시 찾아가는 여정 🎈",
             "https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg")
        ]
    },
    "ESTJ": {
        "books": [
            ("원씽 - 게리 켈러", "효율과 집중을 중시하는 ESTJ에게 딱! 💼"),
            ("성공하는 사람들의 7가지 습관 - 스티븐 코비", "리더십과 실천력의 정석 📊")
        ],
        "movies": [
            ("머니볼", "데이터와 전략으로 세상을 바꾸는 이야기 ⚾",
             "https://upload.wikimedia.org/wikipedia/en/2/2e/Moneyball_Poster.jpg"),
            ("더 울프 오브 월스트리트", "목표를 향한 폭발적인 추진력 💸",
             "https://upload.wikimedia.org/wikipedia/en/f/fc/The_Wolf_of_Wall_Street_%282013%29.png")
        ]
    },
    "ESFJ": {
        "books": [
            ("오베라는 남자 - 프레드릭 배크만", "까칠하지만 따뜻한 사람들의 이야기 😊"),
            ("해리포터와 마법사의 돌 - J.K. 롤링", "우정과 용기가 가득한 모험 🪄")
        ],
        "movies": [
            ("코코", "가족의 사랑과 음악의 힘을 전하는 감동 애니메이션 🎵",
             "https://upload.wikimedia.org/wikipedia/en/9/9f/Coco_%282017_film%29.png"),
            ("노트북", "사랑의 진심을 보여주는 클래식 로맨스 💌",
             "https://upload.wikimedia.org/wikipedia/en/8/86/Posternotebook.jpg")
        ]
    },
    "ISTP": {
        "books": [
            ("호밀밭의 파수꾼 - J.D. 샐린저", "냉소적이지만 진심을 숨기지 못하는 청춘의 이야기 🙃"),
            ("인간 실격 - 다자이 오사무", "세상과 어긋난 한 인간의 내면을 솔직하게 그린 소설 🖤")
        ],
        "movies": [
            ("매드맥스: 분노의 도로", "거칠고 시원한 액션이 가득한 생존의 질주 🏎️💨",
             "https://upload.wikimedia.org/wikipedia/en/6/6e/Mad_Max_Fury_Road.jpg"),
            ("존 윅", "심플하지만 강렬한 액션, 네 스타일일걸? 🔫",
             "https://upload.wikimedia.org/wikipedia/en/9/98/John_Wick_TeaserPoster.jpg")
        ]
    },
    "ISFP": {
        "books": [
            ("보통의 존재 - 이석원", "잔잔하고 솔직한 일상의 감정들을 담은 에세이 🌿"),
            ("나의 라임오렌지나무 - J.M. 바스콘셀로스", "순수한 소년의 성장 이야기 🍊")
        ],
        "movies": [
            ("비긴 어게인", "음악으로 위로받는 사람들의 따뜻한 이야기 🎸",
             "https://upload.wikimedia.org/wikipedia/en/b/bd/Begin_Again_film_poster_2014.jpg"),
            ("리틀 포레스트", "자연과 함께 살아가는 힐링 무드 🍃",
             "https://upload.wikimedia.org/wikipedia/en/b/b2/Little_Forest_%28film%29.png")
        ]
    },
    "ESTP": {
        "books": [
            ("부의 추월차선 - 엠제이 드마코", "빠르게 성공하고 싶은 ESTP에게 딱 💰"),
            ("도둑맞은 집중력 - 요한 하리", "현실적인 문제를 빠르게 파악하고 해결하는 통찰서 🔍")
        ],
        "movies": [
            ("분노의 질주", "스피드와 액션, 그리고 팀워크! 🏁",
             "https://upload.wikimedia.org/wikipedia/en/8/8f/Fast_%26_Furious_Poster.jpg"),
            ("킹스맨", "유머와 액션이 절묘하게 어우러진 스파이 무비 🕶️",
             "https://upload.wikimedia.org/wikipedia/en/6/6b/Kingsman_The_Secret_Service_poster.jpg")
        ]
    },
    "ESFP": {
        "books": [
            ("언어의 온도 - 이기주", "감성적이고 따뜻한 표현이 가득한 책 💕"),
            ("내가 한 말을 내가 믿지 않기 시작했다 - 이병률", "감정 풍부한 시와 문장들 ✨")
        ],
        "movies": [
            ("맘마미아!", "음악과 사랑, 긍정 에너지 가득한 뮤지컬 🎤🌴",
             "https://upload.wikimedia.org/wikipedia/en/7/7b/MammaMiaTeaserPoster.jpg"),
            ("더 그레이티스트 쇼맨", "자신만의 무대를 만드는 열정과 감동 🎪",
             "https://upload.wikimedia.org/wikipedia/en/1/10/The_Greatest_Showman_poster.png")
        ]
    },
}

# 출력
if user_mbti:
    data = recommendations.get(user_mbti)
    st.subheader("📚 너에게 어울리는 책 추천!")
    for title, desc in data["books"]:
        st.markdown(f"**{title}** — {desc}")

    st.subheader("🎬 너에게 어울리는 영화 추천!")
    for title, desc, poster in data["movies"]:
        st.markdown(f"**{title}** — {desc}")
        st.image(poster, width=250)
