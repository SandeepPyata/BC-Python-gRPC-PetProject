from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Acknowledgement(_message.Message):
    __slots__ = ["response"]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: str
    def __init__(self, response: _Optional[str] = ...) -> None: ...

class AdminDetails(_message.Message):
    __slots__ = ["id", "typeOfUser", "user"]
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPEOFUSER_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    id: int
    typeOfUser: str
    user: UserProfileDetails
    def __init__(self, id: _Optional[int] = ..., typeOfUser: _Optional[str] = ..., user: _Optional[_Union[UserProfileDetails, _Mapping]] = ...) -> None: ...

class AllDriversDocs(_message.Message):
    __slots__ = ["driver_docs"]
    DRIVER_DOCS_FIELD_NUMBER: _ClassVar[int]
    driver_docs: _containers.RepeatedCompositeFieldContainer[SingleDriverDocs]
    def __init__(self, driver_docs: _Optional[_Iterable[_Union[SingleDriverDocs, _Mapping]]] = ...) -> None: ...

class AvailableDrivers(_message.Message):
    __slots__ = ["driver_list"]
    class Drivers(_message.Message):
        __slots__ = ["current_location_lat", "current_location_long", "driver_id", "driver_name", "phone_no", "rating"]
        CURRENT_LOCATION_LAT_FIELD_NUMBER: _ClassVar[int]
        CURRENT_LOCATION_LONG_FIELD_NUMBER: _ClassVar[int]
        DRIVER_ID_FIELD_NUMBER: _ClassVar[int]
        DRIVER_NAME_FIELD_NUMBER: _ClassVar[int]
        PHONE_NO_FIELD_NUMBER: _ClassVar[int]
        RATING_FIELD_NUMBER: _ClassVar[int]
        current_location_lat: float
        current_location_long: float
        driver_id: int
        driver_name: str
        phone_no: int
        rating: int
        def __init__(self, driver_id: _Optional[int] = ..., driver_name: _Optional[str] = ..., phone_no: _Optional[int] = ..., current_location_lat: _Optional[float] = ..., current_location_long: _Optional[float] = ..., rating: _Optional[int] = ...) -> None: ...
    DRIVER_LIST_FIELD_NUMBER: _ClassVar[int]
    driver_list: _containers.RepeatedCompositeFieldContainer[AvailableDrivers.Drivers]
    def __init__(self, driver_list: _Optional[_Iterable[_Union[AvailableDrivers.Drivers, _Mapping]]] = ...) -> None: ...

class BookingDetails(_message.Message):
    __slots__ = ["booked", "booked_time", "customer_id", "driver_id", "drop_location_lat", "drop_location_long", "drop_location_text", "final_fare", "pickup_location_lat", "pickup_location_long", "pickup_location_text"]
    BOOKED_FIELD_NUMBER: _ClassVar[int]
    BOOKED_TIME_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    DRIVER_ID_FIELD_NUMBER: _ClassVar[int]
    DROP_LOCATION_LAT_FIELD_NUMBER: _ClassVar[int]
    DROP_LOCATION_LONG_FIELD_NUMBER: _ClassVar[int]
    DROP_LOCATION_TEXT_FIELD_NUMBER: _ClassVar[int]
    FINAL_FARE_FIELD_NUMBER: _ClassVar[int]
    PICKUP_LOCATION_LAT_FIELD_NUMBER: _ClassVar[int]
    PICKUP_LOCATION_LONG_FIELD_NUMBER: _ClassVar[int]
    PICKUP_LOCATION_TEXT_FIELD_NUMBER: _ClassVar[int]
    booked: bool
    booked_time: str
    customer_id: int
    driver_id: int
    drop_location_lat: float
    drop_location_long: float
    drop_location_text: str
    final_fare: int
    pickup_location_lat: float
    pickup_location_long: float
    pickup_location_text: str
    def __init__(self, booked_time: _Optional[str] = ..., final_fare: _Optional[int] = ..., driver_id: _Optional[int] = ..., customer_id: _Optional[int] = ..., pickup_location_text: _Optional[str] = ..., drop_location_text: _Optional[str] = ..., pickup_location_lat: _Optional[float] = ..., pickup_location_long: _Optional[float] = ..., drop_location_lat: _Optional[float] = ..., drop_location_long: _Optional[float] = ..., booked: bool = ...) -> None: ...

class BookingId(_message.Message):
    __slots__ = ["booking_id"]
    BOOKING_ID_FIELD_NUMBER: _ClassVar[int]
    booking_id: int
    def __init__(self, booking_id: _Optional[int] = ...) -> None: ...

class BookingStatus(_message.Message):
    __slots__ = ["booking_id", "status"]
    class StatusType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    BOOKED: BookingStatus.StatusType
    BOOKING_ID_FIELD_NUMBER: _ClassVar[int]
    CANCELLED: BookingStatus.StatusType
    COMPLETED: BookingStatus.StatusType
    INPROGRESS: BookingStatus.StatusType
    STATUS_FIELD_NUMBER: _ClassVar[int]
    booking_id: int
    status: BookingStatus.StatusType
    def __init__(self, booking_id: _Optional[int] = ..., status: _Optional[_Union[BookingStatus.StatusType, str]] = ...) -> None: ...

class CustomerDetails(_message.Message):
    __slots__ = ["id", "rating", "typeOfUser", "user"]
    ID_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    TYPEOFUSER_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    id: int
    rating: int
    typeOfUser: str
    user: UserProfileDetails
    def __init__(self, id: _Optional[int] = ..., typeOfUser: _Optional[str] = ..., rating: _Optional[int] = ..., user: _Optional[_Union[UserProfileDetails, _Mapping]] = ...) -> None: ...

class DriverAvailabilityStatus(_message.Message):
    __slots__ = ["driver_id", "status"]
    class StatusType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AVAILABLE: DriverAvailabilityStatus.StatusType
    DRIVER_ID_FIELD_NUMBER: _ClassVar[int]
    IN_TRIP: DriverAvailabilityStatus.StatusType
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UNAVAILABLE: DriverAvailabilityStatus.StatusType
    driver_id: int
    status: DriverAvailabilityStatus.StatusType
    def __init__(self, driver_id: _Optional[int] = ..., status: _Optional[_Union[DriverAvailabilityStatus.StatusType, str]] = ...) -> None: ...

class DriverDetails(_message.Message):
    __slots__ = ["current_location_lat", "current_location_long", "driver_availability_status", "driver_verified_status", "id", "rating", "typeOfUser", "user"]
    class StatusType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    AVAILABLE: DriverDetails.StatusType
    CURRENT_LOCATION_LAT_FIELD_NUMBER: _ClassVar[int]
    CURRENT_LOCATION_LONG_FIELD_NUMBER: _ClassVar[int]
    DRIVER_AVAILABILITY_STATUS_FIELD_NUMBER: _ClassVar[int]
    DRIVER_VERIFIED_STATUS_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    IN_TRIP: DriverDetails.StatusType
    RATING_FIELD_NUMBER: _ClassVar[int]
    TYPEOFUSER_FIELD_NUMBER: _ClassVar[int]
    UNAVAILABLE: DriverDetails.StatusType
    USER_FIELD_NUMBER: _ClassVar[int]
    current_location_lat: float
    current_location_long: float
    driver_availability_status: DriverDetails.StatusType
    driver_verified_status: str
    id: int
    rating: int
    typeOfUser: str
    user: UserProfileDetails
    def __init__(self, id: _Optional[int] = ..., typeOfUser: _Optional[str] = ..., current_location_lat: _Optional[float] = ..., current_location_long: _Optional[float] = ..., rating: _Optional[int] = ..., driver_availability_status: _Optional[_Union[DriverDetails.StatusType, str]] = ..., driver_verified_status: _Optional[str] = ..., user: _Optional[_Union[UserProfileDetails, _Mapping]] = ...) -> None: ...

class DriverVerificationStatus(_message.Message):
    __slots__ = ["driver_id", "driver_verification_status"]
    DRIVER_ID_FIELD_NUMBER: _ClassVar[int]
    DRIVER_VERIFICATION_STATUS_FIELD_NUMBER: _ClassVar[int]
    driver_id: int
    driver_verification_status: str
    def __init__(self, driver_id: _Optional[int] = ..., driver_verification_status: _Optional[str] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class PaymentStatus(_message.Message):
    __slots__ = ["booking_id", "status"]
    class StatusType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    BOOKING_ID_FIELD_NUMBER: _ClassVar[int]
    NOTAPPLICABLE: PaymentStatus.StatusType
    NOTPAID: PaymentStatus.StatusType
    PAID: PaymentStatus.StatusType
    STATUS_FIELD_NUMBER: _ClassVar[int]
    booking_id: int
    status: PaymentStatus.StatusType
    def __init__(self, booking_id: _Optional[int] = ..., status: _Optional[_Union[PaymentStatus.StatusType, str]] = ...) -> None: ...

class SingleDriverDocs(_message.Message):
    __slots__ = ["admin_id", "bike_registration_number", "docs_link", "driver_id", "license_docs_link"]
    ADMIN_ID_FIELD_NUMBER: _ClassVar[int]
    BIKE_REGISTRATION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DOCS_LINK_FIELD_NUMBER: _ClassVar[int]
    DRIVER_ID_FIELD_NUMBER: _ClassVar[int]
    LICENSE_DOCS_LINK_FIELD_NUMBER: _ClassVar[int]
    admin_id: int
    bike_registration_number: str
    docs_link: str
    driver_id: int
    license_docs_link: str
    def __init__(self, driver_id: _Optional[int] = ..., bike_registration_number: _Optional[str] = ..., license_docs_link: _Optional[str] = ..., docs_link: _Optional[str] = ..., admin_id: _Optional[int] = ...) -> None: ...

class UserProfileDetails(_message.Message):
    __slots__ = ["address", "email", "name", "phoneno"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHONENO_FIELD_NUMBER: _ClassVar[int]
    address: str
    email: str
    name: str
    phoneno: int
    def __init__(self, name: _Optional[str] = ..., address: _Optional[str] = ..., phoneno: _Optional[int] = ..., email: _Optional[str] = ...) -> None: ...
