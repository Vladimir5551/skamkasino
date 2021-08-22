import json


def language(self, lang):
    main = ((self.gamelabel, "gamelabel"), (self.gamelabel2, "gamelabel2"), (self.balance, "balance"),
            (self.btn2, "btn2"), (self.btn3, "btn3"), (self.btn4, "btn4"), (self.btn5, "btn5"),
            (self.gamebtn, "gamebtn"), (self.gamebtn2, "gamebtn2"), (self.btn1, "btn1"))

    with open('json/config.json', 'r', encoding='utf-8') as json_language:
        jsonLang = json.load(json_language)

    jsonLang['Language'] = lang
    with open('json/config.json', 'w', encoding='utf-8') as json_language:
        json.dump(jsonLang, json_language, indent=3, ensure_ascii=False)

    with open('json/language.json', 'r', encoding='utf-8') as json_language:
        json_g1 = json.load(json_language)
        if lang == 'russian':
            json_way = json_g1['russian']
        else:
            json_way = json_g1['english']
    for i in main:
        i[0].text = json_way['Window'][i[1]]