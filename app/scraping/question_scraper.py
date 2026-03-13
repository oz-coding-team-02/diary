import requests
import time
import asyncio
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
from app.db.seeder import save_to_db

trans = GoogleTranslator(source="en", target="ko")

headers = {
    "Referer": "https://conversationstartersworld.com/deep-conversation-topics/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Whale/4.36.368.7 Safari/537.36",
    "sec-ch-ua": '"Chromium";v="144", "Whale";v="4", "Not.A/Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"macOS"',
}

response = requests.get(
    "https://conversationstartersworld.com/philosophical-questions/", headers=headers
)
response.raise_for_status()
soup = BeautifulSoup(response.text, "lxml")

trans_questions_list = []
question_box = soup.find_all("ul", class_="wp-block-list")

# 마지막에 있는 'More deep questions' 리스트 부분 제거
if len(question_box) > 0:
    question_box = question_box[:-1]

print("번역을 시작합니다...")

for question_list in question_box:
    questions = question_list.find_all("li")
    for q in questions:
        original_text = q.get_text(strip=True)
        if not original_text:
            continue

        try:
            # 번역 실행
            translated_text = trans.translate(original_text)
            trans_questions_list.append(translated_text)

            # 진행 상황 출력 (너무 길면 잘라서 출력)
            print(f"[성공] {original_text[:30]}... -> {translated_text[:30]}...")

            # 차단 방지를 위한 지연 (1초 권장)
            time.sleep(0.5)

        except Exception as e:
            print(f"[실패] {original_text[:30]}... 에러: {e}")
            # 실패 시 원문이라도 저장하거나 건너뛸 수 있음
            trans_questions_list.append(original_text)

print("\n목록:")
# print(trans_questions_list)
print(f"총 개수: {len(trans_questions_list)}")


if __name__ == "__main__":
    asyncio.run(save_to_db(trans_questions_list, "question"))
