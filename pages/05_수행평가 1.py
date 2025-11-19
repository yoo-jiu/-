import streamlit as st

# MBTI별 추천 곡 데이터

mbti_data = {
"ISTJ": {
"jpop": ["Subtitle - Official髭男dism", "Lemon - 米津玄師"],
"vocaloid": ["シャルル - バルーン"]
},
"ISFJ": {
"jpop": ["水平線 - back number", "だから僕は音楽を辞めた - ヨルシカ"],
"vocaloid": ["愛言葉III - DECO*27"]
},
"INFJ": {
"jpop": ["夜に駆ける - YOASOBI", "Brave Shine - Aimer"],
"vocaloid": ["アスノヨゾラ哨戒班 - Orangestar"]
},
"INTJ": {
"jpop": ["unravel - TK", "逆光 - Ado"],
"vocaloid": ["ベノム - かいりきベア"]
},
"ISTP": {
"jpop": ["怪物 - YOASOBI", "不可幸力 - Vaundy"],
"vocaloid": ["ブリキノダンス - 日向電工"]
},
"ISFP": {
"jpop": ["花に亡霊 - ヨルシカ", "スパークル - RADWIMPS"],
"vocaloid": ["メルト - supercell"]
},
"INFP": {
"jpop": ["春泥棒 - ヨルシカ", "ドラマツルギー - Eve"],
"vocaloid": ["カゲロウデイズ - じん"]
},
"INTP": {
"jpop": ["KING - Kanaria", "堕天 - Creepy Nuts"],
"vocaloid": ["ドクハク - 水野あつ"]
},
"ESTP": {
"jpop": ["新時代 - Ado", "紅蓮華 - LiSA"],
"vocaloid": ["威風堂々 - 梅とら"]
},
"ESFP": {
"jpop": ["打上花火 - DAOKO × 米津玄師", "三原色 - YOASOBI"],
"vocaloid": ["脱法ロック - Neru"]
},
"ENFP": {
"jpop": ["怪獣の花唄 - Vaundy", "Habit - SEKAI NO OWARI"],
"vocaloid": ["テオ - Omoi"]
},
"ENTP": {
"jpop": ["阿修羅ちゃん - Ado", "ナンセンス文学 - Eve"],
"vocaloid": ["ヒバナ - DECO*27"]
},
"ESTJ": {
"jpop": ["炎 - LiSA", "CORE PRIDE - UVERworld"],
"vocaloid": ["劣等上等 - Giga"]
},
"ESFJ": {
"jpop": ["シル・ヴ・プレジデント - P丸様。", "可愛くてごめん - HoneyWorks"],
"vocaloid": ["桃源恋歌 - GARNiDELiA"]
},
"ENFJ": {
"jpop": ["群青 - YOASOBI", "残響散歌 - Aimer"],
"vocaloid": ["ゴーストルール - DECO*27"]
},
"ENTJ": {
"jpop": ["うっせぇわ - Ado", "不可逆リプレイス - MY FIRST STORY"],
"vocaloid": ["ヴィラン - 日向電工"]
}
}

st.title("🎵 MBTI별 일본 노래 & 보컬로이드 추천")

# MBTI 선택

selected_mbti = st.selectbox("당신의 MBTI를 선택하세요", list(mbti_data.keys()))

# 추천 곡 보여주기

if selected_mbti in mbti_data:
st.subheader(f"🎧 {selected_mbti}님을 위한 J-POP 추천곡")
for song in mbti_data[selected_mbti]["jpop"]:
st.write(f"- {song}")

```
st.subheader(f"🎹 {selected_mbti}님을 위한 보컬로이드 추천곡")
for song in mbti_data[selected_mbti]["vocaloid"]:
    st.write(f"- {song}")
```

else:
st.error("지원하지 않는 MBTI입니다.")
