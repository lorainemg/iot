from pathlib import Path
from google.protobuf.json_format import Parse

def encode(message: str) -> bytes:
    return bytes(message.encode(encoding='utf-8'))


def decode(message: bytes) -> str:
    return str(message.decode(encoding='utf-8'))


AUTH_INFO = {'api_id':"{application id}@{tenant id}", 'password':"NNSXS.VEEBURF3KR77ZR.."}


def function():
    pass


def get_message(filename: Path, proto_obj):
    with open(filename) as f:
        Parse(f.read(), proto_obj)


endpoints = {'topic_name': function}

