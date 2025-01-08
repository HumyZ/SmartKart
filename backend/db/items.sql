CREATE TABLE IF NOT EXISTS public.items
(
    item_id integer NOT NULL,
    brand character varying(1000) COLLATE pg_catalog."default" NOT NULL,
    item_name character varying(1000) COLLATE pg_catalog."default" NOT NULL,
    item_price real NOT NULL,
    item_category character varying(1000) COLLATE pg_catalog."default" NOT NULL,
    store character varying(1000) COLLATE pg_catalog."default" NOT NULL,
    url character varying(1000) COLLATE pg_catalog."default",
    CONSTRAINT items_pkey PRIMARY KEY (item_id)
)

-- ### Sample data inserted into table. (Dummy data for now, until scrapper is implemented) ###
-- The primary key is the item_id (1st element, [0th index] in the tuple)

-- INSERT INTO items (item_id, item_name, item_price, item_category, store)
-- VALUES
-- (0, 'Milk', 0.99, 'Dairy', 'Walmart'),
-- (1, 'Apples', 0.13, 'Fruits and Vegetables', 'Walmart'),
-- (2, 'Bread', 0.60, 'Grains', 'Walmart'),
-- (3, 'Cake', 3.56, 'Desserts', 'No Frills'),
-- (4, 'Chicken', 5.60, 'Meat', 'Walmart'),
-- (5, 'Chicken', 5.40, 'Meat', 'FreshCo'),
-- (6, 'Water', 1.90, 'Beverages', 'Walmart'),
-- (7, 'Detergent', 6.99, 'Household/Cleaning', 'FreshCo');
