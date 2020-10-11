import pandas as pd


class GameWith:
    def __init__(self, pages, keyword):
        self.base = 'https://xn--eckwa2aa3a9c8j8bve9d.gamewith.jp/article/show/'
        self.keyword = keyword
        self.monsters = self.fetchTables(pages)

    def f(self, table, target):
        rank = 'Sランク'
        acc = []
        for row in table:
            if row[1] == self.keyword:
                rank = row[0]
                continue
            acc.append([row[1], target, rank])
        return pd.DataFrame(data=acc, columns=['モンスター', '対象', 'ランク'])

    def fetch(self, page):
        uri = "{}{}".format(self.base, page[1])
        table = pd.read_html(uri, match=self.keyword)[0]       
        table = table.replace('^(.*)【.*$', r'\1', regex=True)
        return self.f(table.values.tolist(), page[0])

    def fetchTables(self, pages):
        return pd.concat([self.fetch(page) for page in pages])

    def to_csv(self, file):
        self.monsters.to_csv(file, header=True, index=False)

    def print(self):
        print(self.monsters)


def gyokurou1():
    return [
        ('アバロン', 17421)
        , ('ニライカナイ', 21474)
        , ('シャンバラ', 26860)
        , ('エデン', 34072)
        , ('黄泉', 38240)
        , ('ニルヴァーナ', 39107)
        , ("ドゥーム", 37345)
        , ('メメントモリ', 44088)
        , ('カルマ', 45509)
        , ('アカシャ', 46807)
        , ('イザナミ零', 21376)
        , ('ヤマトタケル零', 28358)
        , ('クシナダ零', 23414)
        , ('イザナギ零', 21942)
        , ('ツクヨミ零', 21943)
        , ('阿修羅', 8927)
        , ('毘沙門天', 10535)
        , ('摩利支天', 12379)
        , ('大黒天', 13704)
        , ('不動明王', 15105)
        # , ('イザナミ', 2339)
        , ('ヤマトタケル', 5097)
        , ('クシナダ', 4343)
        , ('イザナギ', 6062)
        , ('ツクヨミ', 7433)
    ]

 
if __name__ == '__main__':
    # keyword = '適正理由とおすすめポイント'
    # pages = [
    #     ('ジーク', 231459)
    # ]
    keyword = 'おすすめ適正ポイント'
    pages = gyokurou1()
    gamewith = GameWith(pages, keyword)
    gamewith.print()
    gamewith.to_csv('gyokurou1.gamewith.csv')
