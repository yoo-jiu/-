import streamlit as st

# 16가지 MBTI 유형별 성격 키워드 및 노래 추천 데이터 (이미지 URL 및 가사 추가)
# [MBTI 유형]: (성격 키워드,
#               [(유명 J-POP 제목, 이미지 URL, 가사 일부)],
#               [(유명 VOCALOID 곡 제목, 이미지 URL, 가사 일부)])
MBTI_DATA = {
    "ISTJ": ("현실적, 논리적, 책임감 강한 원칙주의자",
             [("아이묭 - 마리골드 (マリーゴールド)", "https://i.imgur.com/G3t4p7C.jpeg", "麦わらの帽子の君が\n揺れるたびに 揺れるたびに"),
              ("히라이 켄 - Non-Fiction", "https://i.imgur.com/1mH9y1w.jpeg", "誰もが誰かのノンフィクション\nそうさ僕ら物語の途中")],
             [("하츠네 미쿠 - 멜트 (メルト)", "https://i.imgur.com/mX9xLzF.jpeg", "メルト 溶けてしまいそう\n好きだなんて 絶対言えない"),
              ("카가미네 린/렌 - 로스트 원의 호곡 (ロストワンの号哭)", "https://i.imgur.com/8Q7O0lT.jpeg", "一体全体何を学べば\nテストの点数は上がるんですか")]),

    "ISFJ": ("따뜻하고 헌신적이며 조용하고 성실한 수호자",
             [("요네즈 켄시 - Lemon", "https://i.imgur.com/lM3pYwS.jpeg", "あの日の悲しみさえ\nあの日の苦しみさえ"),
              ("Aimer - 잔향산가 (残響散歌)", "https://i.imgur.com/C3k3w5C.jpeg", "誰が為に響く 不協和音\nざわめく波紋 蹴散らして")],
             [("하츠네 미쿠 - 사랑은 전쟁 (恋は戦争)", "https://i.imgur.com/G7y7m7w.jpeg", "恋する乙女は 止まれないの\n暴走モード 突入よ"),
              ("MARETU - 마인드 브랜드 (マインドブランド)", "https://i.imgur.com/i9zC9C7.jpeg", "壊してしまえ こんな精神も\n忘れてしまえ こんな感情も")]),

    "INFJ": ("통찰력 있고 창의적이며 확고한 신념을 가진 예언자",
             [("King Gnu - 백일 (白日)", "https://i.imgur.com/h5rC51m.jpeg", "真っ白な日々に舞い降りた\n黒い雨が 洗い流した"),
              ("미야자키 하야오 OST - 언제나 몇 번이라도", "https://i.imgur.com/h6f3p5v.jpeg", "呼んでいる 胸のどこか奥で\nいつも心踊る 夢を見たい")],
             [("하츠네 미쿠 - 천본앵 (千本桜)", "https://i.imgur.com/E5E8yE8.jpeg", "千本桜 夜ニ紛レ\n君ノ歌声 モガセヨ"),
              ("40mP - 꼭두각시 피에로 (からくりピエロ)", "https://i.imgur.com/lJ4J1jH.jpeg", "からくりピエロ 踊る夜\n君の心 弄ぶように")]),

    "INTJ": ("지적 호기심이 많고 전략적이며 독립적인 설계자",
             [("RADWIMPS - 전전전세 (前前前世)", "https://i.imgur.com/2s3j5Bq.jpeg", "君のゼンゼンゼン世から僕は\n君を探し始めたよ"),
              ("후지이 카제 - Shinunoga E-Wa", "https://i.imgur.com/l6qQ1h3.jpeg", "死ぬのがいいわ あなたとこのまま\nお揃いの地獄へ落ちよう")],
             [("하츠네 미쿠 - 월즈 엔드 댄스홀 (ワールズエンド・ダンスホール)", "https://i.imgur.com/b2Z3t2W.jpeg", "世界の端っこで\nさあ踊り明かそう"),
              ("DECO*27 - 망상감상대상연맹 (妄想感傷代償連盟)", "https://i.imgur.com/r7P3u4V.jpeg", "妄想感傷代償連盟\nきっと僕らはそう")]
             ),
    
    "ISTP": ("과묵하고 분석적이며 도구를 잘 다루는 만능 재주꾼",
             [("Official髭男dism - Pretender", "https://i.imgur.com/N7b0qD6.jpeg", "僕ら恋する何者にも\nなれなかったな"),
              ("LiSA - 홍련화 (紅蓮華)", "https://i.imgur.com/x0L0Q0d.jpeg", "強く 強くなれる理由を知った\n僕を連れて進め")],
             [("GUMI - 외톨이 멜로디 (独りんぼエンヴィー)", "https://i.imgur.com/gK2J3A8.jpeg", "あのね、あたしは\n独りんぼエンヴィー"),
              ("하츠네 미쿠 - Tell Your World", "https://i.imgur.com/y3x7y6S.jpeg", "伝えたい 想いは世界へ\nきっと届くから")]),

    "ISFP": ("호기심 많고 예술적이며 온화한 성격의 모험가",
             [("Vaundy - 괴물 (怪獣の花唄)", "https://i.imgur.com/G3Z1V67.jpeg", "怪獣の歌が響く\n僕らの世界で"),
              ("나카지마 미유키 - 실 (糸)", "https://i.imgur.com/P0u0B6e.jpeg", "縦の糸はあなた 横の糸は私\n逢うべき糸に 出会えることを")],
             [("하츠네 미쿠 - 노래에 형태는 없지만 (歌に形はないけれど)", "https://i.imgur.com/a4E2D3E.jpeg", "歌に形は無いけれど\n君の心を揺らすはず"),
              ("메구리네 루카 - Just Be Friends", "https://i.imgur.com/q2y2n0q.jpeg", "Just be friends\nただそれだけ")]),

    "INFP": ("낭만적이고 사려 깊으며 이상적인 가치 추구자",
             [("YOASOBI - 밤을 달리다 (夜に駆ける)", "https://i.imgur.com/h9y9y6y.jpeg", "沈むように溶けてゆくように\n二人だけの空が広がる夜に"),
              ("오자키 유타카 - I Love You", "https://i.imgur.com/1gH2o8o.jpeg", "I LOVE YOU I LOVE YOU I LOVE YOU\n届かない歌を唄う")],
             [("하츠네 미쿠 - 이별만이 인생이다 (別れだけが人生だ)", "https://i.imgur.com/5J3J5J3.jpeg", "別れだけが人生だ\nそうやって生きてきた"),
              ("벌룬 - 샤를 (シャルル)", "https://i.imgur.com/6U6U6U6.jpeg", "シャルル シャルル シャルル\n笑って 笑って")]),

    "INTP": ("조용하고 분석적이며 끊임없이 지식을 탐구하는 사색가",
             [("Eve - 회회기담 (廻廻奇譚)", "https://i.imgur.com/7L7L7L7.jpeg", "呪いの廻るこの世界で\n僕は君を救えるのか"),
              ("Mrs. GREEN APPLE - 아오와 아페 (青と夏)", "https://i.imgur.com/8M8M8M8.jpeg", "青い夏 空に舞う\n白い雲 掴もうよ")],
             [("하츠네 미쿠 - 마트료시카 (マトリョシカ)", "https://i.imgur.com/9N9N9N9.jpeg", "マトリョシカ マトリョシカ\n踊り狂った")]),
              ("카후 - 퀸 오브 몬스터즈 (QUEEN OF MONSTERS)", "https://i.imgur.com/XqXqXqX.jpeg", "Queen of Monsters\n私は自由よ")]),

    "ESTP": ("개방적이고 행동 지향적이며 타협을 모르는 사업가",
             [("DISH// - 고양이 (猫)", "https://i.imgur.com/1B1B1B1.jpeg", "猫になった 君と二人\n愛し合ったのは幻かな"),
              ("B'z - ULTRA SOUL", "https://i.imgur.com/2C2C2C2.jpeg", "ULTRA SOUL\nHEY!")],
             [("하츠네 미쿠 - Calc.", "https://i.imgur.com/3D3D3D3.jpeg", "あぁ 計算通りいかない\n僕らの恋路"),
              ("나유타 마지 - 콜렉터 (コレクター)", "https://i.imgur.com/4E4E4E4.jpeg", "コレクターコレクター\n君を集める")]),

    "ESFP": ("재미있고 에너지가 넘치며 즉흥적인 연예인",
             [("TWICE - Fanfare", "https://i.imgur.com/5F5F5F5.jpeg", "Fanfare 鳴り響かせ\n世界中に届けよう"),
              ("카와이 마사히로 - 이터널 선샤인 (Eternal Sunshine)", "https://i.imgur.com/6G6G6G6.jpeg", "エターナルサンシャイン\n消えない輝き")],
             [("하츠네 미쿠 - 미쿠미쿠하게 해줄게♪ (みくみくにしてあげる♪)", "https://i.imgur.com/7H7H7H7.jpeg", "みっくみくにしてあげる\n歌ってあげる"),
              ("GUMI - 자상무색 (自傷無色)", "https://i.imgur.com/8I8I8I8.jpeg", "自傷無色\n消えてくよ")]),

    "ENFP": ("열정적이고 창의적이며 사회생활이 활발한 활동가",
             [("back number - HAPPY END", "https://i.imgur.com/9J9J9J9.jpeg", "ハッピーエンド\n私じゃない誰かを"),
              ("아야카 - TSUBAKI", "https://i.imgur.com/0K0K0K0.jpeg", "椿の花が咲く頃に\nまた逢えるかな")],
             [("하츠네 미쿠 - 월드 이즈 마인 (ワールドイズマイン)", "https://i.imgur.com/1L1L1L1.jpeg", "世界で一番お姫様\n気づいてよね"),
              ("GUMI - 굿바이 선언 (グッバイ宣言)", "https://i.imgur.com/2M2M2M2.jpeg", "グッバイ宣言\nバイバイしたいの")]),

    "ENTP": ("지적이고 논쟁을 즐기는 독창적인 발명가",
             [("ONE OK ROCK - wherever you are", "https://i.imgur.com/3N3N3N3.jpeg", "Wherever you are\nI'll always be with you"),
              ("사잔 올 스타즈 - 진흙투성이의 매미 (泥だらけの蜩)", "https://i.imgur.com/4O4O4O4.jpeg", "泥だらけのヒグラシが\n泣いている")],
             [("하츠네 미쿠 - 뇌장작렬 걸 (脳漿炸裂ガール)", "https://i.imgur.com/5P5P5P5.jpeg", "脳漿炸裂ガール\n狂い咲け"),
              ("카가미네 린 - 악의 딸 (悪ノ娘)", "https://i.imgur.com/6Q6Q6Q6.jpeg", "悪ノ娘\nまたもや傲慢に")]),

    "ESTJ": ("실용적이고 체계적이며 현실적인 관리자",
             [("호시노 ゲン - 恋 (코이)", "https://i.imgur.com/7R7R7R7.jpeg", "恋ダンス踊るように\n二人で歩こう"),
              ("아무로 나미에 - Can You Celebrate?", "https://i.imgur.com/8S8S8S8.jpeg", "Can you celebrate?\nCan you kiss me tonight?")],
             [("하츠네 미쿠 - 팩토리 오토마타 (ファクトリーオートマタ)", "https://i.imgur.com/9T9T9T9.jpeg", "ファクトリーオートマタ\n動き続ける"),
              ("MEIKO - Nostalogic", "https://i.imgur.com/0U0U0U0.jpeg", "Nostalogic\n繰り返す記憶")]),

    "ESFJ": ("사교적이고 친절하며 헌신적인 사교적인 코디네이터",
             [("AKB48 - 헤비 로테이션 (ヘビーローテーション)", "https://i.imgur.com/1V1V1V1.jpeg", "ヘビーローテーション\n君が好きなんだ"),
              ("이키모노가카리 - 감사합니다 (ありがとう)", "https://i.imgur.com/2W2W2W2.jpeg", "ありがとう\n伝えたい言葉がある")],
             [("하츠네 미쿠 - 당신에게 바치는 러브송 (あなたに贈るラブソング)", "https://i.imgur.com/3X3X3X3.jpeg", "あなたに贈るラブソング\nこの想い届けて"),
              ("GUMI - 키쿠카이토로 (きくかいとろ)", "https://i.imgur.com/4Y4Y4Y4.jpeg", "きくかいとろ\n心をつなぐ")]),

    "ENFJ": ("카리스마 있고 이타적이며 사람들을 이끄는 지도자",
             [("DREAM COME TRUE - 사랑이 있는 곳 (愛が生まれた日)", "https://i.imgur.com/5Z5Z5Z5.jpeg", "愛が生まれた日\n二人で歩き出す"),
              ("히카루 우타다 - First Love", "https://i.imgur.com/6A6A6A6.jpeg", "First Love\nYou are always gonna be my love")],
             [("하츠네 미쿠 - 로미오와 신데렐라 (ロミオとシンデレラ)", "https://i.imgur.com/7B7B7B7.jpeg", "ロミオとシンデレラ\n禁断の愛"),
              ("GUMI - 생명의 유스티티아 (命のユースティティア)", "https://i.imgur.com/8C8C8C8.jpeg", "命のユースティティア\n歌い続ける")]),

    "ENTJ": ("확신에 차 있고 목표 지향적인 대담한 통솔자",
             [("아라시 - Love so sweet", "https://i.imgur.com/9D9D9D9.jpeg", "Love so sweet\n笑顔咲くように"),
              ("TUBE - Summer Dream", "https://i.imgur.com/0E0E0E0.jpeg", "Summer Dream\n終わらない夏")],
             [("하츠네 미쿠 - 고백 예행 연습 (告白予行練習)", "https://i.imgur.com/1F1F1F1.jpeg", "告白予行練習\n本番はこれから"),
              ("DECO*27 - 신사불성 (神っぽいな)", "https://i.imgur.com/2G2G2G2.jpeg", "神っぽいな\n何が言いたいんだか")])
}

# Streamlit 앱 구성
def main():
    st.set_page_config(page_title="MBTI 맞춤 일본 노래 추천 시스템", layout="wide")
    
    # 제목 설정
    st.title("🎼 MBTI 유형별 맞춤 일본 노래 추천 (이미지 & 가사)")
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
        keywords, jpop_data, vocaloid_data = MBTI_DATA[mbti_select]
        
        # 1. 성격 분석
        st.subheader("💡 성격 키워드")
        st.info(f"**{mbti_select}** 유형은 **{keywords}**입니다.")
        
        st.markdown("---")
        
        # 2. 유명 J-POP 추천
        st.subheader("🎤 당신의 분위기에 맞는 유명 J-POP 추천")
        for title, img_url, lyrics in jpop_data:
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(img_url, width=150, caption=f"'{title}' 이미지")
            with col2:
                st.markdown(f"### {title}")
                st.write(f"```\n{lyrics}\n```")
                st.markdown("---")
        st.caption("※ 대중적으로 많은 사랑을 받은 히트곡 위주로 선정되었습니다.")
        
        st.markdown("---")
        
        # 3. 보컬로이드 노래 추가 추천
        st.subheader("🤖 보컬로이드(VOCALOID) 노래 추가 추천")
        for title, img_url, lyrics in vocaloid_data:
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(img_url, width=150, caption=f"'{title}' 이미지")
            with col2:
                st.markdown(f"### {title}")
                st.write(f"```\n{lyrics}\n```")
                st.markdown("---")
        st.caption("※ 보컬로이드의 상징적인 명곡 및 유형과 분위기가 맞는 곡으로 선정되었습니다.")
        
        st.markdown("---")
        
        st.success(f"📌 {mbti_select} 님, 이 노래들과 함께 오늘 하루를 즐겁게 보내시길 바랍니다!")

if __name__ == "__main__":
    main()
