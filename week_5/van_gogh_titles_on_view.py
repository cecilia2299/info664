import requests
import json

url = "https://collectionapi.metmuseum.org/public/collection/v1/search"
# headers = {'Content-Type':'application/json'}
res=requests.get(url, params= {"q":"van gogh", "isOnView":"true","hasImages" :"true"})
res_json = res.json()
# formatted_res = json.dump(res_json, indent=2)

# print(formatted_res)
# print(res_json["objectIDs"])
# params= {"q":"van gogh", "isOnView":"true","hasImages" :"true"})
    # "artistOrCulture": True
object_list =[]
for object in res_json["objectIDs"]:

    objectsUrl = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{object}"
    # print(objectsUrl)
    resObject =requests.get(objectsUrl)
    resObject_json = resObject.json()
    object_list.append (resObject_json["title"])
print(object_list)
    
    # formatted_object_res = json.dumps(resObject_json, indent=2)
 
    # resobject=requests.post(objectsUrl, data =json.dumps(data))
    # res_json = res.json()
    # formatted_res = json.dumps(res_json, indent=2)
