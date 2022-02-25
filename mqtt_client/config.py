# (API KEY)
PASSWORD = "NNSXS.KF3D5FRVHK7JIZTAGXAYC6AH37W265IG2DPFGQI.FEMR2GH6QG5P7VJ3ILW7Z2UQMGQAB5JTBAOM5L7TWQ4KEAUNFMJA"
APP_ID = "iltellilight-app"
# BROKER_ADDRESS = "eu1.cloud.thethings.network"
BROKER_ADDRESS = "test.mosquitto.org"
# PORT = 1883
PORT = 1883
DEVICE_ID = "eui-70b3d57ed004cb5f"


def configure_mqtt_client():
    from mqtt_client import MQTTClient

    # auth_info = {"api_id": APP_ID, "password": PASSWORD}
    auth_info = {}
    return MQTTClient(BROKER_ADDRESS, PORT, auth_info)
