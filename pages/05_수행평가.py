import streamlit as st

st.set_page_config(page_title="MBTI 일본 노래 추천", layout="wide")

st.title("🎵 MBTI 기반 일본 노래 추천")
st.write("원하는 MBTI 유형을 선택하면 일본 노래 + 보컬로이드 노래를 추천해줘!")

# -------------------------------------------------------
#  MBTI별 데이터베이스 (이미지/가사/번역은 자유롭게 교체)
# -------------------------------------------------------

DATA = {
    "ISTJ": {
        "jpop": [
            {
                "title": "Pretender - Official髭男dism",
                "image": "이미지_URL_1",
                "lyric": "하이라이트 가사 A",
                "ko": "한국어 번역 A"
            },
            {
                "title": "Lemon - 米津玄師",
                "image": "이미지_URL_2",
                "lyric": "하이라이트 가사 A",
                "ko": "한국어 번역 A"
            },
        ],
        "vocaloid": [
            {
                "title": "シャルル - バルーン",
                "image": "이미지_URL_3",
                "lyric": "하이라이트 가사 A",
                "ko": "한국어 번역 A"
            }
        ]
    },

    "ISFJ": {
        "jpop": [
            {
                "title": "アイラブユー - back number",
                "image": "이미지_URL_1",
                "lyric": "하이라이트 가사 A",
                "ko": "한국어 번역 A"
            }
        ],
        "vocaloid": [
            {
                "title": "ラプンツェル - Hatsune Miku",
                "image": "이미지_URL_2",
                "lyric": "하이라이트 가사 A",
                "ko": "한국어 번역 A"
            }
        ]
    },

    "INFJ": {
        "jpop": [
            {
                "title": "夜に駆ける - YOASOBI",
                "image": "이미지_URL_1",
                "lyric": "하이라이트 가사 A",
                "ko": "한국어 번역 A"
            }
        ],
        "vocaloid": [
            {
                "title": "エンヴィーベイビー - Kanaria",
                "image": "이미지_URL_2",
                "lyric": "하이라이트 가사 A",
                "ko": "한국어 번역 A"
            }
        ]
    },

    "INTJ": {
        "jpop": [
            {
                "title": "unravel - TK from 凛として時雨",
                "image": "이미지_URL_1",
                "lyric": "하이라이트 가사 A",
                "ko": "한국어 번역 A"
            }
        ],
        "vocaloid": [
            {
                "title": "失敗作少女 - かいりきベア",
                "image": "이미지_URL_2",
                "lyric": "하이라이트 가사 A",
                "ko": "한국어 번역 A"
            }
        ]
    },

    "ISTP": {
        "jpop": [
            {
                "title": "怪物 - YOASOBI",
                "image": "이미지_URL_1",
                "lyric": "하이라이트 가사 A",
                "ko": "한국어 번역 A"
            }
        ],
        "vocaloid": [
            {
                "title": "ブリキノダンス - 日向電工",
                "image": "이미지_URL_2",
                "lyric": "하이라이트 가사 A",
                "ko": "한국어 번역 A"
            }
        ]
    },

    "ISFP": {
        "jpop": [
            {
                "title": "花に亡霊 - ヨルシカ",
                "image": "이미지_URL_1",
                "lyric": "하이라이트 가사 A",
                "ko": "한국어 번역 A"
            }
        ],
        "vocaloid": [
            {
                "title": "メルト - supercell",
                "image": "이미지_URL_2",
                "lyric": "하이라이트 가사 A",
                "ko": "한국어 번역 A"
            }
        ]
    },

    "INFP": {
        "jpop": [
            {
                "title": "春泥棒 - ヨルシカ",
                "image": "이미지_URL_1",
                "lyric": "하이라이트 가사 A",
                "ko": "한국어 번역 A"
            }
        ],
        "vocaloid": [
            {
                "title": "アスノヨゾラ哨戒班 - Orangestar",
                "image": "이미지_URL_2",
                "lyric": "하이라이트 가사 A",
                "ko": "한국어 번역 A"
            }
        ]
    },

    "INTP": {
        "jpop": [
            {
                "title": "KING - Kanaria",
                "image": "이미지_URL_1",
                "lyric": "하이라이트 가사 A",
                "ko": "한국어 번역 A"
            }
        ],
        "vocaloid": [
            {
                "title": "ドクハク - 水野あつ",
                "image": "이미지_URL_2",
                "lyric": "하이라이트 가사 A",
                "ko": "한국어 번역 A"
            }
        ]
    },

    "ESTP": {
        "jpop": [
            {
                "title": "新時代 - Ado",
                "image": "이미지_URL_1",
                "lyric": "하이라이트 가사 A",
                "ko": "한국어 번역 A"
            }
        ],
        "vocaloid": [
            {
                "title": "威風堂々 - 梅とら",
                "image": "이미지_URL_2",
                "lyric": "하이라이트 가사 A",
                "ko": "한국어 번역 A"
            }
        ]
    },

    "ESFP": {
        "jpop": [
            {
                "title": "打上花火 - DAOKO × 米津玄師",
                "image": "이미지_URL_1",
                "lyric": "하이라이트 가사 A",
                "ko": "한국어 번역 A"
            }
        ],
        "vocaloid": [
            {
                "title": "脱法ロック - Neru",
                "image": "이미지_URL_2",
                "lyric": "하이라이트 가사 A",
                "ko": "한국어 번역 A"
            }
        ]
    },

    "ENFP": {
        "jpop": [
            {
                "title": "怪獣の花唄 - Vaundy",
                "image": "이미지_URL_1",
                "lyric": "하이라이트 가사 A",
                "ko": "한국어 번역 A"
            }
        ],
        "vocaloid": [
            {
                "title": "テオ - Omoi",
                "image": "이미지_URL_2",
                "lyric": "하이라이트 가사 A",
                "ko": "한국어 번역 A"
            }
        ]
    },

    "ENTP": {
        "jpop": [
            {
                "title": "逆光 - Ado",
                "image": "이미지_URL_1",
                "lyric": "하이라이트 가사 A",
                "ko": "한국어 번역 A"
            }
        ],
        "vocaloid": [
            {
                "title": "ヒバナ - DECO*27",
                "image": "이미지_URL_2",
                "lyric": "하이라이트 가사 A",
                "ko": "한국어 번역 A"
            }
        ]
    },

    "ESTJ": {
        "jpop": [
            {
                "title": "紅蓮華 - LiSA",
                "image": "이미지_URL_1",
                "lyric": "하이라이트 가사 A",
                "ko": "한국어 번역 A"
            }
        ],
        "vocaloid": [
            {
                "title": "劣等上等 - Giga",
                "image": "이미지_URL_2",
                "lyric": "하이라이트 가사 A",
                "ko": "한국어 번역 A"
            }
        ]
    },

    "ESFJ": {
        "jpop": [
            {
                "title": "シル・ヴ・プレジデント - P丸様。",
                "image": "이미지_URL_1",
                "lyric": "하이라이트 가사 A",
                "ko": "한국어 번역 A"
            }
        ],
        "vocaloid": [
            {
                "title": "桃源恋歌 - GARNiDELiA",
                "image": "이미지_URL_2",
                "lyric": "하이라이트 가사 A",
                "ko": "한국어 번역 A"
            }
        ]
    },

    "ENFJ": {
        "jpop": [
            {
                "title": "群青 - YOASOBI",
                "image": "이미지_URL_1",
                "lyric": "하이라이트 가사 A",
                "ko": "한국어 번역 A"
            }
        ],
        "vocaloid": [
            {
                "title": "プロトディスコ - DECO*27",
                "image": "이미지_URL_2",
                "lyric": "하이라이트 가사 A",
                "ko": "한국어 번역 A"
            }
        ]
    },

    "ENTJ": {
        "jpop": [
            {
                "title": "炎 - LiSA",
                "image": "이미지_URL_1",
                "lyric": "하이라이트 가사 A",
                "ko": "한국어 번역 A"
            }
        ],
        "vocaloid": [
            {
                "title": "ブリキノダンス - 日向電工",
                "image": "이미지_URL_2",
                "lyric": "하이라이트 가사 A",
                "ko": "한국어 번역 A"
            }
        ]
    },
}

# -------------------------------------------------------
#  UI
# -------------------------------------------------------

mbti = st.selectbox("MBTI를 선택하세요", list(DATA.keys()))

if mbti:
    st.header(f"🎧 {mbti} 추천 일본 노래")

    # JPOP
    st.subheader("⭐ 일본 J-POP 추천")
    for song in DATA[mbti]["jpop"]:
        st.image(song["image"], width=300)
        st.write(f"### 🎵 {song['title']}")
        st.write(f"**하이라이트 가사:** {song['lyric']}")
        st.write(f"**한국어 번역:** {song['ko']}")
        st.write("---")

    st.subheader("💠 보컬로이드 추천")
    for song in DATA[mbti]["vocaloid"]:
        st.image(song["image"], width=300)
        st.write(f"### 🎶 {song['title']}")
        st.write(f"**하이라이트 가사:** {song['lyric']}")
        st.write(f"**한국어 번역:** {song['ko']}")
        st.write("---")
