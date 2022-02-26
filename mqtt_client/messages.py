from protos.downlink_pb2 import Downlinks
from google.protobuf.json_format import MessageToJson

def create_downlink_msg(f_port: int, frm_payload: str, priority: str) -> str:
    '''
    Helper function to create a downlink message. 
    Uses protobuf files to represent the structure of the message
    
    Example message:
    {
        "downlinks": [{
            "f_port": 15,
            "frm_payload": "vu8=",
            "priority": "NORMAL"
        }]
    }
    '''
    downlinks = Downlinks()
    downlinks.downlink.add(f_port=f_port, frm_payload=frm_payload, priority=priority) 
    return MessageToJson(downlinks)