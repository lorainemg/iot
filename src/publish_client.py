import time

from config import configure_mqtt_client, BROKER_ADDRESS, PORT, APP_ID, PASSWORD, DEVICE_ID
from mqtt_client import callbacks
from messages import create_downlink_msg

import paho.mqtt.publish as publish


if __name__ == '__main__':
    client = configure_mqtt_client()
    
    client.start_loop()
    
    callbacks.connected.wait()
    msg = create_downlink_msg(f_port=15, frm_payload="vu8=", priority="NORMAL")
    print(msg)
    
    client.publish("test/up", msg)
    # client.publish(f"v3/{APP_ID}/devices/{DEVICE_ID}/down/push", message)
    input()
    # client.publish(f"test/topic", message)
    # time.sleep(20)
    client.stop_loop()
    # import paho.mqtt.publish as publish
    #
    # publish.single(f"v3/{APP_ID}/devices/{DEVICE_ID}/down/push",
    #                '{"downlinks":[{"f_port": 15,"frm_payload":"vu8=","priority": "NORMAL"}]}',
    #                hostname=BROKER_ADDRESS, port=PORT,
    #                auth={'username': APP_ID, 'password': PASSWORD})
