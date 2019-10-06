import json
file = open("js.json", "r") 
data = file.loads(file)
print(data)