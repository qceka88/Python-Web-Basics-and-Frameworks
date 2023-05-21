--some commands for PostgresSQL
CREATE TABLE the_sea_dragons
(
    member_id                SERIAL PRIMARY KEY,
    member_first_name        VARCHAR(30)           NOT NULL,
    member_last_name         CHARACTER VARYING(30) NOT NULL,
    member_motorcycle        CHARACTER VARYING(30) NOT NULL,
    member_motorcycle_volume BIGINT
);


INSERT INTO the_sea_dragons (member_first_name, member_last_name, member_motorcycle, member_motorcycle_volume)
VALUES ('Ivo', 'Mihaylov', 'YAMAHA-R1', 1000);


ALTER TABLE the_sea_dragons
    ADD COLUMN member_town CHARACTER VARYING(30);


INSERT INTO the_sea_dragons (member_first_name, member_last_name, member_motorcycle, member_motorcycle_volume,
                             member_town)
VALUES ('Pepo', 'Grakov', 'Kawasaki-ZX10R', 1000, 'Veliko Tarnovo');

UPDATE the_sea_dragons
SET member_town = 'Varna'
WHERE member_id = 1;

ALTER TABLE the_sea_dragons
    ALTER COLUMN member_motorcycle DROP NOT NULL;


INSERT INTO the_sea_dragons (member_first_name, member_last_name, member_motorcycle, member_motorcycle_volume,
                             member_town)
VALUES ('Veselin', 'Hristov', NULL, NULL, 'Varna'),
       ('Ico', 'Hristov', NULL, NULL, 'Beloslav'),
       ('Martin', 'Rusev', 'Suzuki-GSXR100', 1000, 'Shkorpilovci'),
       ('Viliyana', 'Staneva', 'Honda-CB100R', 1000, 'Varna'),
       ('Yuri', 'Ivanov', NULL, NULL, 'Varna'),
       ('Dimitar', 'Dimitrov', NULL, NULL, 'Varna')
;

INSERT INTO the_sea_dragons
VALUES (9, 'Yanko', 'Rashkov', NULL, NULL, 'Yambol');


SELECT *
FROM the_sea_dragons
ORDER BY member_id ASC;

