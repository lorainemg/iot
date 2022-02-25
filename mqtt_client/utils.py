def encode(message: str) -> bytes:
    return bytes(message.encode(encoding='utf-8'))


def decode(message: bytes) -> str:
    return str(message.decode(encoding='utf-8'))


AUTH_INFO = {'api_id':"{application id}@{tenant id}", 'password':"NNSXS.VEEBURF3KR77ZR.."}


def function():
    pass


endpoints = {'topic_name': function}

