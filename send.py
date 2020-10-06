import requests

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAxODg3MjIxLCJqdGkiOiI5MWVmYjdlNTIxMDY0N2JlOTEwNzdmMmZhNzhmMzFkMCIsInVzZXJfaWQiOjF9.MV4TRj0fi_w1lOSkyCgMJBc3qx4t44a6w_tWm10Duck'

r = requests.get('http://127.0.0.1:8000/paradigm', headers=headers)

print(r.text)