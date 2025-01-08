import urllib.parse as up
import psycopg2
from ItemEntry import ItemEntry
import time
from selenium import webdriver
import pyimgur

CLIENT_ID = "935fd4bfe708bf3"

up.uses_netloc.append("mbhiokeh")
url = up.urlparse("postgresql://postgres:password@localhost:5432/smartkart") # Update with valid URI
conn = psycopg2.connect(database=url.path[1:],
user=url.username,
password=url.password,
host=url.hostname,
port=url.port
)

cursor = conn.cursor()

count_start = 0

PATH = "./geckodriver"
SITE = "https://www.nofrills.ca/"
driver = webdriver.Firefox()

def find_click_xpath(xpath, wait_long=0):
    driver.find_element_by_xpath(xpath).click()
    if wait_long:
        time.sleep(5)
    else:
        time.sleep(1)

def find_click_link_text(link_text, wait_long=0):
    driver.find_element_by_link_text(link_text).click()
    if wait_long:
        time.sleep(5)
    else:
        time.sleep(1)

def get_product_grid():
    html_list = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/main/div/div/div[5]/div/div[2]/div[3]/div/ul")
    #return html_list.find_elements_by_tag_name("li") seems to be broken
    return html_list.find_elements_by_class_name("product-tile-group__list__item")


# NoFrills specific elements
province = {"AB":"/html/body/div[1]/div/div[6]/div[2]/div/div/ul/li[1]/button",
            "MB":"/html/body/div[1]/div/div[6]/div[2]/div/div/ul/li[3]/button",
            "NL":"/html/body/div[1]/div/div[6]/div[2]/div/div/ul/li[5]/button",
            "ON":"/html/body/div[1]/div/div[6]/div[2]/div/div/ul/li[7]/button",
            "SK":"/html/body/div[1]/div/div[6]/div[2]/div/div/ul/li[9]/button",
            "BC":"/html/body/div[1]/div/div[6]/div[2]/div/div/ul/li[2]/button",
            "NB":"/html/body/div[1]/div/div[6]/div[2]/div/div/ul/li[3]/button",
            "NS":"/html/body/div[1]/div/div[6]/div[2]/div/div/ul/li[6]/button",
            "PEI":"/html/body/div[1]/div/div[6]/div[2]/div/div/ul/li[8]/button"
            }
departments_xpath = '/html/body/div[1]/div/div[1]/div[3]/div/header/div[2]/div[1]/nav/ul/li[1]'
food_xpath = '/html/body/div[1]/div/div[1]/div[3]/div/header/div[2]/div[1]/nav/ul/li[1]/ul/li[3]'
categories = {'dairy': 'Dairy & Eggs', 
              'meat': 'Meat',
              'fish': 'Fish & Seafood',
              'produce': 'Fruits & Vegetables',
              'deli':'Deli',
              'bakery':'Bakery',
              'drinks':'Drinks',
              'frozen':'Frozen',
              'pantry':'Pantry',
              'snacks':'Snacks, Chips & Candy'
              }

subcategories = {'dairy':['Ice Cream', 'Butter & Spreads', 'Desserts & Doughs', 
                          'Egg & Egg Substitutes', 'Lactose Free', 'Milk & Cream', 'Cheese', 
                          'Sour Cream & Dips', 'Yogurt']
                }

cookies_button_xpath = '/html/body/div[2]/div/div/button'

thumbnailClass = 'product-tile__thumbnail__image'
detailsClass = "product-name__item"
priceClass = "price__value"
store = "NoFrills"
cat = "Dairy"

# TODO: Iterate through location, category, subcategory
location = "ON"
category = categories['dairy']
subcategory = subcategories['dairy'][5]

# Start Firefox, wait for page to load (TODO: Smarter wait)
driver.get(SITE)
time.sleep(5)

# Navigate to desired page
find_click_xpath(province[location], 1)
find_click_xpath(departments_xpath)
find_click_xpath(food_xpath, 1)
find_click_link_text(category)
find_click_link_text(subcategory)
find_click_xpath(cookies_button_xpath)

# List of HTML <li> elements
items = get_product_grid()
item_entries = []

print(len(items))

total_height = int(driver.execute_script("return document.body.scrollHeight"))
for i in range(1, total_height, 5):
    driver.execute_script("window.scrollTo(0, {});".format(i))

filenames = []

for item in items:
    thumbnail = item.find_element_by_class_name(thumbnailClass)
    price = item.find_element_by_class_name(priceClass).text[1:]
    details = item.find_elements_by_class_name(detailsClass)
    brand = ""
    name = ""
    if(len(details) > 0):
        brand = details[0].text
        for entry in details[1:]:
            name += entry.text
            name += " "
   
    thumbnail_name = str(count_start) + cat
    with open(thumbnail_name, 'wb') as file:
        file.write(thumbnail.screenshot_as_png)
    filenames.append(thumbnail_name)
    
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(thumbnail_name, title=thumbnail_name)
    
    new_entry = ItemEntry(brand, name, price, store, cat, uploaded_image.link)
    item_entries.append(new_entry)
    
    count_start += 1
    time.sleep(3)
driver.quit()


for i in range(len(item_entries)):
    print(vars(item_entries[i]))
    cursor.execute("INSERT INTO items (item_id, brand, item_name, item_price, item_category, store, url) VALUES(%s, %s, %s, %s, %s, %s, %s)", 
    (i+100, item_entries[i].brand, item_entries[i].name, float(item_entries[i].price), item_entries[i].store, item_entries[i].category, item_entries[i].url))

conn.commit()

cursor.close()
conn.close()


