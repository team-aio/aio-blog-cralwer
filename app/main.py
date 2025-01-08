from fastapi import FastAPI
import requests
from fastapi.responses import JSONResponse
import feedparser

app = FastAPI()

@app.get("/blog/tistory/{user_id}")
async def tistory(user_id: str):
    url = f'https://{user_id}.tistory.com/rss'
    try:
        rss = feedparser.parse(url)
        entries = rss["entries"]
        blog_contents = {'contents': []}
        for entry in entries:
            temp_dict = {}
            temp_dict['title'] = entry["title"]
            temp_dict['link'] = entry['link']
            temp_dict['content'] = entry['description']
            temp_dict['posted_at'] = entry['published']
            blog_contents['contents'].append(temp_dict)

        return JSONResponse(content=blog_contents)

    except requests.exceptions.RequestException as e:
        # 요청 중 오류 발생 시 예외 처리
        print(f'An error occurred: {e}')
        return {'error': f'An error occurred: {e}'}


@app.get("/blog/velog/{user_id}")
async def velog(user_id: str):
    url = f'https://v2.velog.io/rss/{user_id}'
    try:
        rss = feedparser.parse(url)
        entries = rss["entries"]
        blog_contents = {'contents': []}
        for entry in entries:
            temp_dict = {}
            temp_dict['title'] = entry["title"]
            temp_dict['link'] = entry['link']
            temp_dict['content'] = entry['description']
            temp_dict['posted_at'] = entry['published']
            blog_contents['contents'].append(temp_dict)

        return JSONResponse(content=blog_contents)

    except requests.exceptions.RequestException as e:
        # 요청 중 오류 발생 시 예외 처리
        print(f'An error occurred: {e}')
        return {'error': f'An error occurred: {e}'}