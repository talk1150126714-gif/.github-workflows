import requests
import os
import time

HUGGING_FACE_SPACE_URL = "https://huggingface.co/spaces/pine6/open"

def ping_space():
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Pinging Hugging Face Space: {HUGGING_FACE_SPACE_URL}")
    try:
        response = requests.get(HUGGING_FACE_SPACE_URL, timeout=10)
        if response.status_code == 200:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Ping successful! Status code: {response.status_code}")
        else:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Ping failed with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] An error occurred during ping: {e}")

if __name__ == "__main__":
    ping_space()
