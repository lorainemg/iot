import requests
from config import APP_ID, DEVICE_ID
from pprint import pprint
from messages import get_headers, set_device_info

headers = get_headers()

def get_device_info():
    response = requests.get(
        f"https://eu1.cloud.thethings.network/api/v3/applications/{APP_ID}/devices/{DEVICE_ID}?field_mask=name,description,locations",
        headers=headers
    )
    pprint(response.json())
    return response


def put_device_info():
    data = set_device_info(name="Device to Test", description="This is a device to test HTTP api",
                           paths=["name", "description"]) 
    response = requests.put(
        f'https://eu1.cloud.thethings.network/api/v3/applications/{APP_ID}/devices/{DEVICE_ID}',
        data,
        headers=headers
    )
    pprint(response.json())


def get_event_stream():
    new_header = dict(headers)
    new_header["Accept"] = 'text/event-stream'
    new_header["Content-Type"] = "application/json"
    data = '''{
    "identifiers":[{
        "device_ids":{
            "device_id":"%s",
            "application_ids":{"application_id":"%s"}
        }
    }]
  }''' % (DEVICE_ID, APP_ID)
    response = requests.post(f'https://eu1.cloud.thethings.network/api/v3/events', data, headers=new_header)
    pprint(response.json())


def schedule_downlink():
    nheaders = {
        'Content-Type': 'application/json',
        'Authorization': headers['Authorization'],
    }
    data1 = '''{"downlinks": [{
      "frm_payload": "vu8=",
      "f_port": 42,
    }]
  }'''
    data2 = '''{"downlinks":[{
      "decoded_payload": {
        "bytes": [1, 2, 3]
      }
    }]
  }'''
    response = requests.post(
        f'https://eu1.cloud.thethings.network/api/v3/applications/{APP_ID}/devices/{DEVICE_ID}/down/push',
        data2,
        headers=nheaders
    )
    pprint(response.json())