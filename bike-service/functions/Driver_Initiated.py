def UploadDriverDocs(request, mydb, main_pb2):
    driver_id = request.driver_id
    bike_registration_number = request.bike_registration_number
    license_docs_link = request.license_docs_link
    docs_link = request.docs_link
    admin_id = request.admin_id

    try:
        # Inserting Driver Docs into Driver_Docs table
        sql = 'INSERT INTO Driver_Docs (bike_registration_number, license_docs_link, Admin_id, Driver_id, docs_link) values(%s, %s, %s, %s, %s)'
        val = (bike_registration_number, license_docs_link,
               admin_id, driver_id, docs_link)
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()
        return main_pb2.Acknowledgement(response=f"Driver docs uploaded successfully")
    except mydb.Error as e:
        raise e
    except Exception as e:
        raise e
    finally:
        if mydb.open:
            mycursor.close()


def GetAvailableDriversList(request, mydb, main_pb2):
    try:
        # Fetching From Driver table
        sql = 'SELECT d.id, u.name, u.phone_no, d.current_location_lat, d.current_location_long, d.rating from Driver d, User u where d.is_verified_status="verified" and d.current_status=1 and u.typeOfUser="Driver" and d.User_id=u.id'
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        result = mycursor.fetchall()
        docs_list = []

        for row in result:
            dict = {
                "driver_id": row[0],
                "driver_name": row[1],
                "phone_no": row[2],
                "current_location_lat": row[3],
                "current_location_long": row[4],
                "rating": row[5],
            }
            docs_list.append(dict)
        return main_pb2.AvailableDrivers(driver_list=docs_list)

    except mydb.Error as e:
        raise e
    except Exception as e:
        raise e
    finally:
        if mydb.open:
            mycursor.close()
