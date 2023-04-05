import requests
import json

url = "https://collectionapi.metmuseum.org/public/collection/v1/search"
# headers = {'Content-Type':'application/json'}
res=requests.get(url, params= {"q":"van gogh", "isOnView":"true","hasImages" :"true"})
    # "artistOrCulture": True


res_json = res.json()
formatted_res = json.dumps(res_json, indent=2)
print(formatted_res)
