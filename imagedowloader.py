import random
import urllib.request    #from urllib import request
def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jbg"
    urllib.request.urlretrieve(url, full_name)

download_web_image("https://image.cnbcfm.com/api/v1/image/106194367-1571709112694gettyimages-103017185.jpeg?v=1571710756&w=1600&h=900")
