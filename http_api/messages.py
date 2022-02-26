from typing import List
from protobuf.headers_pb2 import Headers
from protobuf.device_info_pb2 import SetDeviceInfo, EndDevice, FieldMask
from config import HTTP_API_KEY, APP_ID, DEVICE_ID
from google.protobuf.json_format import Parse, MessageToJson, MessageToDict


def get_headers():
    header = Headers(Authorization=f"Bearer {HTTP_API_KEY}", Accept="application/json")
    return MessageToDict(header)


def set_device_info(name: str, description: str, paths: List[str]):
     device_info_data = SetDeviceInfo(end_device=EndDevice(name=name, description=description),
                                      field_mask=FieldMask(paths=paths))
     return MessageToJson(device_info_data, preserving_proto_field_name=True)