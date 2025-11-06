import streamlit as st

# 앱 제목
st.title("💫 MBTI별 책 & 영화 추천 앱 💫")
st.write("안녕! 😄 너의 MBTI를 알려주면 너한테 딱 맞는 책이랑 영화 추천해줄게 🎥📖")

# MBTI 목록
mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# 사용자 입력
user_mbti = st.selectbox("너의 MBTI를 골라줘 👇", mbti_list)

# MBTI별 추천 데이터
recommendations = {
    "INFP": {
        "books": [
            ("작별하지 않는다 - 한강", "섬마을에서 일어난 비극을 통해 인간의 기억과 상처를 그린 소설이야."),
            ("모모 - 미하엘 엔데", "시간을 훔치는 회색 신사들에게 맞서는 소녀 모모의 따뜻한 이야기 💕")
        ],
        "movies": [
            ("월-E (WALL-E)", "지구가 버려진 미래, 외로운 로봇 월-E가 사랑을 찾아가는 감동적인 이야기 🌍"),
            ("어바웃 타임 (About Time)", "시간여행 능력을 가진 남자가 진짜 사랑을 찾아가는 달콤한 로맨스 ⏳💞"),
        ]
    },
    "INTJ": {
        "books": [
            ("이기적 유전자 - 리처드 도킨스", "인간 행동을 진화의 관점에서 바라보는 흥미로운 과학서야 🧬"),
            ("1984 - 조지 오웰", "감시 사회 속에서 자유를 갈망하는 인간의 모습을 그린 명작이야 🔍")
        ],
        "movies": [
            ("인셉션 (Inception)", "꿈속의 꿈을 다루는 천재적인 스릴러! 복잡하지만 논리적인 네 스타일 😎"),
            ("인터스텔라 (Interstellar)", "우주와 시간, 사랑의 힘까지 모두 담은 감동적인 SF 걸작 🚀"),
        ]
    },
    "ENFP": {
        "books": [
            ("연금술사 - 파울로 코엘료", "자신의 꿈을 찾아 떠나는 청년의 여정 ✨ 네가 좋아할 모험이야!"),
            ("달러구트 꿈 백화점 - 이미예", "사람들이 ‘꿈’을 사고파는 따뜻한 판타지 🌙")
        ],
        "movies": [
            ("인사이드 아웃 (Inside Out)", "감정들이 주인공! 감정의 세계를 모험하는 감동 애니메이션 🎨"),
            ("라라랜드 (La La Land)", "꿈과 사랑 사이에서 흔들리는 두 사람의 뮤지컬 로맨스 🎶💛"),
        ]
    },
    "ISTP": {
        "books": [
            ("호밀밭의 파수꾼 - J.D. 샐린저", "냉소적이지만 진심을 숨기지 못하는 청춘의 이야기 🙃"),
            ("인간 실격 - 다자이 오사무", "세상과 어긋난 한 인간의 내면을 솔직하게 그린 소설 🖤")
        ],
        "movies": [
            ("매드맥스: 분노의 도로 (Mad Max: Fury Road)", "거칠고 시원한 액션이 가득한 생존의 질주 🏎️💨"),
            ("존 윅 (John Wick)", "심플하지만 강렬한 액션, 네 스타일일걸? 🔫"),
        ]
    },
}

# 추천 결과 표시
if user_mbti:
    data = recommendations.get(user_mbti, None)
    if data:
        st.subheader("📚 너에게 어울리는 책 추천!")
        for title, desc in data["books"]:
            st.markdown(f"**{title}** — {desc}")

        st.subheader("🎬 너에게 어울리는 영화 추천!")
        for title, desc in data["movies"]:
            st.markdown(f"**{title}** — {desc}")
    else:
        st.write("앗, 아직 그 MBTI에 대한 추천이 준비 중이야 😅 곧 업데이트할게!")
