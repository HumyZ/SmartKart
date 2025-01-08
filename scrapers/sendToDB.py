import urllib.parse as up
import psycopg2

def send_to_database(item_id, brand, name, price, store, category, img_url):
    up.uses_netloc.append("mbhiokeh")
    url = up.urlparse("postgresql://postgres:password@localhost:5432/smartkart") # Update with valid URI
    conn = psycopg2.connect(database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
    )

    cursor = conn.cursor()
    cursor.execute("INSERT INTO items (item_id, brand, item_name, item_price, item_category, store, url) VALUES(%s, %s, %s, %s, %s, %s, %s)", 
    (item_id, brand, name, price, store, category, img_url))

    conn.commit()

    cursor.close()
    conn.close()
