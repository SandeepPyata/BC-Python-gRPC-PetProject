def UploadDriverDocs(request, mydb, main_pb2):
    driver_id = request.driver_id
    bike_registration_number = request.bike_registration_number
    license_docs_link = request.license_docs_link
    docs_link = request.docs_link
    admin_id = request.admin_id

    # Inserting Driver Docs into Driver_Docs table
    sql = 'INSERT INTO Driver_Docs (bike_registration_number, license_docs_link, Admin_id, Driver_id, docs_link) values(%s, %s, %s, %s, %s)'
    val = (bike_registration_number, license_docs_link,
           admin_id, driver_id, docs_link)
    mycursor = mydb.cursor()
    mycursor.execute(sql, val)
    mydb.commit()

    return main_pb2.Acknowledgement(response=f"Driver docs uploaded successfully")
