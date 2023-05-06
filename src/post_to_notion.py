import requests
import json
import os
import sys
sys.path.append('./data')
import secret


def post_to_notion(page, debug=False):
    # リクエストヘッダーを設定
    url = f"https://api.notion.com/v1/pages"
    headers = {
        "Notion-Version": secret.VERSION,
        "Content-Type": "application/json",
        "Authorization": f"Bearer {secret.NOTION_API_KEY}",
    }

    # リクエストボディを設定
    payload = {
        "parent": {"database_id": secret.DATABASE_ID}, 
        "properties": page
    }

    # POSTリクエストを送信
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # レスポンスの内容を表示
    if debug:
        print(response.json())


# デバッグ用
if __name__ == "__main__":
    page = {
        "Title": {
            "title": [
            {
                "text": {
                    "content": "hoge"
                }
            }
            ]
        },
        "Date": {
        "date": {
            "time_zone": "Asia/Tokyo",
            "start": "2022-10-10T18:50:00",
            "end": "2022-10-11T13:00:00"
        }
        },
        "Fee": {
            "number": 1000
        },
        "Payment": {
        "select": {
            "name": "LINE Pay"
        }
        },
        "Detail": {
        "rich_text": [
            {
            "text": {
                "content": "hogehgoe"
            }
            }
        ]
        },
    }
    post_to_notion(page, debug=True)
