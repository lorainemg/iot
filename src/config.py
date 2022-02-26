# (API KEY)
PASSWORD = "NNSXS.KF3D5FRVHK7JIZTAGXAYC6AH37W265IG2DPFGQI.FEMR2GH6QG5P7VJ3ILW7Z2UQMGQAB5JTBAOM5L7TWQ4KEAUNFMJA"
HTTP_API_KEY = "NNSXS.6QO42TLSQE2KWW6H24FG4I3ZS6CPMHE4YBI2KXA.FBRMBDG6RLJFCZVWD3GYUZWJN3YTOXFTQE4YVMCS5ILT46WXRIJA"

DEVICE_ID = "eui-70b3d57ed004cb5f"
APP_ID = "iltellilight-app"

# BROKER_ADDRESS = "eu1.cloud.thethings.network"
BROKER_ADDRESS = "test.mosquitto.org"
# PORT = 1883
PORT = 1883


def configure_mqtt_client():
    from mqtt_client.client import MQTTClient

    # auth_info = {"api_id": APP_ID, "password": PASSWORD}
    auth_info = {}
    return MQTTClient(BROKER_ADDRESS, PORT, auth_info)
