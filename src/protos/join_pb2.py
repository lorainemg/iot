# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: join.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='join.proto',
  package='iot',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\njoin.proto\x12\x03iot\"\'\n\rApplicationID\x12\x16\n\x0e\x61pplication_id\x18\x01 \x01(\t\"\x82\x01\n\x0b\x45ndDeviceID\x12\x11\n\tdevice_id\x18\x01 \x01(\t\x12+\n\x0f\x61pplication_ids\x18\x02 \x01(\x0b\x32\x12.iot.ApplicationID\x12\x0f\n\x07\x64\x65v_eui\x18\x03 \x01(\t\x12\x10\n\x08join_eui\x18\x04 \x01(\t\x12\x10\n\x08\x64\x65v_addr\x18\x05 \x01(\t\"$\n\nJoinAccept\x12\x16\n\x0esession_key_id\x18\x01 \x01(\t\"w\n\x0cJoinResponse\x12(\n\x0e\x65nd_device_ids\x18\x01 \x01(\x0b\x32\x10.iot.EndDeviceID\x12\x17\n\x0f\x63orrelation_ids\x18\x02 \x03(\t\x12$\n\x0bjoin_accept\x18\x03 \x01(\x0b\x32\x0f.iot.JoinAccept'
)




_APPLICATIONID = _descriptor.Descriptor(
  name='ApplicationID',
  full_name='iot.ApplicationID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='application_id', full_name='iot.ApplicationID.application_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=19,
  serialized_end=58,
)


_ENDDEVICEID = _descriptor.Descriptor(
  name='EndDeviceID',
  full_name='iot.EndDeviceID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_id', full_name='iot.EndDeviceID.device_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='application_ids', full_name='iot.EndDeviceID.application_ids', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dev_eui', full_name='iot.EndDeviceID.dev_eui', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='join_eui', full_name='iot.EndDeviceID.join_eui', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dev_addr', full_name='iot.EndDeviceID.dev_addr', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=191,
)


_JOINACCEPT = _descriptor.Descriptor(
  name='JoinAccept',
  full_name='iot.JoinAccept',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='session_key_id', full_name='iot.JoinAccept.session_key_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=193,
  serialized_end=229,
)


_JOINRESPONSE = _descriptor.Descriptor(
  name='JoinResponse',
  full_name='iot.JoinResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='end_device_ids', full_name='iot.JoinResponse.end_device_ids', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='correlation_ids', full_name='iot.JoinResponse.correlation_ids', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='join_accept', full_name='iot.JoinResponse.join_accept', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=231,
  serialized_end=350,
)

_ENDDEVICEID.fields_by_name['application_ids'].message_type = _APPLICATIONID
_JOINRESPONSE.fields_by_name['end_device_ids'].message_type = _ENDDEVICEID
_JOINRESPONSE.fields_by_name['join_accept'].message_type = _JOINACCEPT
DESCRIPTOR.message_types_by_name['ApplicationID'] = _APPLICATIONID
DESCRIPTOR.message_types_by_name['EndDeviceID'] = _ENDDEVICEID
DESCRIPTOR.message_types_by_name['JoinAccept'] = _JOINACCEPT
DESCRIPTOR.message_types_by_name['JoinResponse'] = _JOINRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ApplicationID = _reflection.GeneratedProtocolMessageType('ApplicationID', (_message.Message,), {
  'DESCRIPTOR' : _APPLICATIONID,
  '__module__' : 'join_pb2'
  # @@protoc_insertion_point(class_scope:iot.ApplicationID)
  })
_sym_db.RegisterMessage(ApplicationID)

EndDeviceID = _reflection.GeneratedProtocolMessageType('EndDeviceID', (_message.Message,), {
  'DESCRIPTOR' : _ENDDEVICEID,
  '__module__' : 'join_pb2'
  # @@protoc_insertion_point(class_scope:iot.EndDeviceID)
  })
_sym_db.RegisterMessage(EndDeviceID)

JoinAccept = _reflection.GeneratedProtocolMessageType('JoinAccept', (_message.Message,), {
  'DESCRIPTOR' : _JOINACCEPT,
  '__module__' : 'join_pb2'
  # @@protoc_insertion_point(class_scope:iot.JoinAccept)
  })
_sym_db.RegisterMessage(JoinAccept)

JoinResponse = _reflection.GeneratedProtocolMessageType('JoinResponse', (_message.Message,), {
  'DESCRIPTOR' : _JOINRESPONSE,
  '__module__' : 'join_pb2'
  # @@protoc_insertion_point(class_scope:iot.JoinResponse)
  })
_sym_db.RegisterMessage(JoinResponse)


# @@protoc_insertion_point(module_scope)
