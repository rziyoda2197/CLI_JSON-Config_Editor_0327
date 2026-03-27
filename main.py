import json

FILE = "config.json"

try:
    with open(FILE) as f:
        data = json.load(f)
except:
    data = {}

key = input("Key: ")
value = input("Value: ")

data[key] = value

with open(FILE, "w") as f:
    json.dump(data, f, indent=2)

print(data)
