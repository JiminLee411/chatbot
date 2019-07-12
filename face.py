from decouple import config
import random
import pprint
import requests
from flask import Flask, request
# 0. 사용할 이미지 파일 가져오기
file_url = 'https://api.telegram.org/file/bot771555314:AAF5b70ljLSX2CUn9g9DZgOEx74UXHzv14c/photos/file_1.jpg'
response = requests.get(file_url, stream=True)
image = response.raw.read()
# 1. 네이버 A
naver_client_id = config('NAVER_CLIENT_ID')
naver_client_secret = config('NAVER_CLIENT_SECRET')

naver_url = 'https://openapi.naver.com/v1/vision/celebrity'

# 3. 요청보내기! POST
headers = {
    'X-Naver-Client-Id': naver_client_id,
    'X-Naver-Client-Secret': naver_client_secret
}
response = requests.post(naver_url,
                        headers=headers,
                        files={'image': image}).json()

best = response.get('faces')[0].get('celebrity')

if best.get('confidence') > 0.2:
    text = f"{best.get('confidence')*100}만큼 {best.get('value')}를 닮으셨네요~"
    
else:
    text = '사람 아닌듯;;'
print(text)