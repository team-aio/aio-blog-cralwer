tistory_nikname = input()

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

# 요청을 보낼 URL
# url = f'https://doongu.tistory.com/54'
url = 'https://doongu.tistory.com/rss'
print(url)
try:
    # GET 요청 보내기
    response = requests.get(url)
    # 요청이 성공적으로 완료되었는지 확인
    if response.status_code == 200:
        # print(response)
        soup = BeautifulSoup(response.text, 'html.parser')
        # 응답 내용을 JSON 형식으로 가져오기 (예를 들어, JSON 응답일 경우)
        items=soup.find_all('item')
        for item in items:
            title=item.find('title')
            link=item.find('link')
            body=item.find('description')
            # print(type(body))
            md_body = md(str(body))
            print(md_body)
        # md_body = md(str(soup))
        # print(md_body)
        #     # print(item)
        #     print('----------')
    else:
        # 요청 실패 시 상태 코드 출력
        print(f'Request failed with status code: {response.status_code}')
        
except requests.exceptions.RequestException as e:
    # 요청 중 오류 발생 시 예외 처리
    print(f'An error occurred: {e}')