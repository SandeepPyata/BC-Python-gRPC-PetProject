DROP DATABASE IF EXISTS mydatabase;

CREATE DATABASE mydatabase;
USE mydatabase;
 
-- Table: User
CREATE TABLE User (
   id int NOT NULL AUTO_INCREMENT,
   typeOfUser varchar(10) NOT NULL,
   name varchar(100) NOT NULL,
   address varchar(100) NOT NULL,
   phone_no bigint NOT NULL,
   email_id varchar(100) NOT NULL,
   CONSTRAINT User_pk PRIMARY KEY (id)
);

-- Table: Login
CREATE TABLE Login (
   id int NOT NULL AUTO_INCREMENT,
   otp int NOT NULL,
   time_limit int NOT NULL,
   User_id int NOT NULL,
   CONSTRAINT Login_pk PRIMARY KEY (id)
);

-- Table: Admin
CREATE TABLE Admin (
   id int NOT NULL AUTO_INCREMENT,
   User_id int NOT NULL,
   CONSTRAINT Admin_pk PRIMARY KEY (id)
);

-- Table: Customer
CREATE TABLE Customer (
   id int NOT NULL AUTO_INCREMENT,
   User_id int NOT NULL,
   rating int NOT NULL DEFAULT 0,
   CONSTRAINT Customer_pk PRIMARY KEY (id)
);

-- Table: Driver
CREATE TABLE Driver (
    id int  NOT NULL AUTO_INCREMENT,
    User_id int  NOT NULL,
    current_location_lat decimal(7,5)  NULL,
    current_location_long decimal(7,5)  NULL,
    is_verified_status text  NOT NULL,
    rating int NOT NULL DEFAULT 0,
    current_status int  NOT NULL,
    CONSTRAINT Driver_pk PRIMARY KEY (id)
);

-- Table: Bookings
CREATE TABLE Bookings (
   booking_id int  NOT NULL AUTO_INCREMENT,
   booked_time timestamp  NOT NULL,
   final_fare int  NOT NULL,
   booking_status int  NOT NULL,
   payment_status int  NOT NULL,
   Driver_id int  NOT NULL,
   Customer_id int  NOT NULL,
   pickup_location_text text  NOT NULL,
   drop_location_text text  NOT NULL,
   pickup_lat decimal(7,5)  NOT NULL,
   pickup_long decimal(7,5)  NOT NULL,
   drop_lat decimal(7,5)  NOT NULL,
   drop_long decimal(7,5)  NOT NULL,
   CONSTRAINT Bookings_pk PRIMARY KEY (booking_id)
);

-- Table: Driver_Docs
CREATE TABLE Driver_Docs (
   id int NOT NULL AUTO_INCREMENT,
   bike_registration_number varchar(10) NOT NULL,
   license_docs_link text NOT NULL,
   Admin_id int NOT NULL,
   Driver_id int NOT NULL,
   docs_link text NULL,
   CONSTRAINT Driver_Docs_pk PRIMARY KEY (id)
);

-- delimiter $$

-- CREATE TRIGGER insert_into_customer_admin
-- AFTER INSERT ON User FOR EACH ROW
-- BEGIN
--     DECLARE typeOfUser varchar(100);
--     declare id integer;
--     -- @id=id
-- 	SET @typeOfUser := (SELECT typeOfUser from User order by id limit 1);
--     SET @id:= (SELECT id from User order by id limit 1);
--     
--     IF (@typeOfUser = 'Customer') THEN
-- 		INSERT INTO Customer(User_id) values(@id);
-- 	ELSEIF (@typeOfUser = 'Admin') THEN
-- 		INSERT INTO Admin(User_id) values(@id);
-- 	END IF;
-- END$$

-- delimiter ;

