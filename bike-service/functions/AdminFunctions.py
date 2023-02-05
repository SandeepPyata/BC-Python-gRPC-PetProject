def GetAllDriverDocs(request, mydb, main_pb2):
    try:
        # Fetching From Driver_Docs table
        sql = 'SELECT Driver_id, bike_registration_number, license_docs_link, docs_link FROM Driver_Docs'
        mycursor = mydb.cursor()
        mycursor.execute(sql)
        result = mycursor.fetchall()
        docs_list = []
        for row in result:
            dict = {
                "driver_id": row[0],
                "bike_registration_number": row[1],
                "license_docs_link": row[2],
                "docs_link": row[3]
            }
            docs_list.append(dict)
        return main_pb2.AllDriversDocs(driver_docs=docs_list)

    except mydb.Error as e:
        raise e
    except:
        raise e
    finally:
        if mydb.open:
            mycursor.close()


def UpdateVerifiedDriverStatus(request, mydb, main_pb2):
    driver_id = request.driver_id
    driver_verification_status = request.driver_verification_status

    try:
        # Update driver_verification_status with driver_id
        sql = 'UPDATE Driver SET is_verified_status=%s where id=%s'
        val = (driver_verification_status, driver_id)
        mycursor = mydb.cursor()
        mycursor.execute(sql, val)
        mydb.commit()
        return main_pb2.Acknowledgement(response=f"Updated driver status to {driver_verification_status}")
    except mydb.Error as e:
        raise e
    except:
        raise e
    finally:
        if mydb.open:
            mycursor.close()
