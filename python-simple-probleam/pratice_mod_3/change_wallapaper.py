# import requests
# import json
import PyWallpaper

api_url = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'
response = requests.get(api_url)
content = response.content.decode('UTF-8')

# convert string to json
dict_conent = json.loads(content)
image_url = dict_conent["url"]

image_res = requests.get(image_url)

with open("apod.png", 'wb') as image:
    image.write(image_res.content)

PyWallpaper.change_wallpaper('/apod.png')
print("working")
