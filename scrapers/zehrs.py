from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import pyimgur
import sendToDB

PATH = "./geckodriver"
SITE = "https://www.zehrs.ca/"
CLIENT_ID = "935fd4bfe708bf3"
LIMIT = 50

driver = webdriver.Firefox(executable_path=PATH)
driver.maximize_window()
driver.get(SITE)


def handle(path, time=25):
    WebDriverWait(driver, time).until(
        EC.element_to_be_clickable((
            By.XPATH, path))).click()


def get_categories(grid):
    element_list = WebDriverWait(driver, 25).until(
        EC.element_to_be_clickable((By.XPATH, grid)))

    return element_list.find_elements(By.TAG_NAME, "li")


def parse(items, cat):
    id_no = 200
    img_file = "img_file"
    products = []

    for i in range(0, LIMIT, 2):
        img = items[i].find_element(By.CLASS_NAME,
                                    "product-tile__thumbnail__image")
        info = items[i].find_elements(By.CLASS_NAME, "product-name__item")
        price = items[i].find_element(By.CLASS_NAME, "price__value")

        with open(img_file, 'wb') as file:
            file.write(img.screenshot_as_png)

        im = pyimgur.Imgur(CLIENT_ID)
        uploaded_image = im.upload_image(img_file, title=None)

        if info:
            brand, name = info[0], info[1]
            sendToDB.send_to_database(id_no, brand.text, name.text,
                                      float(price.text[1:]), "Zehrs", cat,
                                      uploaded_image.link)
            id_no += 1
    return products


departments_xpath = "/html/body/div[1]/div/div[1]/div[3]/div/header/div[2]/" \
                    "div[1]/nav/ul/li[1]/button"

food_xpath = "/html/body/div[1]/div/div[1]/div[3]/div/header/div[2]/div[1]/" \
             "nav/ul/li[1]/ul/li[3]/a"

category_grid = "/html/body/div[1]/div/div[1]/div[3]/div/header/div[2]/" \
                "div[1]/nav/ul/li[1]/ul"

# Departments -> Food
handle(departments_xpath)
handle(food_xpath)

""" 
This is a sample of how this scrapper fetch all the products under
the category Dairy & Eggs and all of its subcategories Ice Cream, Butter etc. 
"""


# { Cat: ( XPATH, { Sub-Cat: [XPATH, UL] } ) }
item_categories = {"Dairy & Eggs": ("/html/body/div[1]/div/div[2]/main/div/div"
                                    "/div[4]/div/ul/li[7]/a",

                                    {"Ice Cream": ["/html/body/div[1]/div/"
                                                   "div[2]/main/div/div/"
                                                   "div[4]/div/ul/li[1]/a",

                                                   "/html/body/div[1]/div/"
                                                   "div[2]/main/div/div/"
                                                   "div[5]/div/div[2]/"
                                                   "div[3]/div/ul"]})
                   }

# Display Results
for k, v in item_categories.items():
    handle(v[0])    # Cat

    for kk, vv in v[1].items():     # Sub-Cat Dict
        handle(vv[0])
        package = parse(get_categories(vv[1]), kk)   # Ul

print("Success")
driver.quit()
