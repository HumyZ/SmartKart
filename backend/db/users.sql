CREATE TABLE IF NOT EXISTS public.users
(
    id integer NOT NULL DEFAULT nextval('users_id_seq'::regclass),
    is_active boolean NOT NULL DEFAULT true,
    email character varying(1000) COLLATE pg_catalog."default" NOT NULL,
    password bytea NOT NULL,
    last_login timestamp without time zone,
    CONSTRAINT users_pkey PRIMARY KEY (id),
    CONSTRAINT users_email_key UNIQUE (email)
)