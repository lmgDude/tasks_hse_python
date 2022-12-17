import pandas as pd

kdrama_info ={'Ojingeo geim': {'name': 'Игра в кальмара', 'genre': 'триллер, драма', 'age restrictions': 18, 'year': 2021,
                  'actors': ['Ли Джон-джэ', 'Пак Хэ-су', 'О Ён-су', 'Чон Хо-ён', 'Хо Сон-тхэ', 'Анупам Трипати',
                             'Ким Джу-рён', 'Ви Ха-джун', 'Ю Сон-джу', 'Ли Ю-ми'], 'rating': 7.5,
                  'review': 'Сон Ги-хун уже немолод, разведён, по уши погряз в долгах и сидит на шее у старенькой '
                            'матери. Даже выигранные на скачках деньги в его руках долго не задерживаются, '
                            'и однажды он встречает в метро загадочного незнакомца, который сначала предлагает '
                            'сыграть в детскую игру, а затем вручает Ги-хуну немалую сумму и визитку. Но радость '
                            'мужчины сменятся отчаянием, когда он узнаёт, что бывшая жена с новым мужем собираются '
                            'увезти его дочь в Америку. Он звонит по номеру с визитки и становится последним '
                            'участником тайных игр на выживание с призом в 40 миллионов долларов. Среди товарищей по '
                            'несчастью оказываются его друг детства — прогоревший финансист, бандит, смертельно '
                            'больной старик, северокорейская перебежчица, иммигрант из Пакистана и многие другие '
                            'отчаянно нуждающиеся в деньгах.'},
 'Dokkaebi': {'name': 'Демон', 'genre': 'фэнтези, мелодрама, драма, комедия', 'age restrictions': 16, 'year': 2016,
              'actors': ['Кон Ю', 'Ким Го-ын', 'Ли Дон-ук', 'Ю Ин-на', 'Юк Сон-джэ', 'Ли Эль', 'Чо У-джин',
                         'Ким Сон-гём', 'Пак Хи-бон', 'Хан Со-джин'], 'rating': 8.6,
              'review': 'Бессмертный демон токкэби много лет живет среди смертных и порядком устал от жизни. Но если '
                        'ты волшебное существо, есть лишь один способ поставить точку и покинуть бренный мир — '
                        'жениться на смертной. Избранницей демона становится девушка, которая может видеть призраков. '
                        'А ангел смерти, чья задача провожать души умерших в загробный мир, тем временем потерял '
                        'память.'},
 'W': {'name': 'Параллельные миры', 'genre': 'мелодрама, фэнтези, триллер', 'age restrictions': 16, 'year': 2016,
       'actors': ['Ли Джон-сок', 'Хан Хё-джу', 'Чон Ю-джин', 'Кан Ги-ён', 'Ким И-сон', 'Ли Щи-он', 'Ли Тхэ-хван',
                  'Пак Вон-сан', 'Хо Джон-до', 'Хван Сок-чон'], 'rating': 8.1,
       'review': 'История о странном и загадочном романе между парнем Кан-чхолем, который очень богат, но существует '
                 'только в вэб-комиксе «W», и девушкой О Ён-джу, которая является хирургом в реальном мире.'},
 'Yeosingangrim': {'name': 'Истинная красота', 'genre': 'мелодрама, комедия', 'age restrictions': 16, 'year': 2020,
                   'actors': ['Мун Га-ён', 'Чха Ын-у', 'Хван Ин-ёп', 'Пак Ю-на', 'Лим Сэ-ми', 'Пак Хо-сан', 'О И-щик',
                              'Кан Мин-а', 'Щин Джэ-хви', 'Чон Хе-вон'], 'rating': 8.2,
                   'review': 'Старшеклассница Лим Джу-гён с комплексом по поводу своей внешности привыкла краситься и '
                             'достигла в этом деле определённого мастерства. Она начинает встречаться с двумя самыми '
                             'видными парнями.'}}


def get_info(kdrama_info, *args, info="review"):
    all_info = info.split(', ')
    if 'name' in all_info:
        all_info.remove('name')
    if 'year' in all_info:
        all_info.remove('year')
    all_years = sorted([*args])
    new_info = []
    for name in kdrama_info:
        if len(all_years) == 1:
            if kdrama_info[name]['year'] >= all_years[0]:
                kdrama_info[name]['korean name'] = name
                new_info.append(kdrama_info[name])
        elif len(all_years) == 2:
            if all_years[0] <= kdrama_info[name]['year'] <= all_years[1]:
                kdrama_info[name]['korean name'] = name
                new_info.append(kdrama_info[name])
        elif len(all_years) == 3:
            if kdrama_info[name]['year'] in all_years:
                kdrama_info[name]['korean name'] = name
                new_info.append(kdrama_info[name])

    df = pd.DataFrame.from_records(new_info, columns=['year', 'name'] + all_info).sort_values(by='year', ascending=True)
    df = df.set_index(pd.Index([i for i in range(0, df.shape[0])]))
    return df if df.shape[0] != 0 else 'По Вашему запросу ничего не найдено'
