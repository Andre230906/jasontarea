import json

with open ("json.json","r") as f:
    json_object=json.loads(f.read())
    
print(json_object)