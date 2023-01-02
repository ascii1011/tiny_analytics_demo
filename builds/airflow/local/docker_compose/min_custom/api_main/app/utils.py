

import os
from urllib.parse import urlparse
import urllib.request
import urllib

__all__ = ['download_image', 'generate_prompt']

IMAGE_DOWNLOAD_PATH = '/opt/image/download'


def convert_url_to_filename(url):
    a = urlparse(url)
    #print(a.path)                    # Output: /kyle/09-09-201315-47-571378756077.jpg
    #print(os.path.basename(a.path))  # Output: 09-09-201315-47-571378756077.jpg
    return os.path.basename(a.path)

def download_image(url, file_path=IMAGE_DOWNLOAD_PATH, prefix=""):
    filename = convert_url_to_filename(url)
    if prefix:
        filename = prefix + "__" + filename
    full_file_path = os.path.join(file_path, filename)
    print(f"{full_file_path=}")
    #full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_file_path)
    return filename

def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.

Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )



def encode_url(url):
    return url.replace("/", "$").replace(":", "#") + ".png"

def decode_filename(filename):
    return filename.replace('#',':').replace('$','_')
