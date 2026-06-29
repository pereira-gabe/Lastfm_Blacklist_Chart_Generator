# Last.fm Album Chart Generator with Blacklist

Generate a **5×5 collage** of your most-played Last.fm albums from the last month using Pillow.

## Features

- Fetches your top 25 albums using the Last.fm API
- Automatically skips artists defined in your custom `blacklist`
- Saves the output as `chart.png`

## Requirements

- Python 3.10+
- Last.fm account and API key

Install the dependencies:

```bash
pip install requests pillow python-dotenv
````

Create a `.env` file:

```env
LASTFM_API_KEY=your_api_key_here
```

Edit the `USER` variable in the script and run:

```bash
python3 main.py
```
The generated collage will be saved as `chart.png`.
