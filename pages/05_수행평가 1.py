#include <stdio.h>
#include <string.h>

typedef struct {
    char title[200];
    char lyric[300];
    char ko[300];
} Song;

typedef struct {
    char mbti[10];
    Song jpop[2];
    Song vocaloid[1];
} MBTI_Info;

int main() {
    MBTI_Info data[16] = {

        {
            "ISTJ",
            {
                {"Subtitle - Official髭男dism", "하이라이트 가사 A", "한국어 번역 A"},
                {"Lemon - 米津玄師", "하이라이트 가사 A", "한국어 번역 A"}
            },
            {
                {"シャルル - バルーン", "하이라이트 가사 A", "한국어 번역 A"}
            }
        },

        {
            "ISFJ",
            {
                {"水平線 - back number", "하이라이트 가사 A", "한국어 번역 A"},
                {"だから僕は音楽を辞めた - ヨルシカ", "하이라이트 가사 A", "한국어 번역 A"}
            },
            {
                {"愛言葉III - DECO*27", "하이라이트 가사 A", "한국어 번역 A"}
            }
        },

        {
            "INFJ",
            {
                {"夜に駆ける - YOASOBI", "하이라이트 가사 A", "한국어 번역 A"},
                {"Brave Shine - Aimer", "하이라이트 가사 A", "한국어 번역 A"}
            },
            {
                {"アスノヨゾラ哨戒班 - Orangestar", "하이라이트 가사 A", "한국어 번역 A"}
            }
        },

        {
            "INTJ",
            {
                {"unravel - TK", "하이라이트 가사 A", "한국어 번역 A"},
                {"逆光 - Ado", "하이라이트 가사 A", "한국어 번역 A"}
            },
            {
                {"ベノム - かいりきベア", "하이라이트 가사 A", "한국어 번역 A"}
            }
        },

        {
            "ISTP",
            {
                {"怪物 - YOASOBI", "하이라이트 가사 A", "한국어 번역 A"},
                {"不可幸力 - Vaundy", "하이라이트 가사 A", "한국어 번역 A"}
            },
            {
                {"ブリキノダンス - 日向電工", "하이라이트 가사 A", "한국어 번역 A"}
            }
        },

        {
            "ISFP",
            {
                {"花に亡霊 - ヨルシカ", "하이라이트 가사 A", "한국어 번역 A"},
                {"スパークル - RADWIMPS", "하이라이트 가사 A", "한국어 번역 A"}
            },
            {
                {"メルト - supercell", "하이라이트 가사 A", "한국어 번역 A"}
            }
        },

        {
            "INFP",
            {
                {"春泥棒 - ヨルシカ", "하이라이트 가사 A", "한국어 번역 A"},
                {"ドラマツルギー - Eve", "하이라이트 가사 A", "한국어 번역 A"}
            },
            {
                {"カゲロウデイズ - じん", "하이라이트 가사 A", "한국어 번역 A"}
            }
        },

        {
            "INTP",
            {
                {"KING - Kanaria", "하이라이트 가사 A", "한국어 번역 A"},
                {"堕天 - Creepy Nuts", "하이라이트 가사 A", "한국어 번역 A"}
            },
            {
                {"ドクハク - 水野あつ", "하이라이트 가사 A", "한국어 번역 A"}
            }
        },

        {
            "ESTP",
            {
                {"新時代 - Ado", "하이라이트 가사 A", "한국어 번역 A"},
                {"紅蓮華 - LiSA", "하이라이트 가사 A", "한국어 번역 A"}
            },
            {
                {"威風堂々 - 梅とら", "하이라이트 가사 A", "한국어 번역 A"}
            }
        },

        {
            "ESFP",
            {
                {"打上花火 - DAOKO × 米津玄師", "하이라이트 가사 A", "한국어 번역 A"},
                {"三原色 - YOASOBI", "하이라이트 가사 A", "한국어 번역 A"}
            },
            {
                {"脱法ロック - Neru", "하이라이트 가사 A", "한국어 번역 A"}
            }
        },

        {
            "ENFP",
            {
                {"怪獣の花唄 - Vaundy", "하이라이트 가사 A", "한국어 번역 A"},
                {"Habit - SEKAI NO OWARI", "하이라이트 가사 A", "한국어 번역 A"}
            },
            {
                {"テオ - Omoi", "하이라이트 가사 A", "한국어 번역 A"}
            }
        },

        {
            "ENTP",
            {
                {"阿修羅ちゃん - Ado", "하이라이트 가사 A", "한국어 번역 A"},
                {"ナンセンス文学 - Eve", "하이라이트 가사 A", "한국어 번역 A"}
            },
            {
                {"ヒバナ - DECO*27", "하이라이트 가사 A", "한국어 번역 A"}
            }
        },

        {
            "ESTJ",
            {
                {"炎 - LiSA", "하이라이트 가사 A", "한국어 번역 A"},
                {"CORE PRIDE - UVERworld", "하이라이트 가사 A", "한국어 번역 A"}
            },
            {
                {"劣等上等 - Giga", "하이라이트 가사 A", "한국어 번역 A"}
            }
        },

        {
            "ESFJ",
            {
                {"シル・ヴ・プレジデント - P丸様。", "하이라이트 가사 A", "한국어 번역 A"},
                {"可愛くてごめん - HoneyWorks", "하이라이트 가사 A", "한국어 번역 A"}
            },
            {
                {"桃源恋歌 - GARNiDELiA", "하이라이트 가사 A", "한국어 번역 A"}
            }
        },

        {
            "ENFJ",
            {
                {"群青 - YOASOBI", "하이라이트 가사 A", "한국어 번역 A"},
                {"残響散歌 - Aimer", "하이라이트 가사 A", "한국어 번역 A"}
            },
            {
                {"ゴーストルール - DECO*27", "하이라이트 가사 A", "한국어 번역 A"}
            }
        },

        {
            "ENTJ",
            {
                {"うっせぇわ - Ado", "하이라이트 가사 A", "한국어 번역 A"},
                {"不可逆リプレイス - MY FIRST STORY", "하이라이트 가사 A", "한국어 번역 A"}
            },
            {
                {"ヴィラン - 日向電工", "하이라이트 가사 A", "한국어 번역 A"}
            }
        }
    };

    char input[10];
    printf("당신의 MBTI를 입력하세요 (예: INFJ): ");
    scanf("%s", input);

    int found = 0;

    for (int i = 0; i < 16; i++) {
        if (strcmp(input, data[i].mbti) == 0) {
            found = 1;
            printf("\n===== %s 일본 노래 추천 =====\n", data[i].mbti);

            printf("\n[ J-POP 추천곡 ]\n");
            for (int j = 0; j < 2; j++) {
                printf("- %s\n", data[i].jpop[j].title);
            }

            printf("\n[ 보컬로이드 추천곡 ]\n");
            printf("- %s\n", data[i].vocaloid[0].title);

            break;
        }
    }

    if (!found) {
        printf("지원하지 않는 MBTI입니다.\n");
    }

    return 0;
}
