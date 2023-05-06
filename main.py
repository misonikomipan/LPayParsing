import sys
import json
from copy import copy
sys.path.append('./src')
from parsing import parsing
from dictlist_to_csv import dictlist_to_csv
from post_to_notion import post_to_notion


def main(input_file_path, csv_file_path):
    page_format = json.load(open('./data/page_format.json', 'r', encoding='utf-8'))
    page_format["Payment"]["select"]["name"] = "LINE Pay"
    dict_list = parsing(input_file_path)
    
    for kessai_dict in dict_list:
        page = copy(page_format)
        page["Merchant"]["title"][0]["text"]["content"] = kessai_dict["Merchant"]
        page["Date"]["date"]["start"] = kessai_dict["date"]
        page["Date"]["date"]["end"] = None
        page["Price"]["number"] = int(kessai_dict["price"])
        page["Type"]["select"]["name"] = kessai_dict["type"]
        page["Detail"]["rich_text"][0]["text"]["content"] = ""
        post_to_notion(page, True)


main(input_file_path='./data/data.txt',
     csv_file_path='./output/sample_output.csv')
