import threading
import asyncio
import time
from datetime import datetime
from typing import List

def web_crawler(url, delay = 3):
    print(f"Crawler started for {url}")
    time.sleep(delay)
    print(f"crawler ended fr {url}")

    
URLS = [
    "https://ghelanikirtan.vercel.app/",
    "https://github.com/ghelanikirtan/",
    "https://ghelanik.medium.com/",
    "https://python.org/",
    "https://www.linkedin.com/in/kirtan-ghelani/",
]

threads: List[threading.Thread] = []


for url in URLS:
    t = threading.Thread(target=web_crawler, args=(url,), kwargs={'delay' : 5})
    threads.append(t)

st = datetime.now()

for t in threads:
    t.start()
    
# 
for t in threads:
    t.join()
    
et = datetime.now()

# here all the threads will be executed parallely...
print(f"Time Taken: {et-st}")
