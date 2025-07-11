import requests
from datetime import datetime, timezone
import time

ticker = input("Enter the ticker symbol: ")
from_date = input("Enter start date in yyyy/mm/dd format: ")
to_date = input("Enter end date in yyyy/mm/dd format: ")

from_datetime = datetime.strptime(from_date, '%Y/%m/%d')
to_datetime = datetime.strptime(to_date, '%Y/%m/%d')

from_epoch = int(from_datetime.replace(tzinfo=timezone.utc).timestamp())
to_epoch = int(to_datetime.replace(tzinfo=timezone.utc).timestamp())

url = (
    f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}"
    f"?period1={from_epoch}&period2={to_epoch}"
    f"&interval=1d&events=history&includeAdjustedClose=true"
)

print("Generated URL:", url)

# headers mimimc a real browser
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/114.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive",
    "DNT": "1",
}


response = requests.get(url, headers=headers)
if response.status_code == 200:
    with open('data.csv', 'wb') as file:
        file.write(response.content)
    print("Data saved to data.csv")
else:
    print("Failed to fetch data:", response.status_code)
    print(response.text)
