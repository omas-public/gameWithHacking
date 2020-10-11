# GameWithScraiping



```py

import pandas as pd

uri = 'https://xn--eckwa2aa3a9c8j8bve9d.gamewith.jp/article/show/284'
table = pd.read_html(uri, match='評価点')[0]

print(table)

```