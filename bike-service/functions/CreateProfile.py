def CreateCustomer(request, mydb, main_pb2):
    user = {
        "name": request.user.name,
        "address": request.user.address,
        "phoneno": request.user.phoneno,
        "email": request.user.email,
    }
    mycursor = mydb.cursor()
    #  inserting into User table
    sql = 'insert into User (typeOfUser, name, address, phone_no, email_id) values(%s,%s,%s,%s,%s)'
    val = ('Customer', user["name"],
           user["address"], user["phoneno"], user["email"])
    mycursor.execute(sql, val)
    mydb.commit()

    # Getting last inserted row id from User table
    myresult = mycursor.execute(
        'select id from User order by id desc limit 1')
    myresult = mycursor.fetchall()
    last_inserted_id = list(myresult[0])[0]

    # Inserting into Customer as foreign key
    sql = 'insert into Customer (User_id) values(%s)'
    val = (last_inserted_id,)
    mycursor.execute(sql, val)
    mydb.commit()

    return main_pb2.CustomerDetails(id=last_inserted_id, typeOfUser="Customer", user=user)


def CreateAdmin(request, mydb, main_pb2):
    user = {
        "name": request.user.name,
        "address": request.user.address,
        "phoneno": request.user.phoneno,
        "email": request.user.email,
    }

    mycursor = mydb.cursor()

    #  inserting into User table
    sql = 'insert into User (typeOfUser, name, address, phone_no, email_id) values(%s,%s,%s,%s,%s)'
    val = ('Admin', user["name"],
           user["address"], user["phoneno"], user["email"])
    mycursor.execute(sql, val)
    mydb.commit()

    # Getting last inserted row id from User table
    myresult = mycursor.execute(
        'select id from User order by id desc limit 1')
    myresult = mycursor.fetchall()
    last_inserted_id = list(myresult[0])[0]

    # Inserting into Customer as foreign key
    sql = 'insert into Admin (User_id) values(%s)'
    val = (last_inserted_id,)
    mycursor.execute(sql, val)
    mydb.commit()

    return main_pb2.AdminDetails(id=last_inserted_id, typeOfUser="Admin", user=user)


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

    mycursor = mydb.cursor()

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
