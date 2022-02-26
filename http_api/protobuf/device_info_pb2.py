# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: device_info.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='device_info.proto',
  package='iot',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11\x64\x65vice_info.proto\x12\x03iot\".\n\tEndDevice\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\"\x1a\n\tFieldMask\x12\r\n\x05paths\x18\x01 \x03(\t\"W\n\rSetDeviceInfo\x12\"\n\nend_device\x18\x01 \x01(\x0b\x32\x0e.iot.EndDevice\x12\"\n\nfield_mask\x18\x02 \x01(\x0b\x32\x0e.iot.FieldMask'
)




_ENDDEVICE = _descriptor.Descriptor(
  name='EndDevice',
  full_name='iot.EndDevice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='iot.EndDevice.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='iot.EndDevice.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=26,
  serialized_end=72,
)


_FIELDMASK = _descriptor.Descriptor(
  name='FieldMask',
  full_name='iot.FieldMask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='paths', full_name='iot.FieldMask.paths', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=74,
  serialized_end=100,
)


_SETDEVICEINFO = _descriptor.Descriptor(
  name='SetDeviceInfo',
  full_name='iot.SetDeviceInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='end_device', full_name='iot.SetDeviceInfo.end_device', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='field_mask', full_name='iot.SetDeviceInfo.field_mask', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=102,
  serialized_end=189,
)

_SETDEVICEINFO.fields_by_name['end_device'].message_type = _ENDDEVICE
_SETDEVICEINFO.fields_by_name['field_mask'].message_type = _FIELDMASK
DESCRIPTOR.message_types_by_name['EndDevice'] = _ENDDEVICE
DESCRIPTOR.message_types_by_name['FieldMask'] = _FIELDMASK
DESCRIPTOR.message_types_by_name['SetDeviceInfo'] = _SETDEVICEINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EndDevice = _reflection.GeneratedProtocolMessageType('EndDevice', (_message.Message,), {
  'DESCRIPTOR' : _ENDDEVICE,
  '__module__' : 'device_info_pb2'
  # @@protoc_insertion_point(class_scope:iot.EndDevice)
  })
_sym_db.RegisterMessage(EndDevice)

FieldMask = _reflection.GeneratedProtocolMessageType('FieldMask', (_message.Message,), {
  'DESCRIPTOR' : _FIELDMASK,
  '__module__' : 'device_info_pb2'
  # @@protoc_insertion_point(class_scope:iot.FieldMask)
  })
_sym_db.RegisterMessage(FieldMask)

SetDeviceInfo = _reflection.GeneratedProtocolMessageType('SetDeviceInfo', (_message.Message,), {
  'DESCRIPTOR' : _SETDEVICEINFO,
  '__module__' : 'device_info_pb2'
  # @@protoc_insertion_point(class_scope:iot.SetDeviceInfo)
  })
_sym_db.RegisterMessage(SetDeviceInfo)


# @@protoc_insertion_point(module_scope)