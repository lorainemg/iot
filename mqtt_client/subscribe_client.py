import time

from config import configure_mqtt_client, BROKER_ADDRESS, PORT, APP_ID, PASSWORD
# import paho.mqtt.subscribe as subscribe

import callbacks

if __name__ == '__main__':
    client = configure_mqtt_client()
    client.start_loop()
    callbacks.connected.wait()

    client.subscribe_to_topic("test/up")
    # client.subscribe_to_topic("#")
    # client.loop_forever()
    # client.client.loop(50)
    input()
    client.stop_loop()
    # m = subscribe.simple(topics=["#"], hostname=BROKER_ADDRESS, port=PORT,
    #                      auth={'username': APP_ID, 'password': PASSWORD})
    # # for a in m:
    # #     print(a.topic)
    # #     print(a.payload)
    # print(m.topic)
    # print(m.payload)
