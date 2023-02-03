def UpdateBookingStatus(request, mydb, main_pb2):
    booking_id = request.booking_id
    booking_status_code = request.status

    # Updating the status
    sql = 'UPDATE Bookings SET booking_status=%s where booking_id=%s'
    val = (booking_id, booking_status_code)
    mycursor = mydb.cursor()
    mycursor.execute(sql, val)
    mydb.commit()
    status = {
        0: "BOOKED",
        1: "CANCELLED",
        2: "INPROGRESS",
        3: "COMPLETED"
    }
    return main_pb2.Acknowledgement(response=f"Booking status updated to {status[booking_status_code]}")


def UpdateDriverStatus(request, mydb, main_pb2):
    id = request.driver_id
    status_code = request.status

    # Updating status in Driver table
    sql = 'UPDATE Driver SET current_status = %s where id=%s'
    val = (status_code, id)
    mycursor = mydb.cursor()
    mycursor.execute(sql, val)
    mydb.commit()
    status = {
        0: "UNAVAILABLE",
        1: "AVAILABLE",
        2: "IN_TRIP"
    }
    return main_pb2.Acknowledgement(response=f"Driver current status updated to {status[status_code]}")


def UpdatePaymentStatus(request, mydb, main_pb2):
    booking_id = request.booking_id
    payment_status_code = request.status

    # Updating payment status in Bookings Table
    sql = 'UPDATE Bookings SET payment_status=%s where booking_id=%s'
    val = (booking_id, payment_status_code)
    mycursor = mydb.cursor()
    mycursor.execute(sql, val)
    mydb.commit()

    status = {
        0: "NOTPAID",
        1: "PAID",
        2: "NOTAPPLICABLE",
    }
    return main_pb2.Acknowledgement(response=f"Payment status updated to {status[payment_status_code]}")
