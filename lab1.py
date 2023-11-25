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

def get_url_images(path, request) -> None :

    os.chdir(path)
    if not os.path.isdir("dataset"):
        os.mkdir("dataset")
    os.chdir("dataset")

    count = 0   
    page = 0
    while(count < 1000):
    
        request1 = request.replace(" ", "%20")
        url = f"https://yandex.ru/images/search?p={page}&text={request1}"
    
        driver = webdriver.Chrome()
        driver.get(url = url)
        time.sleep(5)

        try:
            _ = driver.find_elements( By.CLASS_NAME, 'CheckboxCaptcha')
            input('Enter после капчи')
            driver.get(url = url)
            time.sleep(5)
        except Exception as e:
            print('Капчи нет')

        images = driver.find_elements( By.CLASS_NAME, 'SimpleImage-Image')
        print( images )

        for i in images:

        
            image_link = i.get_attribute('src') 
            get_image(image_link, request, count)
            count += 1
            print(image_link)
        page += 1
    driver.close()
    driver.quit()


def main():
    directory = os.getcwd()
    request = 'brown bear'
    get_url_images(directory, request)


if __name__ == "__main__":
    main()