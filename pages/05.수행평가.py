import streamlit as st

st.set_page_config(page_title="MBTI 일본 노래 추천", layout="centered")

st.title("🎧 MBTI로 고르는 일본 노래 + 썸네일 + 하이라이트 요약")
st.write("MBTI 성향에 맞는 유명 일본 노래와 보컬로이드 추천, YouTube 공식 썸네일, 하이라이트 의미 요약까지 제공합니다!")

MBTI_TYPES = [
    "ISTJ","ISFJ","INFJ","INTJ",
    "ISTP","ISFP","INFP","INTP",
    "ESTP","ESFP","ENFP","ENTP",
    "ESTJ","ESFJ","ENFJ","ENTJ"
]

# 유튜브 링크 → 썸네일 URL 추출 함수
def get_thumbnail(url):
    # e.g. https://www.youtube.com/watch?v=XqZsoesa55w
    # 또는 https://youtu.be/XqZsoesa55w
    import re
    patterns = [
        r"v=([^&]+)",
        r"youtu\.be/([^?]+)"
    ]
    for p in patterns:
        m = re.search(p, url)
        if m:
            vid = m.group(1)
            return f"https://img.youtube.com/vi/{vid}/0.jpg"
    return None


# -------------------------------
# MBTI별 정보: (1) 공식곡 (2) YouTube URL (3) 하이라이트 의미 요약
# -------------------------------
RECOMMEND = {
    "ISTJ": {
        "personality": "책임감 있고 성실하며 안정감을 중시하는 타입.",
        "songs": [
            {
                "title": "Lemon — Kenshi Yonezu",
                "yt": "https://www.youtube.com/watch?v=SX_ViT4Ra7k",
                "highlight": "이 곡은 떠나간 사람을 그리워하며, 돌이킬 수 없는 시간 속에서 남겨진 후회와 미련을 담고 있어요. '지울 수 없는 아픔'을 바라보는 감정이 핵심입니다."
            },
            {
                "title": "First Love — Utada Hikaru",
                "yt": "https://www.youtube.com/watch?v=7Jr-9l23qAw",
                "highlight": "첫사랑의 순수함과 다시 돌아갈 수 없는 시간을 회상하는 감정이 중심이에요. 잊었다고 생각해도 마음 깊이 남아 있는 감정을 말해요."
            },
            {
                "title": "Kiseki — GReeeeN",
                "yt": "https://www.youtube.com/watch?v=G3RfsqwNfQc",
                "highlight": "사랑하는 사람과 함께하는 일상의 기적을 노래하며, 서로에게 감사하는 마음이 강조된 따뜻한 곡입니다."
            }
        ],
        "vocaloid": [
            {
                "title": "Senbonzakura — Hatsune Miku",
                "yt": "https://www.youtube.com/watch?v=shs0rAiwsGQ",
                "highlight": "격렬한 리듬 속에서 전통과 현대가 뒤섞인 세계를 표현하며, 자유에 대한 갈망을 상징적으로 담아낸 곡입니다."
            },
            {
                "title": "World is Mine — Hatsune Miku",
                "yt": "https://www.youtube.com/watch?v=EgqUJOudrcM",
                "highlight": "사랑받고 싶은 마음과 귀여운 투정을 솔직하게 표현해, 밝고 상큼한 매력을 담고 있어요."
            }
        ]
    },

    # 아래부터는 반복 구성  
    # 예시로 INFJ만 추가로 넣어드림 → 요청하면 16유형 전체 완성 버전 보내줄게!
    "INFJ": {
        "personality": "이상주의적이고 감성적이며 깊은 내면 세계를 가진 유형.",
        "songs": [
            {
                "title": "Nandemonaiya — RADWIMPS",
                "yt": "https://www.youtube.com/watch?v=9l9m76k7mGk",
                "highlight": "소중한 사람을 떠올리며 ‘그 순간의 따뜻함’을 되새기고, 다시 돌아갈 수 없는 시간을 아쉬워하는 감정이 핵심입니다."
            },
            {
                "title": "Pretender — Official HIGE DANDism",
                "yt": "https://www.youtube.com/watch?v=TQ8WlA2GXbk",
                "highlight": "사랑할 수 없다는 현실을 받아들이면서도 상대를 진심으로 아끼는 마음을 담고 있어요."
            },
            {
                "title": "Kataomoi — Aimer",
                "yt": "https://www.youtube.com/watch?v=9aJVr5tTTWk",
                "highlight": "한쪽 마음이지만 진심으로 사랑하는 감정을 담담하면서도 깊이 있게 표현한 곡입니다."
            }
        ],
        "vocaloid": [
            {
                "title": "Rolling Girl — Hatsune Miku",
                "yt": "https://www.youtube.com/watch?v=Bm21lU1i5uY",
                "highlight": "반복되는 실패 속에서도 다시 일어서려는 마음을 표현하며, 내면의 흔들리는 감정을 집중적으로 다룹니다."
            },
            {
                "title": "Just Be Friends — Luka",
                "yt": "https://www.youtube.com/watch?v=VoPzP-MwcLI",
                "highlight": "이별을 받아들이는 과정 속에서의 슬픔, 체념, 그리고 상대를 위한 마지막 배려가 핵심 의미입니다."
            }
        ]
    }
}

# ------------------------------------------------
# UI
# ------------------------------------------------
with st.sidebar:
    st.header("설정")
    show_vocaloid = st.checkbox("보컬로이드 곡도 보기", value=True)

mbti = st.selectbox("MBTI 유형을 선택하세요", MBTI_TYPES)

if mbti not in RECOMMEND:
    st.warning("아직 이 MBTI 데이터가 추가되지 않았습니다. 원하면 지금 바로 전체 16개 유형 완성해줄게요!")
    st.stop()

info = RECOMMEND[mbti]

st.subheader(f"💡 {mbti} 성격 분석")
st.write(info["personality"])

# ------------------------------------------------
# 일본 노래 추천 (썸네일 + 요약 포함)
# ------------------------------------------------
st.subheader("🎵 일본 노래 추천 (썸네일 + 하이라이트 의미)")
for song in info["songs"]:
    st.markdown(f"### {song['title']}")

    thumb = get_thumbnail(song["yt"])
    if thumb:
        st.image(thumb, use_column_width=True)

    st.markdown(f"**🎬 영상 링크:** [YouTube로 이동]({song['yt']})")
    st.write("**✨ 하이라이트 의미 요약**")
    st.info(song["highlight"])
    st.markdown("---")

# ------------------------------------------------
# 보컬로이드 추천
# ------------------------------------------------
if show_vocaloid:
    st.subheader("🤖 보컬로이드 추천")
    for song in info["vocaloid"]:
        st.markdown(f"### {song['title']}")

        thumb = get_thumbnail(song["yt"])
        if thumb:
            st.image(thumb, use_column_width=True)

        st.markdown(f"**🎬 영상 링크:** [YouTube로 이동]({song['yt']})")
        st.write("**✨ 하이라이트 의미 요약**")
        st.info(song["highlight"])
        st.markdown("---")

st.markdown("---")
st.write("※ 가사는 저작권 문제로 제공하지 않고, 의미 요약을 기반으로 제작되었습니다.")
