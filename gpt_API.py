import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()


def main():
    URL = "https://api.openai.com/v1/chat/completions"
    OPENAI_KEY = os.getenv("OPENAI_KEY")
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_KEY}"
    }
    payload = {
        "model": "gpt-4o-mini",
        "messages" : [{"role": "user","content": "Do you have an idea for a cool catchphrase for me to use?"}]
    }
    response = requests.post(URL, data=json.dumps(payload), headers=headers)
    print(response.json()['choices'][0]['message']['content'])


if __name__ == "__main__":
    main()