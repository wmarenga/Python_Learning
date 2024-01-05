import json

file_path = r"J:\\Github\\Dev_and_DataScience_Learning\\Python_Learning\\Python3_Course_from_Basic_to_Advanced_with_real_projects\\a186_a190_files_manipulating\\data.json"

with open(file_path, 'r', encoding='utf8') as file:
    d1_json = file.read()
    d1_json = json.loads(d1_json)  # Return to dictionary

for k, v in d1_json.items():
    print(k)
    print(k)
