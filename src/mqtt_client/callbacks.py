from mqtt_client.utils import encode, decode, endpoints
from messages import load_join_response

from threading import Event

connected = Event()
connected.clear()


def on_message(client, userdata, msg):
    # decode_message = str(decode(message.payload))
    decode_message = msg.payload.decode("utf-8")
    print("message topic=", msg.topic)
    print("message msg=", decode_message)
    
    if msg.topic.endswith("/join"):
        response = load_join_response(decode_message)
    
    # print("message retain flag=", message.retain)
    #
    # api_function = endpoints[message.topic]
    # action, topic, result = api_function(decode_message)
    # print(result)
    # if action:
    #     client.publish(topic, encode(result))


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    print("Connected with flags " + str(flags))

    if rc == 0:
        print("Client connected to the broker")
        connected.set()
        print()
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # client.subscribe("$SYS/#")


# The callback for when the client publish a message from the server
def on_publish(client, userdata, mid):
    print("Published with mid " + str(mid))


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribe with mid " + str(mid))
    print("Subscribe with granted_qos " + str(granted_qos))


def on_log(client, userdata, level, buf):
    print("log: ", buf)