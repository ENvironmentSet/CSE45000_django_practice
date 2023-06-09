import requests

HOST = 'http://127.0.0.1:8000'

res = requests.post(HOST + '/api-token-auth/', { 'username':'envs', 'password': 'tj020611', })
res.raise_for_status() 
token = res.json()['token'] 
print(token)
# 인증이 필요한 요청에 아래의 headers를 붙임

headers = {'Authorization' : 'Token ' + token, 'Accept' : 'application/json' }
# Post Create
data = { 
  'title' : 'Hello from python client',
  'text' : 'Hi there!!',
  'created_date' : '2022-06-07T18:34:00+09:00',
  'published_date' : '2022-06-07T18:34:00+09:00'
}
file = {'image' : open('./figure.jpg', 'rb')}
res = requests.post(HOST + '/api_root/Post/', data=data, files=file, headers=headers) 
print(res)
print(res.json())