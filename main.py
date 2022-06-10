import pytesseract, cv2, requests, os, random, threading, re, sys, time, enchant, shutil, numpy
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files (x86)/Tesseract-OCR/tesseract.exe"
sys.setrecursionlimit(1500)

class Solver:
    def __init__(self):
        self.config   = '--psm 6 --oem 3'
        self.base_url = "https://zefoy.com/"
        
        self.start    = time.time()
        self.reqs     = 0
        
        threading.Thread(target=self.monitor).start()

        while True:
            self.solve()
            
            if threading.active_count() < 2 + 1:
                threading.Thread(target=self.solve).start()
    
    def monitor(self):
        while True:
            os.system(f'title Captcha Solver ^| Requests ~ {self.reqs} ^| Time Elapsed ~ {round(time.time() - self.start, 1)}s')
            time.sleep(0.5)
            
            
    def solve(self):
        try:
            sess = requests.Session()
            num = random.randint(1000, 9999)

            sessid = sess.get(
                self.base_url,
                headers={
                    "origin": "https://zefoy.com",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
                    "x-requested-with": "XMLHttpRequest"
                }
            ).cookies.values()[0]

            response = sess.get(
                self.base_url + "a1ef290e2636bf553f39817628b6ca49.php",
                headers={
                    "origin": "https://zefoy.com",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
                    "x-requested-with": "XMLHttpRequest",
                    "cookie": f"PHPSESSID={sessid}",
                },
                params={
                    "_CAPTCHA": "",
                    "t": "0.23092200 1654778649"
                }
            )

            with open(f"./captchas/captcha{num}.png", 'wb') as _:
                _.write(response.content)
            
            file = cv2.imread(f"./captchas/captcha{num}.png")
            os.remove(f"./captchas/captcha{num}.png")
            thresh, im_bw = cv2.threshold(file, 190, 260, cv2.THRESH_BINARY)
            _name = f'./captchas/enhanced{num}.png'
            b = cv2.imwrite(_name, im_bw)
            def bbox(im):
                a = numpy.array(im)[:,:,:3]
                m = numpy.any(a != [255, 255, 255], axis=2)
                coords = numpy.argwhere(m)
                y0, x0, y1, x1 = *numpy.min(coords, axis=0), *numpy.max(coords, axis=0)
                return (x0, y0, x1+1, y1+1)

            im = Image.open(_name)
            im2 = im.crop(bbox(im))
            im2.save(_name)
            
            ocr = pytesseract.image_to_string(_name, config=self.config)
            captcha = str(ocr)
            
            if captcha != "" and not None or not None:
                _captcha = re.compile('[^a-zA-Z]').sub('', captcha).lower()
                
                d = enchant.Dict("en_US")
                if d.check(_captcha) == False:
                    _captcha = d.suggest(_captcha)[0]
                
                if len(_captcha) > 2:

                    print(_captcha)

                    shutil.copy(f"./captchas/enhanced{num}.png", f"./solved/{_captcha}.png")

                    _response = sess.post(
                            "https://zefoy.com",
                            data={
                                "captcha_secure": _captcha,
                                "r75619cf53f5a5d7aa6af82edfec3bf0": ""
                            },
                            headers={
                                "cookie": f"PHPSESSID={sessid}",
                                "origin": "https://zefoy.com",
                                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
                                "x-requested-with": "XMLHttpRequest"
                            }
                        )

                    if "c2VuZF9mb2xsb3dlcnNfdGlrdG9r" in _response.text:
                        print("SOLVED", time.time() - self.start)
                        sys.exit('solved successfully')
                    else:
                        pass
                    
                    self.reqs += 1

            os.remove(f'./captchas/enhanced{num}.png')
            
        except Exception as e:
            try: 
                os.remove(f'./captchas/enhanced{num}.png')
                os.remove(f"./captchas/captcha{num}.png")
            except: 
                pass


if __name__ == "__main__":
    os.system("cls" if os.name == 'nt' else 'clear')
    Solver()
