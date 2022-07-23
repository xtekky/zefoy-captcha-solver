
```py
json_data =  {
    "requests": [{
        "image": {
            "content": "base64 encoded image"
        },
        "features": [{"type": "TEXT_DETECTION"}]
    }]
}

req = requests.post(
    url = 'https://content-vision.googleapis.com/v1/images:annotate',
    headers = {
        'x-origin': 'https://explorer.apis.google.com',
    },
    params = {
        'alt': 'json',
        'key': 'AIzaSyAa8yy0GdcGPHdtD083HiGGx_S0vMPScDM',
    },
    json = json_data
)

print(req.json())
```
