LOCALIZATIONS = {
    "en": {
        "score": "Score:",
        "summary_rank": "Summary Rank:",
        "eff_stat": "Eff Stat:",
        "rank": "Rank:",
    },
    "vi": {
        "score": "Điểm:",
        "summary_rank": "Xếp hạng tổng quát:",
        "eff_stat": "T.tính Đề Xuất:",
        "rank": "Hạng:",
    },
    "chs": {
        "score": "分数:",
        "summary_rank": "总排名:",
        "eff_stat": "有效词条:",
        "rank": "排名:",
    },
    "cht": {
        "score": "分數:",
        "summary_rank": "總排名:",
        "eff_stat": "有效詞條:",
        "rank": "排名:",
    },
}


def gettext(key, lang):
    if lang not in LOCALIZATIONS:
        lang = "en"
    return LOCALIZATIONS[lang].get(key, key)
