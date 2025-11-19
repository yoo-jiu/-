import streamlit as st

# 16가지 MBTI 유형별 성격 키워드 및 노래 추천 데이터
# [MBTI 유형]: (성격 키워드, [유명 J-POP], [유명 VOCALOID 곡])
MBTI_DATA = {
    "ISTJ": ("현실적, 논리적, 책임감 강한 원칙주의자",
             ["아이묭 - 마리골드 (マリーゴールド)", "히라이 켄 - Non-Fiction"],
             ["하츠네 미쿠 - 멜트 (メルト)", "카가미네 린/렌 - 로스트 원의 호곡 (ロストワンの号哭)"]),

    "ISFJ": ("따뜻하고 헌신적이며 조용하고 성실한 수호자",
             ["요네즈 켄시 - Lemon", "Aimer - 잔향산가 (残響散歌)"],
             ["하츠네 미쿠 - 사랑은 전쟁 (恋は戦争)", "MARETU - 마인드 브랜드 (マインドブランド)"]),

    "INFJ": ("통찰력 있고 창의적이며 확고한 신념을 가진 예언자",
             ["King Gnu - 백일 (白日)", "미야자키 하야오 OST - 언제나 몇 번이라도"],
             ["하츠네 미쿠 - 천본앵 (千本桜)", "40mP - 꼭두각시 피에로 (からくりピエロ)"]),

    "INTJ": ("지적 호기심이 많고 전략적이며 독립적인 설계자",
             ["RADWIMPS - 전전전세 (前前前世)", "후지이 카제 - Shinunoga E-Wa"],
             ["하츠네 미쿠 - 월즈 엔드 댄스홀 (ワールズエンド・ダンスホール)", "DECO*27 - 망상감상대상연맹 (妄想感傷代償連盟)"]),

    "ISTP": ("과묵하고 분석적이며 도구를 잘 다루는 만능 재주꾼",
             ["Official髭男dism - Pretender", "LiSA - 홍련화 (紅蓮華)"],
             ["GUMI - 외톨이 멜로디 (独りんぼエンヴィー)", "하츠네 미쿠 - Tell Your World"]),

    "ISFP": ("호기심 많고 예술적이며 온화한 성격의 모험가",
             ["Vaundy - 괴물 (怪獣の花唄)", "나카지마 미유키 - 실 (糸)"],
             ["하츠네 미쿠 - 노래에 형태는 없지만 (歌に形はないけれど)", "메구리네 루카 - Just Be Friends"]),

    "INFP": ("낭만적이고 사려 깊으며 이상적인 가치 추구자",
             ["YOASOBI - 밤을 달리다 (夜に駆ける)", "오자키 유타카 - I Love You"],
             ["하츠네 미쿠 - 이별만이 인생이다 (別れだけが人生だ)", "벌룬 - 샤를 (シャルル)"]),

    "INTP": ("조용하고 분석적이며 끊임없이 지식을 탐구하는 사색가",
             ["Eve - 회회기담 (廻廻奇譚)", "Mrs. GREEN APPLE - 아오와 아페 (青と夏)"],
             ["하츠네 미쿠 - 마트료시카 (マトリョシカ)", "카후 - 퀸 오브 몬스터즈 (QUEEN OF MONSTERS)"]),

    "ESTP": ("개방적이고 행동 지향적이며 타협을 모르는 사업가",
             ["DISH// - 고양이 (猫)", "B'z - ULTRA SOUL"],
             ["하츠네 미쿠 - Calc.", "나유타 마지 - 콜렉터 (コレクター)"]),

    "ESFP": ("재미있고 에너지가 넘치며 즉흥적인 연예인",
             ["TWICE - Fanfare", "카와이 마사히로 - 이터널 선샤인 (Eternal Sunshine)"],
             ["하츠네 미쿠 - 미쿠미쿠하게 해줄게♪ (みくみくにしてあげる♪)", "GUMI - 자상무색 (自傷無色)"]),

    "ENFP": ("열정적이고 창의적이며 사회생활이 활발한 활동가",
             ["back number - HAPPY END", "아야카 - TSUBAKI"],
             ["하츠네 미쿠 - 월드 이즈 마인 (ワールドイズマイン)", "GUMI - 굿바이 선언 (グッバイ宣言)"]),

    "ENTP": ("지적이고 논쟁을 즐기는 독창적인 발명가",
             ["ONE OK ROCK - wherever you are", "사잔 올 스타즈 - 진흙투성이의 매미 (泥だらけの蜩)"],
             ["하츠네 미쿠 - 뇌장작렬 걸 (脳漿炸裂ガール)", "카가미네 린 - 악의 딸 (悪ノ娘)"]),

    "ESTJ": ("실용적이고 체계적이며 현실적인 관리자",
             ["호시노 겐 - 恋 (코이)", "아무로 나미에 - Can You Celebrate?"],
             ["하츠네 미쿠 - 팩토리 오토마타 (ファクトリーオートマタ)", "MEIKO - Nostalogic"]),

    "ESFJ": ("사교적이고 친절하며 헌신적인 사교적인 코디네이터",
             ["AKB48 - 헤비 로테이션 (ヘビーローテーション)", "이키모노가카리 - 감사합니다 (ありがとう)"],
             ["하츠네 미쿠 - 당신에게 바치는 러브송 (あなたに贈るラブソング)", "GUMI - 키쿠카이토로 (きくかいとろ)"]),

    "ENFJ": ("카리스마 있고 이타적이며 사람들을 이끄는 지도자",
             ["DREAM COME TRUE - 사랑이 있는 곳 (愛が生まれた日)", "히카루 우타다 - First Love"],
             ["하츠네 미쿠 - 로미오와 신데렐라 (ロミオとシンデレラ)", "GUMI - 생명의 유스티티아 (命のユースティティア)"]),

    "ENTJ": ("확신에 차 있고 목표 지향적인 대담한 통솔자",
             ["아라시 - Love so sweet", "TUBE - Summer Dream"],
             ["하츠네 미쿠 - 고백 예행 연습 (告白予行練習)", "DECO*27 - 신사불성 (神っぽいな)"]),
}

# Streamlit 앱 구성
def main():
    st.set_page_config(page_title="MBTI 맞춤 일본 노래 추천 시스템", layout="wide")
    
    # 제목 설정
    st.title("🎼 MBTI 유형별 맞춤 일본 노래 추천")
    st.markdown("---")

    # MBTI 선택
    mbti_list = sorted(MBTI_DATA.keys())
    mbti_select = st.selectbox(
        "**당신의 MBTI 유형을 선택해 주세요!**", 
        mbti_list, 
        index=mbti_list.index("INFP") # 기본값 설정
    )

    if mbti_select:
        st.header(f"✨ {mbti_select} 유형 분석 및 추천 곡")
        
        # 데이터 추출
        keywords, jpop_list, vocaloid_list = MBTI_DATA[mbti_select]
        
        # 1. 성격 분석
        st.subheader("💡 성격 키워드")
        st.info(f"**{mbti_select}** 유형은 **{keywords}**입니다.")
        
        st.markdown("---")
        
        # 2. 유명 J-POP 추천
        st.subheader("🎤 당신의 분위기에 맞는 유명 J-POP 추천")
        jpop_markdown = "\n".join([f"* **{title}**" for title in jpop_list])
        st.markdown(jpop_markdown)
        st.caption("※ 대중적으로 많은 사랑을 받은 히트곡 위주로 선정되었습니다.")
        
        st.markdown("---")
        
        # 3. 보컬로이드 노래 추가 추천
        st.subheader("🤖 보컬로이드(VOCALOID) 노래 추가 추천")
        vocaloid_markdown = "\n".join([f"* **{title}**" for title in vocaloid_list])
        st.markdown(vocaloid_markdown)
        st.caption("※ 보컬로이드의 상징적인 명곡 및 유형과 분위기가 맞는 곡으로 선정되었습니다.")
        
        st.markdown("---")
        
        st.success(f"📌 {mbti_select} 님, 이 노래들과 함께 오늘 하루를 즐겁게 보내시길 바랍니다!")

if __name__ == "__main__":
    main()
