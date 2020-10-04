import requests

headers = {}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjAxNzc4MjM1LCJqdGkiOiJiNDRiZGVjOWRlNzY0OTVjYjcwMmFlMGE1ZmQ5YjE2YyIsInVzZXJfaWQiOjF9.NgY5yIWug_ZVhm8jLkV49JV9k6weWaRIK_dQ0kBNv8w'

r = requests.get('http://127.0.0.1:8000/paradigm', headers=headers)

print(r.text)