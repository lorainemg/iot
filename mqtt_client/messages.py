from protos.downlink_pb2 import Downlinks
from google.protobuf.json_format import MessageToDict

def create_downlink_msg(f_port: int, frm_payload: str, priority: str) -> str:
    downlinks = Downlinks()
    downlinks.downlink.add(f_port=f_port, frm_payload=frm_payload, priority=priority)
    d = MessageToDict(downlinks)
    return str(d)