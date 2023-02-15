import json
res = []
with open('food.json')as file:

    json_file = json.load(file)
    for food in json_file:
        if food['Type']=='Fruit':
            res.append(food)
            print (food)
            





