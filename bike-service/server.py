from concurrent import futures
import main_pb2
import main_pb2_grpc
import grpc
import logging
import mysql
import mysql.connector
import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="2002",
    database="mydatabase"
)

print(mydb)


class RideServicer(main_pb2_grpc.RideServicer):

    def CreateCustomer(self, request, context):
        user = {
            "name": request.user.name,
            "address": request.user.address,
            "phoneno": request.user.phoneno,
            "email": request.user.email,
        }

        mycursor = mydb.cursor()

        # Testing purpose
        sql = 'delete from User where name="Hell"'
        mycursor.execute(sql)
        mydb.commit()

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
        last_inserted_id = myresult[0]

        # Inserting into Customer as foreign key
        sql = 'insert into Customer (userID) values(%s)'
        val = (last_inserted_id,)
        mycursor.execute(sql, val)
        mydb.commit()

        # Printing after insertion
        myresult = mycursor.execute('select * from User')
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)

        return main_pb2.CustomerDetails(typeOfUser="Customer", user=user)

    def CreateAdmin(self, request, context):
        user = {
            "name": request.user.name,
            "address": request.user.address,
            "phoneno": request.user.phoneno,
            "email": request.user.email,
        }

        mycursor = mydb.cursor()

        sql = 'delete from User where name="Hell"'
        mycursor.execute(sql)
        mydb.commit()

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
        last_inserted_id = myresult[0]

        # Inserting into Customer as foreign key
        sql = 'insert into Customer (userID) values(%s)'
        val = (last_inserted_id,)
        mycursor.execute(sql, val)
        mydb.commit()

        # Printing after insertion
        myresult = mycursor.execute('select * from User')
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)

        return main_pb2.CustomerDetails(typeOfUser="Customer", user=user)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    print("Server running")
    main_pb2_grpc.add_RideServicer_to_server(
        RideServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
