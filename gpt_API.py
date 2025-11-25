import json
import requests
import open_metro_API_integration
import os
from dotenv import load_dotenv

load_dotenv()

WEATHER_DATA = open_metro_API_integration.main()

def main():
    user_question = input("What is your question?: ")

    PROMT = f"""Here is the weather for today:
    {WEATHER_DATA}
    Here is the question from a user:
    {user_question}
    Please answer the question."""

    URL = "https://api.openai.com/v1/chat/completions"
    OPENAI_KEY = os.getenv("OPENAI_KEY")
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_KEY}"
    }
    payload = {
        "model": "gpt-4o-mini",
        "messages" : [{"role": "user","content": PROMT}]
    }
    response = requests.post(URL, data=json.dumps(payload), headers=headers)
    print(response.json()['choices'][0]['message']['content'])


if __name__ == "__main__":
    main()