import json

with open('questions.json') as json_file:
    data = json.load(json_file)
    print(len(data))
