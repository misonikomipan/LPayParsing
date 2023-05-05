def parsing(file_path):
    kessai_dict_list = []
    # ファイル読み込み
    with open(file_path, 'r', encoding='utf-8') as f:
        raw_text = f.read()

    # データ整形
    all_kessai_list = raw_text.split("\n\n")[1:]
    for kessai_list in all_kessai_list[1:]:
        kessai_date, kessai_tmp = kessai_list.split("\n", 1)
        oneday_kessai_list = kessai_tmp.split("]")[:-1]
        # print(kessai_date)
        for one_kessai in oneday_kessai_list:
            kessai_dict = {"date": kessai_date}
            kessai_dict["time"], kessai_dict[
                "name"], kessai_other = one_kessai.split("\t", 2)
            if kessai_other[1:9] == "LINE Pay":
                kessai_dict["type"], kessai_other = kessai_other[10:].split(
                    " ", 1)
                kessai_dict["price"], kessai_dict[
                    "state"], *kessai_others = kessai_other.split("\n")
                for kessai_other in kessai_others:
                    key, *value = kessai_other.split(": ", 1)
                    if value:
                        kessai_dict[key] = value[0]
                kessai_dict_list.append(kessai_dict)
            else:  # その他イベント
                pass
                # do nothing

    return kessai_dict_list


if __name__ == "__main__":
    print("parsing.py is called as main.")
    import os    
    # outputフォルダがなければ作成
    if not os.path.exists('./output'): os.mkdir('./output')
    # 書き込み
    with open('./output/sample_output.txt', 'w', encoding='utf-8') as f:
        kessai_dict_list = parsing(file_path := './data/data.txt')
        print(*kessai_dict_list, file=f)
