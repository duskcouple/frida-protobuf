# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pyproto/tbclient.Error.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pyproto/tbclient.Error.proto',
  package='tbclient',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1cpyproto/tbclient.Error.proto\x12\x08tbclient\"k\n\x05\x45rror\x12\x14\n\x07\x65rrorno\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x13\n\x06\x65rrmsg\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x14\n\x07usermsg\x18\x03 \x01(\tH\x02\x88\x01\x01\x42\n\n\x08_errornoB\t\n\x07_errmsgB\n\n\x08_usermsgb\x06proto3'
)




_ERROR = _descriptor.Descriptor(
  name='Error',
  full_name='tbclient.Error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='errorno', full_name='tbclient.Error.errorno', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='errmsg', full_name='tbclient.Error.errmsg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='usermsg', full_name='tbclient.Error.usermsg', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_errorno', full_name='tbclient.Error._errorno',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_errmsg', full_name='tbclient.Error._errmsg',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_usermsg', full_name='tbclient.Error._usermsg',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=42,
  serialized_end=149,
)

_ERROR.oneofs_by_name['_errorno'].fields.append(
  _ERROR.fields_by_name['errorno'])
_ERROR.fields_by_name['errorno'].containing_oneof = _ERROR.oneofs_by_name['_errorno']
_ERROR.oneofs_by_name['_errmsg'].fields.append(
  _ERROR.fields_by_name['errmsg'])
_ERROR.fields_by_name['errmsg'].containing_oneof = _ERROR.oneofs_by_name['_errmsg']
_ERROR.oneofs_by_name['_usermsg'].fields.append(
  _ERROR.fields_by_name['usermsg'])
_ERROR.fields_by_name['usermsg'].containing_oneof = _ERROR.oneofs_by_name['_usermsg']
DESCRIPTOR.message_types_by_name['Error'] = _ERROR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Error = _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), {
  'DESCRIPTOR' : _ERROR,
  '__module__' : 'pyproto.tbclient.Error_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.Error)
  })
_sym_db.RegisterMessage(Error)


# @@protoc_insertion_point(module_scope)