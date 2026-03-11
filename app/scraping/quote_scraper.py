import time

import requests
from bs4 import BeautifulSoup

cookies = {
    "PHPSESSID": "gcnf3pdthbllseudomjoelm94p",
    "2a0d2363701f23f8a75028924a3af643": "MjExLjIzNy4xMjUuMjM1",
    "e1192aefb64683cc97abb83c71057733": "cXVvdGVz",
}

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "ko-KR,ko;q=0.9,ja-JP;q=0.8,ja;q=0.7,en-US;q=0.6,en;q=0.5",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "If-Modified-Since": "Tue, 10 Mar 2026 09:29:18 GMT",
    "Referer": "https://saramro.com/",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Whale/4.36.368.7 Safari/537.36",
    "sec-ch-ua": '"Chromium";v="144", "Whale";v="4", "Not.A/Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
}


quotes = []
for i in range(30):
    response = requests.get(
        f"https://saramro.com/quotes?page={i}", cookies=cookies, headers=headers
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")
    authors = soup.select(".bo_tit")
    contents = soup.find_all("td", attrs={"colspan": "5"})

    for a, c in zip(authors, contents):
        author = a.get_text(strip=True).split("- ")[-1]
        content = c.get_text(strip=True).split("-")[0]
        print(f'author: {author}, content: {content}')
        quotes.append({"author": author, "content": content})
        time.sleep(0.5)

print("\n목록:")
# print(quotes)
print(f'총 개수: {len(quotes)}')