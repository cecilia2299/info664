import json
res = {}
with open ('Artworks.json') as file:
    json_file = json.load(file)
    for entry in json_file:
     nat_list = entry['Nationality']
     for nat in nat_list:
        if nat not in res:
            res[nat] = []
        res[nat].append(entry)
        
for nationality in res:
    with open(f'res/{nationality}.json','w') as write_file:
        json.dump(res[nationality], write_file, indent=2)
