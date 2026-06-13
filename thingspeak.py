import requests

API_KEY = "YOUR_API_KEY"

def upload_data(aqi,temp,humidity):

    url = (
        "https://api.thingspeak.com/update"
        f"?api_key={API_KEY}"
        f"&field1={aqi}"
        f"&field2={temp}"
        f"&field3={humidity}"
    )

    try:
        requests.get(url)
    except:
        pass