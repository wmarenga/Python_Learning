import json

with open('a186_files_manipulating/abc.json', 'r') as file:
    d1_json = file.read()
    d1_json = json.loads(d1_json)  # Return to dictionary

for k, v in d1_json.items():
    print(k)
    for k1, v1 in v.items():
        print(k1, v1)
