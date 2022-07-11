> OCR API:
- endpoint: https://api.xtekky.com/ocr
- method: POST
- json-data: `{"image":"base64 encoded image bytes"}`

> python example:

```py
import base64, requests

with open("captcha.png", "rb") as x:
    image_bytes = x.read()

r = requests.post(
    url = "https://api.xtekky.com/ocr",
    json = {
        "image": base64.b64encode(image_bytes).decode(),
    }
)

print(r.text)
```
