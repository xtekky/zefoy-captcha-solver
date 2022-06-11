<h1 align="center">
  Zefoy Captcha Solver 👻
</h1>

<p align="center">
  Zefoy OCR bruteforce captcha solver using cv2, PIL and pytesseract aswell as the Zefoy API
</p>

<p align="center"> 
  <kbd>
<img src="https://cdn.discordapp.com/attachments/956638416064376875/984798143755481118/3b459bc61bb8a51f74c0d3a80c3a7b1f1.jpg?size=4096"></img>
  </kbd>
</p>

<p align="center">
  <img src="https://img.shields.io/github/languages/top/xtekky/zefoy-captcha-solver?style=flat-square" </a>
  <img src="https://img.shields.io/github/last-commit/xtekky/zefoy-captcha-solver?style=flat-square" </a>
  <img src="https://img.shields.io/github/stars/xtekky/zefoy-captcha-solver?color=7F9DE0&label=Stars&style=flat-square" </a>
  <img src="https://img.shields.io/github/forks/xtekky/zefoy-captcha-solver?color=7F9DE0&label=Forks&style=flat-square" </a>
</p>

<h4 align="center">
  <a href="https://discord.gg/onlp">🌌・Discord</a>
  <a href="https://github.com/xtekky/zefoy-captcha-solver#changelog">📜・ChangeLog</a>
</h4>

<h2 align="center">
  Zefoy Captcha Solver was made by

Love ❌ code ✅

</h2>

---

## :fire: Features

✔ Solves the zefoy captcha under 20s

---

## 🚀・Setup Twitch Acc Gen

```sh-session
> Install python and pip
> Download this repo or git-clone it
> Install the requirements with: pip install -r requirements.txt
> run main.py, you may aswell then add your code when the captcha gets solved
```

## 🤝・Contributing

- The solver is not accurate at all, if you wish you can optimize it and make a pull request

## 🎉・Upcoming/enhancements

- Make it better faster


## 💭・ChangeLog

```diff
v0.0.2 ⋮ 2022-06-10
+ better response when solved

v0.0.1 ⋮ 2022-06-10
+ initial commit
```

## x・Filter Example
```python
import os, cv2, numpy, pytesseract, PIL, re, enchant
from tkinter import W
import scipy.ndimage as ndimage
import matplotlib.pyplot as plt

file = cv2.imread(f"./captcha.png")
thresh, im_bw = cv2.threshold(file, 200, 260, cv2.THRESH_BINARY)
_name = f'./enhanced.png'
b = cv2.imwrite(_name, im_bw)
def bbox(im):
    a = numpy.array(im)[:,:,:3]
    m = numpy.any(a != [255, 255, 255], axis=2)
    coords = numpy.argwhere(m)
    y0, x0, y1, x1 = *numpy.min(coords, axis=0), *numpy.max(coords, axis=0)
    return (x0, y0+1, x1-1, y1-1)

im = PIL.Image.open(_name)
im2 = im.crop(bbox(im))
im2.save(_name)


image = PIL.Image.open(_name)
inverted_image = PIL.ImageOps.invert(image)
inverted_image.save(_name)

im = PIL.Image.open(_name)
im2 = im.crop(bbox(im))
im2.save(_name)

basewidth = 700
img = PIL.Image.open(_name)
wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
img.save(_name)

cv2.imwrite(_name, cv2.threshold(cv2.dilate(cv2.threshold(cv2.imread(_name), 115, 255, cv2.THRESH_BINARY_INV)[1], cv2.getStructuringElement(cv2.MORPH_RECT, (3,3)), iterations=1), 115, 255, cv2.THRESH_BINARY_INV)[1])

ocr = pytesseract.image_to_string(_name, lang='eng', config='--psm 6 --oem 3')
captcha = str(ocr)

if captcha != "" and not None or not None:
                _captcha = re.compile('[^a-zA-Z]').sub('', captcha).lower()
                print(_captcha)
```

## x・Comparison
#### Before
![captcha](https://user-images.githubusercontent.com/98614666/173166442-dab67c1b-6b90-49e3-a3df-85d69797c68b.png)
#### After
![enhanced](https://user-images.githubusercontent.com/98614666/173166447-82fd2154-e98d-41dc-ac49-0b6b1105da8a.png)



<p align="center">
  README.md inspired from Rdimo
</p>
