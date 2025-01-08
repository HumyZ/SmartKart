CREATE TABLE IF NOT EXISTS public.accounts
(
    userid integer NOT NULL,
    email character varying(1000) COLLATE pg_catalog."default" NOT NULL,
    password bytea NOT NULL,
    last_login timestamp with time zone,
    CONSTRAINT accounts_pkey PRIMARY KEY (userid),
    CONSTRAINT accounts_email_key UNIQUE (email)
)