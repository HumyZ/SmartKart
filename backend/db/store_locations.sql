CREATE TABLE IF NOT EXISTS public.store_locations
(
    name character varying COLLATE pg_catalog."default" NOT NULL,
    lat real,
    "long" real
)