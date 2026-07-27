import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("MONDAY_API_KEY")
DEALS_BOARD_ID = os.getenv("DEALS_BOARD_ID")
WORK_BOARD_ID = os.getenv("WORK_BOARD_ID")

URL = "https://api.monday.com/v2"

headers = {
    "Authorization": API_KEY,
    "Content-Type": "application/json",
}


def fetch_board(board_id):
    query = f"""
    query {{
      boards(ids: {board_id}) {{
        items_page(limit: 500) {{
          items {{
            name
            column_values {{
              text
              column {{
                title
              }}
            }}
          }}
        }}
      }}
    }}
    """

    response = requests.post(
        URL,
        json={"query": query},
        headers=headers
    )

    data = response.json()

    if "errors" in data:
        raise Exception(data["errors"])

    items = data["data"]["boards"][0]["items_page"]["items"]

    rows = []

    for item in items:

        row = {
            "Deal": item["name"]
        }

        for col in item["column_values"]:
            row[col["column"]["title"]] = col["text"]

        rows.append(row)

    return pd.DataFrame(rows)


def fetch_deals():
    """
    Fetch Deal Funnel board
    """
    return fetch_board(DEALS_BOARD_ID)


def fetch_work_orders():
    """
    Fetch Work Order board
    """
    return fetch_board(WORK_BOARD_ID)