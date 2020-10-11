import pandas as pd

uri = 'https://xn--eckwa2aa3a9c8j8bve9d.gamewith.jp/article/show/284'
table = pd.concat(pd.read_html(uri, match='評価点'))              # すべての属性を取得

table = table.drop(columns='キャラ')                              
table = table[table['名前と入手方法'].str.contains('）ガチャ　')]
table = table.sort_values('評価点', ascending=False)

today = pd.to_datetime('today').strftime('%Y%m%d')                # 今日の日付
table.to_csv(f'./gw.{today}.csv', index=False, encoding="utf-8")  # ファイルに書き込み

