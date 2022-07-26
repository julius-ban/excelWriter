# python 3.9
import requests
import pandas as pd
import time

# 읽어올 엑셀 파일 지정
filename = 'result.xlsx'

# 엑셀 파일 읽어 오기
df = pd.read_excel(filename, engine='openpyxl', usecols=[1])
tuples = df.itertuples()
idx = 0
for tup in tuples:
    url_items = "URL 주소" + tup[1]
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url_items, headers=headers)
    morpheme = response.json()['result']['data'][4]['value']
    df.at[idx, '받아온 결과를 입력할 컬럼'] = morpheme
    print(morpheme)
    idx += 1
    time.sleep(1)

df.to_excel(excel_writer=filename)