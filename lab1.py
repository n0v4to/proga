import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import requests

def get_image(image_link, name, index):
    if not os.path.isdir(name):
        os.mkdir(name)
    picture = requests.get(image_link)
    saver = open(os.path.join(f"{name}/{str(index).zfill(4)}.jpg"), "wb")
    saver.write(picture.content)
    saver.close()


if __name__ == "__main__":
    main()