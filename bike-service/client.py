# from __future__ import print_function
# import logging
# import grpc
# from protos import main_pb2
# from protos import main_pb2_grpc


# def run():
#     # NOTE(gRPC Python Team): .close() is possible on a channel and should be
#     # used in circumstances in which the with statement does not fit the needs
#     # of the code.
#     with grpc.insecure_channel('localhost:50051') as channel:
#         stub = main_pb2_grpc.RideStub(channel)
#         response = stub.CreateCustomer(
#             main_pb2.CustomerDetails(typeOfUser="customer", ))


# if __name__ == '__main__':
#     logging.basicConfig()
#     run()
