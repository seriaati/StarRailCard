# Copyright 2024 DEViantUa <t.me/deviant_ua>
# All rights reserved.

SUPPORTED_LANGUAGES = {
    "cht": "cht",
    "cn": "cn",
    "de": "de",
    "en": "en",
    "es": "es",
    "fr": "fr",
    "id": "id",
    "jp": "jp",
    "kr": "kr",
    "pt": "pt",
    "ru": "ru",
    "th": "th",
    "vi": "vi",
    "ua": "ua",
}


translationLang = {
    "en": {
        "lvl": "LVL",
        "AR": "AR",
        "WL": "WL",
        "AC": "Achievements",
        "AB": "Abyss",
        "score": "Score:",
        "summary_rank": "Summary Rank:",
        "eff_stat": "Eff Stat:",
        "rank": "Rank:",
    },
    "ru": {
        "lvl": "Уровень",
        "AR": "РП",
        "WL": "УМ",
        "AC": "Достижения",
        "AB": "Бездна",
    },
    "ua": {
        "lvl": "Рівень",
        "AR": "РП",
        "WL": "РС",
        "AC": "Досягнення",
        "AB": "Безодня",
    },
    "vi": {
        "lvl": "Cấp độ ",
        "AR": "AR",
        "WL": "WL",
        "AC": "Thành tích ",
        "AB": "Vực thẳm",
        "score": "Điểm:",
        "summary_rank": "Tổng quát:",
        "eff_stat": "Đề xuất:",
        "rank": "Hạng:",
    },
    "th": {
        "lvl": "ระดับ ",
        "AR": "AR",
        "WL": "WL",
        "AC": " ความสำเร็จ ",
        "AB": "Abyss",
    },
    "pt": {
        "lvl": "Nível ",
        "AR": "AR",
        "WL": "WL",
        "AC": " Conquistas ",
        "AB": "Abismo",
    },
    "kr": {
        "lvl": "레벨 ",
        "AR": "AR",
        "WL": "WL",
        "AC": "업적",
        "AB": "어비스",
    },
    "jp": {
        "lvl": "レベル ",
        "AR": "AR",
        "WL": "WL",
        "AC": "アチーブメント",
        "AB": "アビス",
        "score": "スコア:",
        "summary_rank": "総合ランク:",
        "rank": "ランク:",
    },
    "zh": {
        "lvl": "等級",
        "AR": "AR",
        "WL": "WL",
        "AC": "成就總數",
        "AB": "深境螺旋",
        "score": "分數:",
        "summary_rank": "總排名:",
        "eff_stat": "有效詞條:",
        "rank": "排名:",
    },
    "cn": {
        "lvl": "等级",
        "AR": "AR",
        "WL": "WL",
        "AC": "成就总数",
        "AB": "深境螺旋",
        "score": "分数:",
        "summary_rank": "总排名:",
        "eff_stat": "有效词条:",
        "rank": "排名:",
    },
    "id": {"lvl": "Level ", "AR": "AR", "WL": "WL", "AC": " Prestasi ", "AB": " Abyss"},
    "fr": {
        "lvl": "Niveau ",
        "AR": "AR",
        "WL": "WL",
        "AC": " Réalisations ",
        "AB": " Abîme",
    },
    "es": {"lvl": "Nivel ", "AR": "AR", "WL": "WL", "AC": " Logros ", "AB": " Abismo"},
    "de": {"lvl": "Level ", "AR": "AR", "WL": "WL", "AC": " Erfolge ", "AB": " Abyss"},
    "chs": {
        "lvl": "等级",
        "AR": "AR",
        "WL": "WL",
        "AC": "成就总数",
        "AB": "深境螺旋",
        "score": "分数:",
        "summary_rank": "总排名:",
        "eff_stat": "有效词条:",
        "rank": "排名:",
    },
    "cht": {
        "lvl": "等級",
        "AR": "AR",
        "WL": "WL",
        "AC": "成就總數",
        "AB": "深境螺旋",
        "score": "分數:",
        "summary_rank": "總排名:",
        "eff_stat": "有效詞條:",
        "rank": "排名:",
    },
}


class Translator:
    def __init__(self, lang) -> None:
        self.lang = str(lang)

    def __getattr__(self, name):
        if self.lang not in translationLang:
            lang = "en"
        else:
            lang = self.lang

        if name not in translationLang[lang]:
            return translationLang["en"].get(name, name)
        return translationLang[lang][name]
