import paho.mqtt.client as mqtt
from typing import List
from callbacks import on_connect, on_publish, on_subscribe, on_message, on_log
from utils import encode, decode, endpoints
from uuid import uuid1

class MQTTClient:
    def __init__(self, broker_address: str, port: int, auth_info: dict):
        self.broker_address = broker_address
        self.topics = []
        self.client = mqtt.Client(client_id=str(uuid1()))
        self.client.on_message = on_message
        self.client.on_connect = on_connect
        self.client.on_publish = on_publish
        self.client.on_log = on_log
        # self.client.tls_set()
        self.client.on_subscribe = on_subscribe
        if "api_id" in auth_info:
            self.client.username_pw_set(auth_info['api_id'], auth_info['password'])
        self.client.connect(self.broker_address, port)

    def start_loop(self):
        self.client.loop_start()

    def loop_forever(self, timeout: int = 1):
        self.client.loop_forever(timeout)

    def subscribe_to_topic(self, topic: str):
        self.topics.append(topic)
        result, mid = self.client.subscribe(topic)
        print(f"Subscribe result: ({result}), subscribe mid: ({mid})")
        return result, mid

    def subscribe_to_topics(self, topics: List[str]):
        self.topics += topics
        for topic in topics:
            self.client.subscribe(topic)

    def publish(self, topic: str, message: str):
        message_info = self.client.publish(topic, message)
        print("Message is published: ", message_info.is_published())
        print("Publish result ", message_info.rc)
        print("Message mid: ", message_info.mid)
        message_info.wait_for_publish()
        print("Message is published after waiting ", message_info.is_published())

    def stop_loop(self):
        self.client.loop_stop()

    def disconnect(self):
        self.client.disconnect()
