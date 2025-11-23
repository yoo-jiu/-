import streamlit as st

# 유튜브 썸네일을 가져오는 헬퍼 함수
def get_yt_thumb(video_id):
    # 썸네일 로딩의 안전성을 위해 'mqdefault.jpg'를 사용합니다.
    if video_id == "NONE":
        # 이미지가 없을 때 보여줄 기본 이미지
        return "https://images.unsplash.com/photo-1507838153414-b4b713384ebd?ixlib=rb-1.2.1&auto=format&fit=crop&w=150&q=80"
    return f"https://img.youtube.com/vi/{video_id}/mqdefault.jpg"

# 16가지 MBTI 유형별 데이터 (모든 ID 11자리로 안정화 완료)
MBTI_DATA = {
    "ISTJ": ("현실적, 논리적, 책임감 강한 원칙주의자",
             [("아이묭 - 마리골드", "0xSiBpUdW4E", "麦わらの帽子の君が\n揺れるたびに 揺れるたびに"),
              ("히라이 켄 - POP STAR", "WpyeP6o5z0k", "I wanna be a pop star\n君をもっと夢中にさせてあげるからね")],
             [("하츠네 미쿠 - 멜트", "YlEfJaT_7eU", "メルト 溶けてしまいそう\n好きだなんて 絶対言えない"),
              ("카가미네 린 - 로스트 원의 호곡", "8oBV3jPTW4s", "一体全体何を学べば\nテストの点数は上がるんですか")]),

    "ISFJ": ("따뜻하고 헌신적이며 조용하고 성실한 수호자",
             [("요네즈 켄시 - Lemon", "SX_ViT4Ra7k", "あの日の悲しみさえ\nあの日の苦しみさえ"),
              ("Aimer - 잔향산가 (귀멸의 칼날)", "tLQLa6lM3Us", "誰が為に響く 不協和音\nざわめく波紋 蹴散らして")],
             [("하츠네 미쿠 - 사랑은 전쟁", "f4jZ3h_NqI0", "恋する乙女は 止まれないの\n暴走モード 突入よ"),
              ("하츠네 미쿠 - 마인드 브랜드", "CLDEer75Gxc", "壊してしまえ こんな精神も\n忘れてしまえ こんな感情も")]),

    "INFJ": ("통찰력 있고 창의적이며 확고한 신념을 가진 예언자",
             [("King Gnu - 백일 (Hakujitsu)", "ony539T074w", "真っ白な日々に舞い降りた\n黒い雨が 洗い流した"),
              ("키무라 유미 - 언제나 몇 번이라도 (센과 치히로)", "IWqDcwM2Qk0", "呼んでいる 胸のどこか奥で\nいつも心踊る 夢を見たい")],
             [("하츠네 미쿠 - 천본앵", "shs0rAiwsGQ", "千本桜 夜ニ紛レ\n君ノ歌声 モガセヨ"),
              ("하츠네 미쿠 - 꼭두각시 피에로", "HuQ6pi5JPbw", "からくりピエロ 踊る夜\n君の心 弄ぶように")]),

    "INTJ": ("지적 호기심이 많고 전략적이며 독립적인 설계자",
             [("RADWIMPS - 전전전세 (너의 이름은)", "PDSkFeMVNFs", "君のゼンゼンゼン世から僕は\n君を探し始めたよ"),
              ("후지이 카제 - 죽는 게 나아 (Shinunoga E-Wa)", "TcLLpZBWsCk", "死ぬのがいいわ あなたとこのまま\nお揃いの地獄へ落ちよう")],
             [("하츠네 미쿠 - 월즈 엔드 댄스홀", "0y6K1N0kO_0", "世界の端っこで\nさあ踊り明かそう"),
              ("하츠네 미쿠 - 망상감상대상연맹", "e1xCOsgWg0M", "妄想感傷代償連盟\nきっと僕らはそう")]),
    
    "ISTP": ("과묵하고 분석적이며 도구를 잘 다루는 만능 재주꾼",
             [("Official髭男dism - Pretender", "TQ8WlA2GXxc", "僕ら恋する何者にも\nなれなかったな"),
              ("LiSA - 홍련화 (귀멸의 칼날)", "CwkzK-F0Y00", "強く 強くなれる理由を知った\n僕を連れて進め")],
             [("하츠네 미쿠 - 혼자 놀이 엔비 (Hitorinbo Envy)", "Uy3M82s4wUA", "あのね、あたしは\n独りんぼエンヴィー"),
              ("하츠네 미쿠 - Tell Your World", "PqJNc9KVIZE", "伝えたい 想いは世界へ\nきっと届くから")]),

    "ISFP": ("호기심 많고 예술적이며 온화한 성격의 모험가",
             [("Vaundy - 괴수의 꽃노래", "ysSxxIqKNN0", "怪獣の歌が響く\n僕らの世界で"),
              ("나카지마 미유키 - 실", "du90qO_x0j0", "縦の糸はあなた 横の糸は私\n逢うべき糸に 出会えることを")],
             [("하츠네 미쿠 - 노래에 형태는 없지만", "IpY3a2K_d_4", "歌に形は無いけれど\n君の心を揺らすはず"),
              ("메구리네 루카 - Just Be Friends", "VoPzP-MwcLI", "Just Be Friends\nただそれだけ")]),

    "INFP": ("낭만적이고 사려 깊으며 이상적인 가치 추구자",
             [("YOASOBI - 밤을 달리다", "x8VYWazR5mE", "沈むように溶けてゆくように\n二人だけの空が広がる夜に"),
              ("오자키 유타카 - I Love You", "h9i0Q48-WdY", "I LOVE YOU I LOVE YOU I LOVE YOU\n届かない歌を唄う")],
             [("하츠네 미쿠 - 이별만이 인생이다", "C9tvQPP_1I8", "別れだけが人生だ\nそうやって生きてきた"),
              ("flower - 샤를", "TA5OFS_y9bE", "シャルル シャルル シャルル\n笑って 笑って")]),

    "INTP": ("조용하고 분석적이며 끊임없이 지식을 탐구하는 사색가",
             [("Eve - 회회기담 (주술회전)", "1tk1pqwrOys", "呪いの廻るこの世界で\n僕は君を救えるのか"),
              ("Mrs. GREEN APPLE - 푸름과 여름", "m34DPnRpBww", "青い夏 空に舞う\n白い雲 掴もうよ")],
             [("하츠네 미쿠 - 마트료시카", "HOz-9FzIDf0", "マトリョシカ マトリョシカ\n踊り狂った"),
              ("카후 - 포니 (Phony)", "9QLT1Aw_45s", "絶望の雨はあたしの傘を突いて\n濡らしてゆくわ")]),

    "ESTP": ("개방적이고 행동 지향적이며 타협을 모르는 사업가",
             [("DISH// - 고양이 (Neko)", "gsT6eKsnT0M", "猫になった 君と二人\n愛し合ったのは幻かな"),
              ("B'z - ULTRA SOUL", "pJD6m_7y8_4", "ULTRA SOUL\nHEY!")],
             [("하츠네 미쿠 - Calc.", "2v9Jd-nJ2d0", "あぁ 計算通りいかない\n僕らの恋路"),
              ("하츠네 미쿠 - 에일리언 에일리언", "Sum7n9rU_n0", "エイリアン わたしエイリアン\nあなたの心を惑わせる")]),

    "ESFP": ("재미있고 에너지가 넘치며 즉흥적인 연예인",
             [("SEKAI NO OWARI - RPG", "Mi9uNu35Gmk", "空は青く澄み渡り 海を目指して歩く\n怖くても大丈夫 僕らはもう一人じゃない"),
              ("녹황색사회 - Mela!", "aRdHX9JxdXE", "今なんじゃない？\nメラメラとたぎれ")],
             [("하츠네 미쿠 - 미쿠미쿠하게 해줄게♪", "06d8Swc6h4s", "みっくみくにしてあげる\n歌ってあげる"),
              ("GUMI - KING", "cm-l2h6GB8Q", "You are KING\nYou are KING")]),

    "ENFP": ("열정적이고 창의적이며 사회생활이 활발한 활동가",
             [("back number - 해피 엔드", "Hz3Xj9w6k6E", "ハッピーエンド\n私じゃない誰かを"),
              ("아야카 - 무지개색 (Nijiiro)", "w3FY2r1TLLM", "これからはじまるあなたの物語\nずっと長く道は続くよ")],
             [("하츠네 미쿠 - 월드 이즈 마인", "EuJ6UR_pD5s", "世界で一番お姫様\n気づいてよね"),
              ("flower - 굿바이 선언", "dVjFQ5_W_sA", "グッバイ宣言\nバイバイしたいの")]),

    "ENTP": ("지적이고 논쟁을 즐기는 독창적인 발명가",
             [("ONE OK ROCK - Wherever you are", "4uF7g32_8vM", "Wherever you are\nI'll always be with you"),
              ("Ado - 시끄러워 (Usseewa)", "Qp3b-RXtz4w", "うっせぇわ うっせぇわ うっせぇわ\nあなたが思うより健康です")],
             [("하츠네 미쿠 - 뇌장작렬 걸", "Ey_N3dDJQoU", "脳漿炸裂ガール\n狂い咲け"),
              ("카가미네 린 - 악의 딸", "hJ6A-kT-o1s", "悪ノ娘\nまたもや傲慢に")]),

    "ESTJ": ("실용적이고 체계적이며 현실적인 관리자",
             [("호시노 겐 - 코이 (사랑)", "jhOVibLEDhA", "恋ダンス踊るように\n二人で歩こう"),
              ("Perfume - FLASH", "q6D8j005pp0", "Lightning\n最高速で駆け抜けて")],
             [("하츠네 미쿠 - 공명하게 해 (Hibikase)", "RutR7Y-sA9A", "感覚を共鳴させて\n深く深く"),
              ("MEIKO - Nostalogic", "Yu_d7j-e65E", "Nostalogic\n繰り返す記憶")]),

    "ESFJ": ("사교적이고 친절하며 헌신적인 사교적인 코디네이터",
             [("AKB48 - 헤비 로테이션", "lkHlnWFnA0c", "ヘビーローテーション\n君が好きなんだ"),
              ("이키모노가카리 - 감사합니다 (Arigato)", "vz_x3j-X6Y8", "ありがとう\n伝えたい言葉がある")],
             [("HoneyWorks - 금요일의 아침인사", "Ix54zK60u_I", "おはようのオーディションして\n髪型もバッチリOK"), # ID 수정 완료
              ("하츠네 미쿠 - 사랑의 말 III (Ai Kotoba III)", "WptXk39wiIQ", "僕らだけの愛の言葉\nずっと忘れないよ")]), # ID 수정 완료

    "ENFJ": ("카리스마 있고 이타적이며 사람들을 이끄는 지도자",
             [("DREAMS COME TRUE - LOVE LOVE LOVE", "qZcMhtDm-kY", "ねぇどうして\nすごく愛してるのに"),
              ("히카루 우타다 - First Love", "_Q5-4yMi-xg", "First Love\nYou are always gonna be my love")],
             [("하츠네 미쿠 - 로미오와 신데렐라", "04JCv2rTpzw", "ロミオとシンデレラ\n禁断の愛"),
              ("GUMI - 생명의 유스티티아", "d7Hn-1Ey7eY", "命のユースティティア\n歌い続ける")]),

    "ENTJ": ("확신에 차 있고 목표 지향적인 대담한 통솔자",
             [("YOASOBI - 아이돌 (Idol)", "OTQ2c0K-F-A", "無敵の笑顔で荒らすメディア\n知りたいその秘密"),
              ("요네즈 켄시 - KICK BACK (체인소맨)", "M2cck-ZTVkW", "努力 未来 A BEAUTIFUL STAR\nランドリー今日はガラ空きで")],
             [("하츠네 미쿠 - 고백 예행연습", "Yi8L-P-N_A4", "告白予行練習\n本番はこれから"),
              ("하츠네 미쿠 - 신 같네 (God-ish)", "e1xCOsgWg0M", "神っぽいな\n何が言いたいんだか")])
}

# Streamlit 앱 구성
def main():
    st.set_page_config(page_title="MBTI 맞춤 일본 노래 추천 시스템", layout="wide")
    
    # 제목 설정
    st.title("🎼 MBTI 유형별 맞춤 일본 노래 추천")
    st.markdown("이미지 파일 없이 **유튜브 썸네일**을 실시간으로 가져옵니다.")
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
        for title, video_id, lyrics in jpop_data:
            col1, col2 = st.columns([1, 2])
            with col1:
                # 썸네일 표시
                st.image(get_yt_thumb(video_id), width=180, caption="YouTube Thumbnail")
            with col2:
                st.markdown(f"### {title}")
                st.code(lyrics, language="text") 
                st.markdown("---")
        st.caption("※ 썸네일은 유튜브 공식 영상 또는 인기 영상에서 가져왔습니다.")
        
        st.markdown("---")
        
        # 3. 보컬로이드 노래 추가 추천
        st.subheader("🤖 보컬로이드(VOCALOID) 노래 추가 추천")
        for title, video_id, lyrics in vocaloid_data:
            col1, col2 = st.columns([1, 2])
            with col1:
                # 썸네일 표시
                st.image(get_yt_thumb(video_id), width=180, caption="YouTube Thumbnail")
            with col2:
                st.markdown(f"### {title}")
                st.code(lyrics, language="text") 
                st.markdown("---")
        st.caption("※ 보컬로이드의 상징적인 명곡 및 유형과 분위기가 맞는 곡으로 선정되었습니다.")
        
        st.markdown("---")
        
        st.success(f"📌 {mbti_select} 님, 이 노래들과 함께 오늘 하루를 즐겁게 보내시길 바랍니다!")

if __name__ == "__main__":
    main()
