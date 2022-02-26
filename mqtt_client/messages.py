from protos.downlink_pb2 import Downlinks
from protos.join_pb2 import JoinResponse
from google.protobuf.json_format import MessageToJson, Parse

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

def load_join_response(response: str) -> JoinResponse:
    '''
    Helper function to load the response of a join call (for example, response of v3/app1@tenant1/devices/dev1/join).
    
    Example:
    {
        "end_device_ids": {
            "device_id": "dev1",
            "application_ids": {
            "application_id": "app1"
            },
            "dev_eui": "4200000000000000",
            "join_eui": "4200000000000000",
            "dev_addr": "01DA1F15"
        },
        "correlation_ids": [
            "gs:conn:01D2CSNX7FJVKQPCVG612QF1TX",
            "gs:uplink:01D2CT834K2YD17ZWZ6357HC0Z",
            "ns:uplink:01D2CT834KNYD7BT2NHK5R1WVA",
            "rpc:/ttn.lorawan.v3.GsNs/HandleUplink:01D2CT834KJ4AVSD1SJ637NAV6",
            "as:up:01D2CT83AXQFQYQ35SR74CTWKH"
        ],
        "join_accept": {
            "session_key_id": "AWiZpAyXrAfEkUNkBljRoA=="
        }
    }
    '''
    join_response = JoinResponse()
    Parse(response, join_response)
    return join_response
    