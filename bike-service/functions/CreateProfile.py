'''
Considerations:
1. No Driver/Admin/Customer uses same email for 2 profiles

'''


def CheckForUser(mycursor, email, typeOfUser):
    try:
        sql = 'select id from User where email_id=%s'
        result = mycursor.execute(sql, (email,))
        if (result != 0):
            raise Exception(f"{typeOfUser} already exists")
    except Exception as e:
        raise e


def CreateCustomer(request, mydb, main_pb2):
    user = {
        "name": request.user.name,
        "address": request.user.address,
        "phoneno": request.user.phoneno,
        "email": request.user.email,
    }

    try:
        mycursor = mydb.cursor()

        # Check if user exists
        CheckForUser(mycursor, user["email"], "Customer")

        #  inserting into User table
        sql = 'insert into User (typeOfUser, name, address, phone_no, email_id) values(%s,%s,%s,%s,%s)'
        val = ('Customer', user["name"],
               user["address"], user["phoneno"], user["email"])
        mycursor.execute(sql, val)

        # Inserting into Customer as foreign key
        sql = 'insert into Customer(`User_id`) select `id` from User order by `id` desc limit 1'
        mycursor.execute(sql)

        mydb.commit()
        print("Committed")
        return main_pb2.CustomerDetails(typeOfUser="Customer", user=user)

    except mydb.Error as e:
        raise e
    except Exception as e:
        raise e
    finally:
        if mydb.open:
            mycursor.close()


def CreateAdmin(request, mydb, main_pb2):
    user = {
        "name": request.user.name,
        "address": request.user.address,
        "phoneno": request.user.phoneno,
        "email": request.user.email,
    }
    try:
        mycursor = mydb.cursor()

        # Check if user exists
        CheckForUser(mycursor, user["email"], "Admin")

        # Inserting into Customer as foreign key
        sql = 'insert into Admin(`User_id`) select `id` from User order by `id` desc limit 1'
        mycursor.execute(sql)
        mydb.commit()

        return main_pb2.AdminDetails(typeOfUser="Admin", user=user)

    except mydb.Error as e:
        raise e
    except Exception as e:
        raise e
    finally:
        if mydb.open:
            mycursor.close()


def CreateDriver(request, mydb, main_pb2):
    user = {
        "name": request.user.name,
        "address": request.user.address,
        "phoneno": request.user.phoneno,
        "email": request.user.email,
    }
    details = {
        "typeOfUser": "Driver",
        "current_location_long": request.current_location_long,
        "current_location_lat": request.current_location_lat,
        "rating": 0,
        "driver_availability_status": 0,
        "driver_verified_status": "unverified",
        "user": user
    }
    try:
        mycursor = mydb.cursor()

        # Check if user exists
        CheckForUser(mycursor, user["email"], "Driver")

        #  inserting into User table
        sql = 'insert into User (typeOfUser, name, address, phone_no, email_id) values(%s,%s,%s,%s,%s)'
        val = (details["typeOfUser"], user["name"],
               user["address"], user["phoneno"], user["email"])
        mycursor.execute(sql, val)
        mydb.commit()

        # Getting last inserted row id from User table
        myresult = mycursor.execute(
            'select id from User order by id desc limit 1')
        myresult = mycursor.fetchall()
        last_inserted_id = list(myresult[0])[0]

        # Inserting into Customer as foreign key
        sql = 'insert into Driver (User_id,current_location_lat, current_location_long, is_verified_status, rating, current_status) values(%s,%s,%s,%s,%s,%s)'
        val = (last_inserted_id, details["current_location_lat"], details["current_location_long"],
               details["driver_verified_status"], details["rating"], details["driver_availability_status"])
        mycursor.execute(sql, val)
        mydb.commit()

        return main_pb2.DriverDetails(id=last_inserted_id, typeOfUser="Driver", driver_availabilty_status="unavailable", driver_verified_status="unverified", user=user)

    except mydb.Error as e:
        raise e
    except Exception as e:
        raise e
    finally:
        if mydb.open:
            mycursor.close()
