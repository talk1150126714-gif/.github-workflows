import requests
import os
import time

# ==================== 配置区 ====================
HUGGING_FACE_SPACE_URLS = [
    "https://pine6-open.hf.space/",
    "https://pine6-plan.hf.space/",     # ← 替换成你要访问的页面
    "https://pine6-open.hf.space/api/health",       # 推荐添加健康检查接口
    # "https://pine6-open.hf.space/your-other-page", # 继续添加更多
]

# 可选：每个请求之间的间隔（秒），防止请求太密集
DELAY_BETWEEN_REQUESTS = 1
# ================================================

def ping_space(url):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] Pinging: {url}")
    
    try:
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            print(f"[{timestamp}] ✅ Success! Status: {response.status_code}")
        else:
            print(f"[{timestamp}] ⚠️  Failed with status: {response.status_code}")
            
    except requests.exceptions.Timeout:
        print(f"[{timestamp}] ❌ Timeout when pinging {url}")
    except requests.exceptions.RequestException as e:
        print(f"[{timestamp}] ❌ Error pinging {url}: {e}")


if __name__ == "__main__":
    print(f"🚀 Starting multi-page ping at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Total URLs to ping: {len(HUGGING_FACE_SPACE_URLS)}\n")
    
    for url in HUGGING_FACE_SPACE_URLS:
        ping_space(url)
        if DELAY_BETWEEN_REQUESTS > 0:
            time.sleep(DELAY_BETWEEN_REQUESTS)
    
    print(f"\n✅ All pings completed at {time.strftime('%Y-%m-%d %H:%M:%S')}")
