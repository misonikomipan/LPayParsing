file_path = 'data.txt'
with open(file_path, 'r', encoding='utf-8') as f:
    raw_text = f.read()

all_kessai_list = raw_text.split("\n\n")[1:]
for kessai_list in all_kessai_list[1:]:
    kessai_date, kessai_tmp = kessai_list.split("\n", 1)
    oneday_kessai_list = kessai_tmp.split("]")[:-1]
    print(kessai_date)
    for one_kessai in oneday_kessai_list:
        kessai_dict = {"date": kessai_date}
        kessai_dict["time"], kessai_dict["name"], kessai_other = one_kessai.split("\t", 2)
        if kessai_other[1:9] == "LINE Pay":
            kessai_dict["type"], kessai_other = kessai_other[10:].split(" ", 1)
            kessai_dict["price"], kessai_dict["state"], *kessai_others  = kessai_other.split("\n")
            for kessai_other in kessai_others:
                key, *value = kessai_other.split(": ", 1)
                if value:
                    kessai_dict[key] = value[0]
            print(kessai_dict)
        else: # ポイント獲得イベント
            pass
            # do nothing

