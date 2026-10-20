import requests

r = requests.get("https://jsonplaceholder.typicode.com/todos/1")

print(r.status_code)   # 200
print(r.headers["Content-Type"])
print(r.text)          # сырой текст
print(r.json())        # уже словарь

r = requests.get(
    "https://jsonplaceholder.typicode.com/todos/1",
    params={"userID": 1},
    )

print(r.url)
print(len(r.json()))

payload = {"title": "My Note", "body": "text", "userID": 1}
r = requests.post("https://jsonplaceholder.typicode.com/posts", json = payload)
print(r.status_code)
print(r.json())

try:
    r = requests.get("https://jsonplaceholder.typicode.com/todos/1", timeout = 5)
    r.raise_for_status()
    data = r.json()
except requests.RequestException as e:
    print("Ошибка запроса", e)


def get_user_todos(user_id: int) -> list[dict]:
    try:
        r = requests.get(
            "https://jsonplaceholder.typicode.com/todos", 
            timeout = 5,
            params = {"userId": user_id}
            )
        r.raise_for_status()
        todos = r.json()
        return [c for c in todos if not c["completed"]]
    except requests.RequestException:
         return []

todos = get_user_todos(1)
print(len(todos))
print(todos[0]["title"])
print(get_user_todos(999))   # []