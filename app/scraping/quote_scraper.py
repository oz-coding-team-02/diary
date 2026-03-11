import asyncio
import time

import requests
from bs4 import BeautifulSoup
from tortoise import Tortoise
import os
from dotenv import load_dotenv

cookies = {
    "PHPSESSID": os.getenv("PHPSESSID"),
    "2a0d2363701f23f8a75028924a3af643": os.getenv("COOKIE_KEY_1"),
    "e1192aefb64683cc97abb83c71057733": os.getenv("COOKIE_KEY_2")
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
#
#
# async def save_quotes_to_db(data: list[dict]):
#     """스크래핑한 명언 데이터 리스트를 받아 데이터베이스에 저장합니다."""
#     if not data:
#         print("데이터베이스에 저장할 명언이 없습니다.")
#         return
#
#     # Tortoise ORM의 bulk_create를 사용하여 여러 객체를 한 번에 효율적으로 생성합니다.
#     quotes_to_create = [Quote(**item) for item in data]
#     await Quote.bulk_create(quotes_to_create)
#     print(f"✅ {len(quotes_to_create)}개의 명언을 데이터베이스에 성공적으로 저장했습니다.")

# async def main():
#     # --- 데이터베이스 연결 설정 ---
#     # 동료분이 설정할 부분이므로, 실제 환경에 맞게 수정해야 합니다.
#     await Tortoise.init(
#         db_url="postgres://user:password@host:port/dbname",  # 실제 PostgreSQL 접속 정보로 변경해주세요.
#         modules={"models": ["__main__"]}  # 현재 파일(__main__)에 모델이 정의되어 있음을 알림
#     )
#     await Tortoise.generate_schemas()  # DB에 테이블이 없으면 생성합니다.
#
#     scraped_quotes = scrape_quotes_sync()
#     await save_quotes_to_db(scraped_quotes)
#
# if __name__ == "__main__":
#     asyncio.run(main())