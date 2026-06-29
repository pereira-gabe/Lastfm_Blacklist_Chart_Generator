import io
import os
import requests
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("LASTFM_API_KEY") # TODO: implement support for spotify profiles
USER = "shoegazygabe" #input("lastfm username: ")

GRID_SIZE = 5
IMG_SIZE = 300

url = "https://ws.audioscrobbler.com/2.0/"

blacklist = [
    "virgingod",
    "Link do Zap",
    "Big Rush",
    "Bladee",
    "Kamaitachi"
]

params = {
    "method": "user.gettopalbums",
    "user": USER,
    "api_key": API_KEY,
    "format": "json",
    "period": "12month",
    "limit": 50
}

response = requests.get(url, params=params)

data = response.json()
covers = []

for album in data["topalbums"]["album"]:
    if album["artist"]["name"] not in blacklist and len(covers) < 25:
        image_url = album["image"][-1]["#text"]

        if image_url:
            try:
                img_data = requests.get(image_url).content
                img = Image.open(io.BytesIO(img_data)).convert("RGB")
                img = img.resize((300, 300))
                covers.append(img)
            except Exception:
                pass

    elif len(covers) < 25:
        print(f"Ignored: {album["artist"]["name"]}: {album["name"]}, {album["playcount"]} scrobbles")

while len(covers) < 25:
        covers.append(Image.new("RGB", (300, 300), "black"))

grid = Image.new("RGB", (GRID_SIZE * IMG_SIZE, GRID_SIZE * IMG_SIZE))

for i, cover in enumerate(covers[:25]):
    x = (i % GRID_SIZE) * IMG_SIZE
    y = (i // GRID_SIZE) * IMG_SIZE
    grid.paste(cover, (x, y))

if os.path.exists("chart.png"):
    os.remove("chart.png")

grid.save("chart.png")
grid.show()
