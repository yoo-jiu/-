import streamlit as st

st.set_page_config(page_title="MBTI 일본 노래 추천", layout="wide")
st.title("🎧 MBTI 기반 일본 노래 & 보컬로이드 추천")

# MBTI별 추천곡 데이터 (이미지 포함, 한국어 번역 제거)
DATA = {
    "ISTJ": {
        "jpop": [
            {"title": "Subtitle - Official髭男dism", "image": "https://i.imgur.com/3YlANgG.jpg", "lyric": "「君と過ごした日々…」라는 후렴이 반복되며 책임감 있는 사랑과 회상을 느끼게 합니다."},
            {"title": "Lemon - 米津玄師", "image": "https://i.imgur.com/6XjUBa8.jpg", "lyric": "失くしたものの大きさを実感し、痛みと後悔を抱え続ける心情이 돋보이는 곡입니다."}
        ],
        "vocaloid": [
            {"title": "シャルル - バルーン", "image": "https://i.imgur.com/Wx6YFQk.jpg", "lyric": "「どうして笑うんだろう」라는 반복되는 후렴이 자유에 대한 갈망과 슬픔을 함께 느끼게 합니다."}
        ]
    },
    "ISFJ": {
        "jpop": [
            {"title": "水平線 - back number", "image": "https://i.imgur.com/bm0vNwS.jpg", "lyric": "穏やかな波音に 비유된 日常 속의 사랑과 안정감을 노래해요."},
            {"title": "だから僕は音楽を辞めた - ヨルシカ", "image": "https://i.imgur.com/e3s7rkG.jpg", "lyric": "音楽を通じて失った 사람への 그리움을 표현하며, 마음의 공허함을 드러냅니다."}
        ],
        "vocaloid": [
            {"title": "愛言葉III - DECO*27", "image": "https://i.imgur.com/FaVYqzP.jpg", "lyric": "서로에게 전하는 애정의言葉 (말)을 반복하며, 따뜻하고 헌신적인 사랑을 노래합니다."}
        ]
    },
    "INFJ": {
        "jpop": [
            {"title": "夜に駆ける - YOASOBI", "image": "https://i.imgur.com/8FzEyKx.jpg", "lyric": "밤하늘을 달리듯 사랑과 삶의 무게를 동시에 느끼며, 운명과 선택의 이야기를 담고 있어요。"},
            {"title": "Brave Shine - Aimer", "image": "https://i.imgur.com/y9qX1Xh.jpg", "lyric": "어둠 속에서도 빛을 향해 나아가는 강한 의지를 표현하며 희망과 투쟁의 감정을 담고 있어요。"}
        ],
        "vocaloid": [
            {"title": "アスノヨゾラ哨戒班 - Orangestar", "image": "https://i.imgur.com/KqZtZSh.jpg", "lyric": "별이 빛나는 밤하늘 아래에서의 고독과 꿈을 지키는 결심을 노래합니다。"}
        ]
    },
    "INTJ": {
        "jpop": [
            {"title": "unravel - TK from 凛として時雨", "image": "https://i.imgur.com/yoGZB5S.jpg", "lyric": "파괴와 재생, 혼란한 감정의 소용돌이를 통해 깊은 자기 성찰을 그려냅니다。"},
            {"title": "逆光 - Ado", "image": "https://i.imgur.com/9pu2mZr.jpg", "lyric": "빛과 그림자의 대비를 통해 내면의 갈등과 에너지를 폭발적으로 표출해요。"}
        ],
        "vocaloid": [
            {"title": "ベノム - かいりきベア", "image": "https://i.imgur.com/WrYHPya.jpg", "lyric": "독(venom) 같은 감정이 마음 안에 퍼져나가며 강렬한 집착과 고뇌를 노래해요。"}
        ]
    },
    "ISTP": {
        "jpop": [
            {"title": "怪物 - YOASOBI", "image": "https://i.imgur.com/vQdWzPy.jpg", "lyric": "자신의 내면에 숨어 있는 괴물 같은 본성을 보며 두려움과 힘을 동시에 느끼는 감정입니다。"},
            {"title": "不可幸力 - Vaundy", "image": "https://i.imgur.com/ZXKQshh.jpg", "lyric": "불행 속에서도 존재의 의미를 찾고, 뒤틀린 운명에 맞서는 태도를 담고 있어요。"}
        ],
        "vocaloid": [
            {"title": "ブリキノダンス - 日向電工", "image": "https://i.imgur.com/5a6a1CI.jpg", "lyric": "기계적인 춤과 반복되는 리듬 속에서 자유와 속박의 경계를 탐구합니다。"}
        ]
    },
    "ISFP": {
        "jpop": [
            {"title": "花に亡霊 - ヨルシカ", "image": "https://i.imgur.com/1q3WbZp.jpg", "lyric": "꽃처럼 피었다 사라지는 존재에 대한 그리움과 덧없음을 노래합니다。"},
            {"title": "スパークル - RADWIMPS", "image": "https://i.imgur.com/GPipYAp.jpg", "lyric": "빛나는 순간들을 통해 삶의 의미를 되돌아보고, 희망과 상실을 함께 느껴요。"}
        ],
        "vocaloid": [
            {"title": "メルト - supercell", "image": "https://i.imgur.com/8uBu6dK.jpg", "lyric": "서로에게 용해되듯 다가가는 마음을 부드럽고 따뜻하게 표현한 곡입니다。"}
        ]
    },
    "INFP": {
        "jpop": [
            {"title": "春泥棒 - ヨルシカ", "image": "https://i.imgur.com/tAvvU6k.jpg", "lyric": "봄을 훔치는 듯한 순수하고 몽환적인 감성을 통해 잃어간 시간에 대한 아쉬움을 노래해요。"},
            {"title": "ドラマツルギー - Eve", "image": "https://i.imgur.com/G1TbpvV.jpg", "lyric": "극처럼 펼쳐지는 삶의 갈등과 감정의 기복을 드라마틱하게 표현합니다。"}
        ],
        "vocaloid": [
            {"title": "カゲロウデイズ - じん", "image": "https://i.imgur.com/lzCRVqo.jpg", "lyric": "시간과 현실의 흐름 속에서 반복되는 비극과 희망을 노래해요。"}
        ]
    },
    "INTP": {
        "jpop": [
            {"title": "KING - Kanaria", "image": "https://i.imgur.com/2soyJHj.jpg", "lyric": "왕처럼 군림하고 싶어 하는 욕망과 자유에 대한 집착이 섞여 있어요。"},
            {"title": "堕天 - Creepy Nuts", "image": "https://i.imgur.com/IaA6qX9.jpg", "lyric": "떨어지는 천사처럼 내면의 어두운 면과 타협하는 태도를 보여줍니다。"}
        ],
        "vocaloid": [
            {"title": "ドクハク - 水野あつ", "image": "https://i.imgur.com/k3BmXtW.jpg", "lyric": "독과 사랑이 뒤섞인 감정 속에서 고독과 통찰을 동시에 느끼게 합니다。"}
        ]
    },
    "ESTP": {
        "jpop": [
            {"title": "新時代 - Ado", "image": "https://i.imgur.com/0aFJq5C.jpg", "lyric": "변화를 두려워하지 않고 새로운 시대를 맞이하겠다는 결연함이 느껴져요。"},
            {"title": "紅蓮華 - LiSA", "image": "https://i.imgur.com/EtgQg1i.jpg", "lyric": "불타는 연꽃처럼 강렬한 의지와 전투적인 감정을 표현한 곡입니다。"}
        ],
        "vocaloid": [
            {"title": "威風堂々 - 梅とら", "image": "https://i.imgur.com/M8YZqKZ.jpg", "lyric": "당당하고 강렬하게 존재감을 드러내는 에너지와 자존감을 노래합니다。"}
        ]
    },
    "ESFP": {
        "jpop": [
            {"title": "打上花火 - DAOKO × 米津玄師", "image": "https://i.imgur.com/MhEMOq1.jpg", "lyric": "불꽃놀이처럼 잠깐 반짝이는 감정과 순간의 아름다움을 담은 곡이에요。"},
            {"title": "三原色 - YOASOBI", "image": "https://i.imgur.com/OUdVpZg.jpg", "lyric": "세 가지 색으로 비유된 관계와 감정의 혼합을 멋지게 표현합니다。"}
        ],
        "vocaloid": [
            {"title": "脱法ロック - Neru", "image": "https://i.imgur.com/xtQtqyk.jpg", "lyric": "사회 규범과의 충돌, 틀을 벗어난 자유에 대한 욕망이 강하게 느껴져요。"}
        ]
    },
    "ENFP": {
        "jpop": [
            {"title": "怪獣の花唄 - Vaundy", "image": "https://i.imgur.com/NuZ8FMX.jpg", "lyric": "거대한 괴수처럼 사랑을 노래하고, 그 속에서 순수함과 열정을 보여줍니다。"},
            {"title": "Habit - SEKAI NO OWARI", "image": "https://i.imgur.com/9kF0e9r.jpg", "lyric": "습관이란 이름으로 반복되는 일상 속에서도 특별한 의미를 찾아요。"}
        ],
        "vocaloid": [
            {"title": "テオ - Omoi", "image": "https://i.imgur.com/qTftgut.jpg", "lyric": "빛나는 꿈과 이상을 향해 달려가는 청춘의 열정과 희망을 담고 있어요。"}
        ]
    },
    "ENTP": {
        "jpop": [
            {"title": "阿修羅ちゃん - Ado", "image": "https://i.imgur.com/9A0xZkC.jpg", "lyric": "파격적이고 도전적인 태도, 내면의 혼란을 강렬하게 드러냅니다。"},
            {"title": "ナンセンス文学 - Eve", "image": "https://i.imgur.com/oDnXz2K.jpg", "lyric": "무의미해 보이는 단어와 감정 속에 깊은 철학과 아이러니를 담고 있어요。"}
        ],
        "vocaloid": [
            {"title": "ヒバナ - DECO*27", "image": "https://i.imgur.com/7V1NBUP.jpg", "lyric": "불꽃처럼 폭발하는 감정, 사랑과 증오 사이의 강렬한 갈등을 노래해요。"}
        ]
    },
    "ESTJ": {
        "jpop": [
            {"title": "炎 - LiSA", "image": "https://i.imgur.com/Oy7TIw2.jpg", "lyric": "자신의 신념을 위해서 무엇이든 태울 수 있는 강한 의지를 표현합니다。"},
            {"title": "CORE PRIDE - UVERworld", "image": "https://i.imgur.com/2gQWQXF.jpg", "lyric": "핵심 자존감과 자부심, 그리고 삶의 굳건한 기본을 강조하는 곡이에요。"}
        ],
        "vocaloid": [
            {"title": "劣等上等 - Giga", "image": "https://i.imgur.com/76rJOZI.jpg", "lyric": "자기 자신을 낮추면서도 동시에 강하게 주장하는 역설적인 태도를 담고 있어요。"}
        ]
    },
    "ESFJ": {
        "jpop": [
            {"title": "シル・ヴ・プレジデント - P丸様。", "image": "https://i.imgur.com/1c5Fh6G.jpg", "lyric": "사람들과 함께 리더십을 발휘하는 즐거움과 책임감을 표현합니다。"},
            {"title": "可愛くてごめん - HoneyWorks", "image": "https://i.imgur.com/U5vnx7v.jpg", "lyric": "사랑스러운 자신을 인정받고 싶은 소박한 마음을 귀엽고 솔직하게 노래합니다。"}
        ],
        "vocaloid": [
            {"title": "桃源恋歌 - GARNiDELiA", "image": "https://i.imgur.com/IZB0xus.jpg", "lyric": "이상향(桃源)을 향한 사랑과 평화에 대한 열망을 로맨틱하게 표현해요。"}
        ]
    },
    "ENFJ": {
        "jpop": [
            {"title": "群青 - YOASOBI", "image": "https://i.imgur.com/Be5nYV6.jpg", "lyric": "파란 하늘처럼 넓고 깊은 감정 속에서 공동체와 연대의 의미를 탐구합니다。"},
            {"title": "残響散歌 - Aimer", "image": "https://i.imgur.com/4FqZx5g.jpg", "lyric": "울려 퍼지는 메아리처럼 과거와 현재의 감정이 뒤섞이는 드라마틱한 곡이에요。"}
        ],
        "vocaloid": [
            {"title": "ゴーストルール - DECO*27", "image": "https://i.imgur.com/ZXFQTRz.jpg", "lyric": "규칙과 금지된 감정 사이에서 자신의 정체성을 찾으려는 고투의 노래예요。"}
        ]
    },
    "ENTJ": {
        "jpop": [
            {"title": "うっせぇわ - Ado", "image": "https://i.imgur.com/XZcN6NU.jpg", "lyric": "사회에 대한 반항과 자기 주장을 강하게 드러내는 대담한 곡입니다。"},
            {"title": "不可逆リプレイス - MY FIRST STORY", "image": "https://i.imgur.com/q9GJkQ8.jpg", "lyric": "되돌릴 수 없는 변화와 치열한 삶의 전투를 노래합니다。"}
        ],
        "vocaloid": [
            {"title": "ヴィラン - 日向電工", "image": "https://i.imgur.com/Nh3L3OE.jpg", "lyric": "악당(Villain)처럼 강하고 냉정한 모습 뒤에 숨겨진 아픔을 표현해요。"}
        ]
    }
}

# MBTI 선택
mbti = st.selectbox("당신의 MBTI를 선택하세요", list(DATA.keys()))

if mbti:
    st.header(f"🎶 {mbti} 유형에게 어울리는 노래 추천")

    st.subheader("— 일본 J‑POP 추천")
    for song in DATA[mbti]["jpop"]:
        st.image(song["image"], width=300)
        st.write(f"**{song['title']}**")
        st.write(f"하이라이트 가사: {song['lyric']}")
        st.write("---")

    st.subheader("— 보컬로이드 추천")
    for song in DATA[mbti]["vocaloid"]:
        st.image(song["image"], width=300)
        st.write(f"**{song['title']}**")
        st.write(f"하이라이트 가사: {song['lyric']}")
        st.write("---")
