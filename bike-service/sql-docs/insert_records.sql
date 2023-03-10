-- use mydatabase;

-- -- User Data Insertion
-- insert into User (id, typeOfUser, name, address, phone_no, email_id) values (1, 'Admin', 'Admin1', '564 Loomis Drive', '4571734216','jalcott0@google.pl');
-- insert into User (id, typeOfUser, name, address, phone_no, email_id) values (2, 'Customer', 'Customer1', '47482 Division Park', '3789338518','mgandy1@disqus.com');
-- insert into User (id, typeOfUser, name, address, phone_no, email_id) values (3, 'Driver', 'Driver1','7 Carpenter Place', '4547285164','abrugsma2@yellowpages.com');
-- insert into User (id, typeOfUser, name, address, phone_no, email_id) values (4, 'Driver', 'Driver2','77235 Prentice Parkway','5172524091','pexelby3@cbsnews.com');
-- insert into User (id, typeOfUser, name, address, phone_no, email_id) values (5, 'Customer','Customer1', '2293 Larry Plaza',  '8234259217','speddowe4@uiuc.edu');
-- insert into User (id, typeOfUser, name, address, phone_no, email_id) values (6, 'Admin', 'Admin2','0054 Tony Terrace','2919987876','kalflat5@skype.com');


-- -- Login
-- insert into Login (id, otp, time_limit, User_id) values (1, 4324, 180, 1);
-- insert into Login (id, otp, time_limit, User_id) values (2, 4577, 180, 2);
-- insert into Login (id, otp, time_limit, User_id) values (3, 5646, 180, 3);
-- insert into Login (id, otp, time_limit, User_id) values (4, 3408, 180, 4);
-- insert into Login (id, otp, time_limit, User_id) values (5, 7002, 180, 5);
-- insert into Login (id, otp, time_limit, User_id) values (6, 1115, 180, 6);


-- -- Customer
-- insert into Customer (id, userID, rating) values (1, 1, 4.3);
-- insert into Customer (id, userID, rating) values (2, 2, 3.4);
-- insert into Customer (id, userID, rating) values (3, 3, 1.9);
-- insert into Customer (id, userID, rating) values (4, 4, 4.3);
-- insert into Customer (id, userID, rating) values (5, 5, 2.7);
-- insert into Customer (id, userID, rating) values (6, 6, 1.9);


-- -- Admin
-- insert into Admin (id, userID) values (1, 1);
-- insert into Admin (id, userID) values (2, 2);
-- insert into Admin (id, userID) values (3, 3);
-- insert into Admin (id, userID) values (4, 4);
-- insert into Admin (id, userID) values (5, 5);
-- insert into Admin (id, userID) values (6, 6);


-- -- Driver
-- insert into Driver (id, userID, current_location_lat, current_location_long, is_verified_status, rating, current_status) values (1, 1, 32.06653, 16.49964, 'verified', 1, 'unavailable');
-- insert into Driver (id, userID, current_location_lat, current_location_long, is_verified_status, rating, current_status) values (2, 2, 15.08618, 90.68729, 'verified', 4, 'available');
-- insert into Driver (id, userID, current_location_lat, current_location_long, is_verified_status, rating, current_status) values (3, 3, 38.25148, 20.71688, 'verified', 2, 'available');
-- insert into Driver (id, userID, current_location_lat, current_location_long, is_verified_status, rating, current_status) values (4, 4, 43.73787, 21.23004, 'verified', 1, 'unavailable');
-- insert into Driver (id, userID, current_location_lat, current_location_long, is_verified_status, rating, current_status) values (5, 5, 16.50333, 95.99816, 'verified', 2, 'available');
-- insert into Driver (id, userID, current_location_lat, current_location_long, is_verified_status, rating, current_status) values (6, 6, 27.96014, 69.32364, 'verified', 2, 'in-trip');

-- -- Bookings
-- insert into Bookings (booking_id, booked_time, final_fare, booking_status, payment_status, Driver_driver_id, Customer_customer_id, pickup_location_text, drop_location_text, pickup_lat, pickup_long, drop_lat, drop_long) values (1, '2022-10-17 08:41:27', 374, 'booked', 'unPaid', 1, 1, '12600 Mendota Road', '90 Monument Place', 45.50803, -73.5645, 8.45381, 39.28091);
-- insert into Bookings (booking_id, booked_time, final_fare, booking_status, payment_status, Driver_driver_id, Customer_customer_id, pickup_location_text, drop_location_text, pickup_lat, pickup_long, drop_lat, drop_long) values (2, '2022-06-06 15:42:00', 334, 'searching', 'notApplicable', 2, 2, '49138 4th Way', '7 Farwell Junction', 47.20865, 27.0686, -7.29068, 10.66396);
-- insert into Bookings (booking_id, booked_time, final_fare, booking_status, payment_status, Driver_driver_id, Customer_customer_id, pickup_location_text, drop_location_text, pickup_lat, pickup_long, drop_lat, drop_long) values (3, '2022-06-17 13:33:21', 336, 'canceled', 'notApplicable', 3, 3, '8 Norway Maple Circle', '733 Ruskin Way', 49.61065, 18.7359, 51.17109, 15.1227);
-- insert into Bookings (booking_id, booked_time, final_fare, booking_status, payment_status, Driver_driver_id, Customer_customer_id, pickup_location_text, drop_location_text, pickup_lat, pickup_long, drop_lat, drop_long) values (4, '2022-10-05 01:24:47', 439, 'inProgress', 'unpaid', 4, 4, '7669 Helena Junction', '70 Heath Junction', 8.08286, -80.80822, 15.24989, 20.8562);
-- insert into Bookings (booking_id, booked_time, final_fare, booking_status, payment_status, Driver_driver_id, Customer_customer_id, pickup_location_text, drop_location_text, pickup_lat, pickup_long, drop_lat, drop_long) values (5, '2022-03-06 19:07:37', 302, 'completed', 'paid', 5, 5, '35732 Dovetail Drive', '7 Barnett Pass', 49.43823, 1.05989, 31.10759, 11.04645);
-- insert into Bookings (booking_id, booked_time, final_fare, booking_status, payment_status, Driver_driver_id, Customer_customer_id, pickup_location_text, drop_location_text, pickup_lat, pickup_long, drop_lat, drop_long) values (6, '2022-07-26 01:11:57', 407, 'completed', 'paid', 6, 6, '2 Schmedeman Alley', '57279 Oriole Circle', 28.88376, 64.38597, 22.2790, 14.4463);

-- -- Driver_Docs
-- insert into Driver_Docs (id, bike_registration_number, license_docs_link, Admin_id, Driver_id, docs_link) values (1, 'HR26DQ553', 'http://www.lequydonhanoi.edu.vn/upload_images/S%C3%A1ch%20ngo%E1%BA%A1i%20ng%E1%BB%AF/Rich%20Dad%20Poor%20Dad.pdf',1, 1, 'https://drive.google.com/file/d/0B1HXnM1lBuoqMzVhZjcwNTAtZWI5OS00ZDg3LWEyMzktNzZmYWY2Y2NhNWQx/view?hl=en&resourcekey=0-5DqnTtXPFvySMiWstuAYdA');
-- insert into Driver_Docs (id, bike_registration_number, license_docs_link, Admin_id, Driver_id, docs_link) values (2, 'HR26DQ554', 'http://fop86.com/Rich%20Dad%20Poor%20Dad/Rich%20Dad%20Poor%20Dad.pdf',2, 2, 'https://drive.google.com/file/d/0B1HXnM1lBuoqMzVhZjcwNTAtZWI5OS00ZDg3LWEyMzktNzZmYWY2Y2NhNWQx/view?hl=en&resourcekey=0-5DqnTtXPFvySMiWstuAYdA');
-- insert into Driver_Docs (id, bike_registration_number, license_docs_link, Admin_id, Driver_id, docs_link) values (3, 'HR26DQ555', 'https://archive.org/download/richdadpoordadhindi/Rich%20dad%20poor%20dad%20Hindi.pdf',3, 3, 'https://drive.google.com/file/d/0B1HXnM1lBuoqMzVhZjcwNTAtZWI5OS00ZDg3LWEyMzktNzZmYWY2Y2NhNWQx/view?hl=en&resourcekey=0-5DqnTtXPFvySMiWstuAYdA');
-- insert into Driver_Docs (id, bike_registration_number, license_docs_link, Admin_id, Driver_id, docs_link) values (4, 'HR26DQ556', 'http://fop86.com/Rich%20Dad%20Poor%20Dad/Rich%20Dad%20Poor%20Dad.pdf',4, 4, 'https://drive.google.com/file/d/0B1HXnM1lBuoqMzVhZjcwNTAtZWI5OS00ZDg3LWEyMzktNzZmYWY2Y2NhNWQx/view?hl=en&resourcekey=0-5DqnTtXPFvySMiWstuAYdA');
-- insert into Driver_Docs (id, bike_registration_number, license_docs_link, Admin_id, Driver_id, docs_link) values (5, 'HR26DQ557', 'https://camaapearl.files.wordpress.com/2016/02/cashflow1.pdf',5, 5, 'https://drive.google.com/file/d/0B1HXnM1lBuoqMzVhZjcwNTAtZWI5OS00ZDg3LWEyMzktNzZmYWY2Y2NhNWQx/view?hl=en&resourcekey=0-5DqnTtXPFvySMiWstuAYdA');
-- insert into Driver_Docs (id, bike_registration_number, license_docs_link, Admin_id, Driver_id, docs_link) values (6, 'HR26DQ558', 'http://117.240.231.117:8081/jspui/bitstream/123456789/537/1/Rich%20Dad%27s%20Cashflow%20quadrant%20Guide%20to%20Financial%20Freedom.pdf',6, 6, 'https://drive.google.com/file/d/0B1HXnM1lBuoqMzVhZjcwNTAtZWI5OS00ZDg3LWEyMzktNzZmYWY2Y2NhNWQx/view?hl=en&resourcekey=0-5DqnTtXPFvySMiWstuAYdA');






