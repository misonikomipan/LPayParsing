import parsing
import os
import csv

# outputフォルダがなければ作成
if not os.path.exists('./output'): os.mkdir('./output')

# 読み込み
dict_list = parsing.parsing('./data/data.txt')
field_name = set()
for dict in dict_list:
    field_name |= set(dict.keys())

# 書き込み
with open('./output/test.csv','w',encoding='utf-8',newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = field_name)
    writer.writeheader()
    writer.writerows(dict_list)