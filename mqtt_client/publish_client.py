import time

from config import configure_mqtt_client, BROKER_ADDRESS, PORT, APP_ID, PASSWORD, DEVICE_ID
import callbacks
import paho.mqtt.publish as publish

if __name__ == '__main__':
    client = configure_mqtt_client()
    # client.subscribe_to_topic(f"#")
    message = '''{
          "downlinks": [{
            "f_port": 15,
            "frm_payload": "vu8=",
            "priority": "NORMAL"
          }]
        }'''
    client.start_loop()
    callbacks.connected.wait()

    client.publish("test/up", "on")
    # client.publish(f"v3/{APP_ID}/devices/{DEVICE_ID}/down/push", message)
    input()
    # client.publish(f"test/topic", message)
    # time.sleep(20)
    # client.stop_loop()
    # import paho.mqtt.publish as publish
    #
    # publish.single(f"v3/{APP_ID}/devices/{DEVICE_ID}/down/push",
    #                '{"downlinks":[{"f_port": 15,"frm_payload":"vu8=","priority": "NORMAL"}]}',
    #                hostname=BROKER_ADDRESS, port=PORT,
    #                auth={'username': APP_ID, 'password': PASSWORD})
