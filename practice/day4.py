import json

data = {"id": 1, "name":"Yerassyl", "tags": ["a", "b"], "active": True, "x": None }

s = json.dumps(data, ensure_ascii = False, indent = 2)
# print(s)
# print(type(s))

back = json.loads(s)
# print(back == data, type(back))

with open("data.json", "w", encoding = "utf-8") as f:
    json.dump(data, f, ensure_ascii = False, indent = 2)

with open("data.json", "r", encoding = "utf-8") as f:
    loaded = json.load(f)

# print(loaded)

try:
    json.loads("{bad json}")
except:
    print("Invalid JSON")