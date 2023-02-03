def UpdateUserProfile(request, mydb, main_pb2):
    mycursor = mydb.cursor()

    details = {
        "name": request.name,
        "address": request.address,
        "phoneno": request.phoneno,
        "email": request.email
    }

    # Modifying User table
    sql = 'UPDATE User SET address=%s, phone_no=%s, email_id=%s WHERE name=%s'
    val = (details["address"], details["phoneno"],
           details["email"], details["name"])
    mycursor.execute(sql, val)
    mydb.commit()

    return main_pb2.Acknowledgement(response=f'{details["name"]} profile updated')


'''
def UpdateCustomerDetails(self, request, context):
    user = {
        "name": request.user.name,
        "address": request.user.address,
        "phoneno": request.user.phoneno,
        "email": request.user.email,
    }
    self.UpdateUserProfile(user)
    return main_pb2.CustomerDetails(typeOfUser="Customer", user=user)


def UpdateAdminDetails(self, request, context):
    user = {
        "name": request.user.name,
        "address": request.user.address,
        "phoneno": request.user.phoneno,
        "email": request.user.email,
    }
    self.UpdateUserProfile(user)
    return main_pb2.AdminDetails(typeOfUser="Admin", user=user)


def UpdateDriverDetails(self, request, context):
    user = {
        "name": request.user.name,
        "address": request.user.address,
        "phoneno": request.user.phoneno,
        "email": request.user.email,
    }
    self.UpdateUserProfile(user)
    return main_pb2.DriverDetails(typeOfUser="Driver", user=user)
'''
