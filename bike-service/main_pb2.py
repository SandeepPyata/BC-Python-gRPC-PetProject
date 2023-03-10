# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: main.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nmain.proto\x12\x08mainFile\"\x8f\x01\n\rPaymentStatus\x12\x12\n\nbooking_id\x18\x01 \x01(\x05\x12\x32\n\x06status\x18\x02 \x01(\x0e\x32\".mainFile.PaymentStatus.StatusType\"6\n\nStatusType\x12\x0b\n\x07NotPaid\x10\x00\x12\x08\n\x04Paid\x10\x01\x12\x11\n\rNotApplicable\x10\x02\"Q\n\x18\x44riverAvailabilityStatus\x12\x11\n\tdriver_id\x18\x01 \x01(\x05\x12\"\n\x1a\x64river_availability_status\x18\x02 \x01(\t\"\x1f\n\tBookingId\x12\x12\n\nbooking_id\x18\x01 \x01(\x05\"\x9e\x01\n\rBookingStatus\x12\x12\n\nbooking_id\x18\x01 \x01(\x05\x12\x32\n\x06status\x18\x02 \x01(\x0e\x32\".mainFile.BookingStatus.StatusType\"E\n\nStatusType\x12\n\n\x06\x42ooked\x10\x00\x12\x0c\n\x08\x43\x61nceled\x10\x01\x12\x0e\n\nInProgress\x10\x02\x12\r\n\tCompleted\x10\x03\"\x8d\x02\n\x0e\x42ookingDetails\x12\x13\n\x0b\x62ooked_time\x18\x01 \x01(\t\x12\x12\n\nfinal_fare\x18\x02 \x01(\x05\x12\x11\n\tdriver_id\x18\x03 \x01(\x05\x12\x13\n\x0b\x63ustomer_id\x18\x04 \x01(\x05\x12\x1c\n\x14pickup_location_text\x18\x05 \x01(\t\x12\x1a\n\x12\x64rop_location_text\x18\x06 \x01(\t\x12\x1b\n\x13pickup_location_lat\x18\x07 \x01(\x01\x12\x1c\n\x14pickup_location_long\x18\x08 \x01(\x01\x12\x19\n\x11\x64rop_location_lat\x18\t \x01(\x01\x12\x1a\n\x12\x64rop_location_long\x18\n \x01(\x01\"#\n\x0f\x41\x63knowledgement\x12\x10\n\x08response\x18\x01 \x01(\t\"Q\n\x18\x44riverVerificationStatus\x12\x11\n\tdriver_id\x18\x01 \x01(\x05\x12\"\n\x1a\x64river_verification_status\x18\x02 \x01(\t\"A\n\x0e\x41llDriversDocs\x12/\n\x0b\x64river_docs\x18\x01 \x03(\x0b\x32\x1a.mainFile.SingleDriverDocs\"u\n\x10SingleDriverDocs\x12\x11\n\tdriver_id\x18\x01 \x01(\x05\x12 \n\x18\x62ike_registration_number\x18\x02 \x01(\t\x12\x19\n\x11license_docs_link\x18\x03 \x01(\t\x12\x11\n\tdocs_link\x18\x04 \x01(\t\"\x06\n\x04void\"\xec\x01\n\rDriverDetails\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\ntypeOfUser\x18\x02 \x01(\t\x12\x1c\n\x14\x63urrent_location_lat\x18\x03 \x01(\x01\x12\x1d\n\x15\x63urrent_location_long\x18\x04 \x01(\x01\x12\x0e\n\x06rating\x18\x05 \x01(\x05\x12\"\n\x1a\x64river_availability_status\x18\x06 \x01(\t\x12\x1e\n\x16\x64river_verified_status\x18\x07 \x01(\t\x12*\n\x04user\x18\x08 \x01(\x0b\x32\x1c.mainFile.UserProfileDetails\"Z\n\x0c\x41\x64minDetails\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\ntypeOfUser\x18\x02 \x01(\t\x12*\n\x04user\x18\x03 \x01(\x0b\x32\x1c.mainFile.UserProfileDetails\"m\n\x0f\x43ustomerDetails\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\ntypeOfUser\x18\x02 \x01(\t\x12\x0e\n\x06rating\x18\x03 \x01(\x05\x12*\n\x04user\x18\x04 \x01(\x0b\x32\x1c.mainFile.UserProfileDetails\"S\n\x12UserProfileDetails\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x0f\n\x07phoneno\x18\x03 \x01(\x04\x12\r\n\x05\x65mail\x18\x04 \x01(\t2\xa1\x08\n\x04Ride\x12H\n\x0e\x43reateCustomer\x12\x19.mainFile.CustomerDetails\x1a\x19.mainFile.CustomerDetails\"\x00\x12?\n\x0b\x43reateAdmin\x12\x16.mainFile.AdminDetails\x1a\x16.mainFile.AdminDetails\"\x00\x12\x42\n\x0c\x43reateDriver\x12\x17.mainFile.DriverDetails\x1a\x17.mainFile.DriverDetails\"\x00\x12O\n\x15UpdateCustomerDetails\x12\x19.mainFile.CustomerDetails\x1a\x19.mainFile.CustomerDetails\"\x00\x12\x46\n\x12UpdateAdminDetails\x12\x16.mainFile.AdminDetails\x1a\x16.mainFile.AdminDetails\"\x00\x12I\n\x13UpdateDriverDetails\x12\x17.mainFile.DriverDetails\x1a\x17.mainFile.DriverDetails\"\x00\x12>\n\x10GetAllDriverDocs\x12\x0e.mainFile.void\x1a\x18.mainFile.AllDriversDocs\"\x00\x12]\n\x1aUpdateVerifiedDriverStatus\x12\".mainFile.DriverVerificationStatus\x1a\x19.mainFile.Acknowledgement\"\x00\x12\x46\n\rCreateBooking\x12\x18.mainFile.BookingDetails\x1a\x19.mainFile.Acknowledgement\"\x00\x12K\n\x13UpdateBookingStatus\x12\x17.mainFile.BookingStatus\x1a\x19.mainFile.Acknowledgement\"\x00\x12\x41\n\rCancelBooking\x12\x13.mainFile.BookingId\x1a\x19.mainFile.Acknowledgement\"\x00\x12U\n\x12UpdateDriverStatus\x12\".mainFile.DriverAvailabilityStatus\x1a\x19.mainFile.Acknowledgement\"\x00\x12K\n\x13UpdatePaymentStatus\x12\x17.mainFile.PaymentStatus\x1a\x19.mainFile.Acknowledgement\"\x00\x12K\n\x10UploadDriverDocs\x12\x1a.mainFile.SingleDriverDocs\x1a\x19.mainFile.Acknowledgement\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'main_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PAYMENTSTATUS._serialized_start=25
  _PAYMENTSTATUS._serialized_end=168
  _PAYMENTSTATUS_STATUSTYPE._serialized_start=114
  _PAYMENTSTATUS_STATUSTYPE._serialized_end=168
  _DRIVERAVAILABILITYSTATUS._serialized_start=170
  _DRIVERAVAILABILITYSTATUS._serialized_end=251
  _BOOKINGID._serialized_start=253
  _BOOKINGID._serialized_end=284
  _BOOKINGSTATUS._serialized_start=287
  _BOOKINGSTATUS._serialized_end=445
  _BOOKINGSTATUS_STATUSTYPE._serialized_start=376
  _BOOKINGSTATUS_STATUSTYPE._serialized_end=445
  _BOOKINGDETAILS._serialized_start=448
  _BOOKINGDETAILS._serialized_end=717
  _ACKNOWLEDGEMENT._serialized_start=719
  _ACKNOWLEDGEMENT._serialized_end=754
  _DRIVERVERIFICATIONSTATUS._serialized_start=756
  _DRIVERVERIFICATIONSTATUS._serialized_end=837
  _ALLDRIVERSDOCS._serialized_start=839
  _ALLDRIVERSDOCS._serialized_end=904
  _SINGLEDRIVERDOCS._serialized_start=906
  _SINGLEDRIVERDOCS._serialized_end=1023
  _VOID._serialized_start=1025
  _VOID._serialized_end=1031
  _DRIVERDETAILS._serialized_start=1034
  _DRIVERDETAILS._serialized_end=1270
  _ADMINDETAILS._serialized_start=1272
  _ADMINDETAILS._serialized_end=1362
  _CUSTOMERDETAILS._serialized_start=1364
  _CUSTOMERDETAILS._serialized_end=1473
  _USERPROFILEDETAILS._serialized_start=1475
  _USERPROFILEDETAILS._serialized_end=1558
  _RIDE._serialized_start=1561
  _RIDE._serialized_end=2618
# @@protoc_insertion_point(module_scope)
