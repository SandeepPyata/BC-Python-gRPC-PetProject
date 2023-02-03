from concurrent import futures
import main_pb2
import main_pb2_grpc
import grpc
import logging
import mysql
import mysql.connector
import pymysql
from functions import AdminFunctions, CreateProfile, Customer_Initiated, Driver_Initiated, Status_Change, UpdateProfile

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="2002",
    database="mydatabase"
)


class RideServicer(main_pb2_grpc.RideServicer):

    def CreateCustomer(self, request, context):
        return CreateProfile.CreateCustomer(request, mydb, main_pb2)

    def CreateAdmin(self, request, context):
        return CreateProfile.CreateAdmin(request, mydb, main_pb2)

    def CreateDriver(self, request, context):
        return CreateProfile.CreateDriver(request, mydb, main_pb2)

    def UpdateUserProfile(self, request, context):
        return UpdateProfile.UpdateUserProfile(request, mydb, main_pb2)

    def GetAllDriverDocs(self, request, context):
        return AdminFunctions.GetAllDriverDocs(request, mydb, main_pb2)

    def UpdateVerifiedDriverStatus(self, request, context):
        return AdminFunctions.UpdateVerifiedDriverStatus(request, mydb, main_pb2)

    def CreateBooking(self, request, context):
        return Customer_Initiated.CreateBooking(request, mydb, main_pb2)

    def CancelBooking(self, request, context):
        return Customer_Initiated.CancelBooking(request, mydb, main_pb2)

    def UpdateBookingStatus(self, request, context):
        return Status_Change.UpdateBookingStatus(request, mydb, main_pb2)

    def UpdateDriverStatus(self, request, context):
        return Status_Change.UpdateDriverStatus(request, mydb, main_pb2)

    def UpdatePaymentStatus(self, request, context):
        return Status_Change.UpdatePaymentStatus(request, mydb, main_pb2)

    def UploadDriverDocs(self, request, context):
        return Driver_Initiated.UploadDriverDocs(request, mydb, main_pb2)


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
