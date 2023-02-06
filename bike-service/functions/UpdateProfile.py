def UpdateUserProfile(request, mydb, main_pb2):

    details = {
        "name": request.name,
        "address": request.address,
        "phoneno": request.phoneno,
        "email": request.email
    }

    try:
        # Modifying User table
        sql = 'UPDATE User SET address=%s, phone_no=%s, name=%s WHERE email_id=%s'
        val = (details["address"], details["phoneno"],
               details["name"], details["email"])
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()

        return main_pb2.Acknowledgement(response=f'{details["name"]} profile updated')
    except mydb.Error as e:
        raise e
    except Exception as e:
        raise e
    finally:
        if mydb.open:
            mycursor.close()
