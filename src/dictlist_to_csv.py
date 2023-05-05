import os
import csv

def dictlist_to_csv(dict_list, out_file_path):
    # 読み込み
    field_name = set()
    for dict in dict_list:
        field_name |= set(dict.keys())

    # 書き込み
    output_dir = os.path.dirname(out_file_path)
    if not os.path.exists(output_dir):  # outputフォルダがなければ作成
        os.mkdir(output_dir)
    with open(out_file_path, 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_name)
        writer.writeheader()
        writer.writerows(dict_list)


if __name__ == "__main__":
    import parsing
    print("dictlist_to_csv.py is called as main.")
    # 読み込み
    dict_list = parsing.parsing('./data/data.txt')
    # 実行
    dictlist_to_csv(dict_list, './output/test.csv')
    pass