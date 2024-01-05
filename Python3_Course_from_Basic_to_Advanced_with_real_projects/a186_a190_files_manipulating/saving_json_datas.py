import json

# Explanatory video about json:
# https://www.youtube.com/watch?v=XmCrArtfjaQ

file_path = r"J:\\Github\\Dev_and_DataScience_Learning\\Python_Learning\\Python3_Course_from_Basic_to_Advanced_with_real_projects\\a186_a190_files_manipulating\\data.json"

# people = {
#     'name': 'Luiz Otávio 2',
#     'surname': 'Miranda',
#     'adresses': [
#         {'street': 'R1', 'number': 32},
#         {'street': 'R2', 'number': 55},
#     ],
#     'height': 1.8,
#     'favorite_numbers': (2, 4, 6, 8, 10),
#     'dev': True,
#     'nothing': None,
# }

# json.dump  => for file
# json.dumps => for string

# ! To create a json file:

# with open(file_path, 'w', encoding='utf8') as file:
#     json.dump(
#         people,
#         file,
#         # using ascii is more compatible (ensure_ascii=True). ensure_ascii=False (with accentuation)
#         ensure_ascii=False,
#         indent=2,  # to format by indented lines.
# )

# ! To convert from file to a variable:

with open(file_path, 'r', encoding='utf8') as file:
    people = json.load(file)
    print(people)
    # print(type(people))
    print(people['name'])
