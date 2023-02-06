from dateutil.parser import parse
from functions import Email_Service


def CreateBooking(request, mydb, main_pb2):

    booked_time = parse(request.booked_time, fuzzy=True)
    final_fare = request.final_fare
    driver_id = request.driver_id
    customer_id = request.customer_id
    booking_status = 0
    payment_status = 0
    pickup_location_text = request.pickup_location_text
    drop_location_text = request.drop_location_text
    pickup_location_lat = request.pickup_location_lat
    pickup_location_long = request.pickup_location_long
    drop_location_lat = request.drop_location_lat
    drop_location_long = request.drop_location_long

    try:
        # Insert Into Booking Table
        sql = 'INSERT INTO Bookings (booked_time, final_fare, booking_status, payment_status, Driver_id, Customer_id, pickup_location_text, drop_location_text, pickup_lat, pickup_long, drop_lat, drop_long) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
        val = (booked_time, final_fare, booking_status, payment_status,  driver_id, customer_id, pickup_location_text,
               drop_location_text, pickup_location_lat, pickup_location_long, drop_location_lat, drop_location_long)
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)

        # Change driver availability status to in-trip in Driver table
        sql = 'UPDATE Driver SET current_status = 2 where id=%s'
        mycursor = mydb.cursor()
        mycursor.execute(sql, (driver_id,))

        # Send Email notification to customer
        # Fetch customer details
        sql = 'SELECT u.name, u.email_id from User u where u.id=%s'
        myresult = mycursor.execute(sql, (customer_id,))
        result = list(list(mycursor.fetchall())[0])
        customer_name, customer_email = result[0], result[1]

        # Fetch driver details
        sql = 'SELECT u.name from User u where u.id=%s'
        myresult = mycursor.execute(sql, (driver_id,))
        result = list(list(mycursor.fetchall())[0])
        driver_name = result[0]
        Email_Service.Send_Email(
            customer_email, f'Bike booked by {customer_name}; Allocated driver: {driver_name}')

        mydb.commit()
        return main_pb2.Acknowledgement(response=f"Bike booked from {pickup_location_text} to {drop_location_text}")
    except mydb.Error as e:
        raise e
    except Exception as e:
        raise e
    finally:
        if mydb.open:
            mycursor.close()


def CancelBooking(request, mydb, main_pb2):
    booking_id = request.booking_id

    try:
        # Updating the booking status, payment status
        sql = 'UPDATE Bookings SET booking_status=1, payment_status=2 where booking_id=%s'
        mycursor = mydb.cursor()
        mycursor.execute(sql, (booking_id,))
        ack = "Booking status updated to CANCELLED, Payment status updated to NOTAPPLICABLE, "

        # Updating status in Driver table
        sql = 'UPDATE Driver SET current_status = 1 where id=(SELECT Driver_id From Bookings where booking_id=%s)'
        val = (id,)
        mycursor.execute(sql, val)
        ack += "Driver status updated to AVAILABLE"

        mydb.commit()
        return main_pb2.Acknowledgement(response=ack)
    except mydb.Error as e:
        raise e
    except Exception as e:
        raise e
    finally:
        if mydb.open:
            mycursor.close()
