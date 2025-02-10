DO
$do$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = 'sixdigit') THEN

        CREATE USER sixdigit WITH PASSWORD '93k67y87s70t';
        CREATE TABLESPACE sixdigit OWNER sixdigit location '/var/lib/postgresql/data';
        CREATE DATABASE sixdigit OWNER sixdigit TABLESPACE sixdigit;

        ALTER ROLE sixdigit SET client_encoding TO 'utf8';
        ALTER ROLE sixdigit SET default_transaction_isolation TO 'read committed';
        ALTER ROLE sixdigit SET timezone TO 'UTC';
        GRANT ALL PRIVILEGES ON DATABASE sixdigit TO sixdigit;

   END IF;
END
$do$;




