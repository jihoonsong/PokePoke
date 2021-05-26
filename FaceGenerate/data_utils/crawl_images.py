from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request


mans = ['']

count = 0

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.google.co.kr/imghp?hl=ko&tab=wi&ogbl')

for man in mans:

    try:
        elem = driver.find_element_by_name("q")  # Get Search Bar
        elem.send_keys('{} 얼굴 사진'.format(man))  # Type search words
        elem.send_keys(Keys.RETURN)  # Press Enter

        time.sleep(3)

        try:
            images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
        except:
            print('{} Passed'.format(man))
            continue

        if len(images) == 0:
            print('{} No Images'.format(man))
            continue

        time.sleep(1)

        for image in images:

            inner_count = 0

            try:
                image.click()
                time.sleep(3)

                imgUrl = driver.find_element_by_xpath(
                    "/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img").get_attribute(
                    'src')

                if imgUrl[:4] != 'http':
                    continue
                else:
                    urllib.request.urlretrieve(imgUrl,
                                               'C:/Users/grand/Desktop/ML/CycleGAN/data/man/image_{}.jpg'.format(
                                                   str(count)))
                    inner_count += 1
                    count += 1

                if inner_count == 25:
                    break
            except:
                continue

        elem = driver.find_element_by_name("q")
        elem.clear()

    except:
        print('{} Passed'.format(man))
        continue