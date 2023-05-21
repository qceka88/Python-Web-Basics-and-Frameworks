"""

   PostgreSQL





Code below is for PostgreSQL


--INSERT INTO people VALUES (example@example.com, Georgi, Petrov), ('somethin@example.com','Petur','Kirilov');

-- insert into people(email, first_name, last_name) values ('example@something', 'Georgi', 'Petrov'), ('something@example', 'Petur', 'Georgiev')

SELECT * FROM public.people WHERE first_name= 'Ivan' or first_name = 'Georgi';

-- UPDATE people SET last_name = 'Georgiev' where first_name = 'Georgi' and last_name = 'Petrov';

-- ALTER TABLE people
-- ADD COLUMN salary DECIMAL;


"""

# docker run -p 5432:5432 -e POSTGRES_USER=Yanko -e POSTGRES_PASSWORD=1234 -d -v my-postgres-data:/var/lib/postgresql/data --name custom-name postgres:latest
#docker run -p 5050:80 -e PGADMIN_DEFAULT_EMAIL=some@email.com -e PGADMIN_DEFAULT_PASSWORD=password -v my-data:/var/lib/pgadmin -d dpage/pgadmin4
#
# -- CREATE TABLE employee (
# --     id SERIAL UNIQUE NOT NULL,
# --     first_name CHARACTER VARYING (100) NOT NULL,
# --     last_name CHARACTER VARYING (100) NOT NULL,
# --     town CHARACTER VARYING (100) NOT NULL,
# --     salary BIGINT NOT NULL
# -- );
# --
# --
# -- ALTER TABLE employee
# --     ADD COLUMN salary DECIMAL;
# --
# -- ALTER TABLE employee
# -- RENAME COLUMN town TO job_tittle;

# CREATE TABLE The_Sea_Dragons(
#     member_id                SERIAL,
#     member_first_name        CHARACTER VARYING(100) NOT NULL,
#     member_last_name         CHARACTER VARYING(100) NOT NULL,
#     member_motorcycle        CHARACTER VARYING(100) NOT NULL,
#     member_motorcycle_volume BIGINT                 NOT NULL);
#
# ALTER TABLE the_sea_dragons
#     ALTER COLUMN member_motorcycle DROP NOT NULL,
#     ALTER COLUMN member_motorcycle_volume DROP NOT NULL;
#
# INSERT INTO the_sea_dragons VALUES (1 ,'Ivo', 'Minaylov', 'Yamaha-R1', 1000);
#
# INSERT INTO the_sea_dragons VALUES (2,'Pepo', 'Grakov', 'Kwasaki-ZX10R', 1000),
#        (3, 'Veselin', 'Hristov', NULL, NULL),
#        (4, 'Ico', 'Hristov', NULL, NULL),
#        (5, 'Martin', 'Hristov', 'Suzuki-GSX-R1000', 1000),
#        (6, 'Vilyana', 'Staneva', 'Honda-CB1000R', 1000),
#        (7, 'Yuri', 'Ivanov', NULL, NULL),
#        (8, 'Dimitar', 'Dimitrov', NULL, NULL);
#
# INSERT INTO the_sea_dragons VALUES (9, 'Yanko', 'Rashkov');
#
# SELECT * FROM public.the_sea_dragons
# ORDER BY member_id ASC;