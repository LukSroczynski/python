import random
import urllib.request


def download_web_image(url):
    name = random.randrange(1,1000)
    full_name = str(name) + ".jpeg"
    urllib.request.urlretrieve(url, full_name)

download_web_image("https://yt3.ggpht.com/"
                   "--n5ELY2uT-U/AAAAAAAAAAI/AAAAAAAAAAA/d9JvaIEpstw/s88-c-k-no-mo-rj-c0xffffff/photo.jpg")