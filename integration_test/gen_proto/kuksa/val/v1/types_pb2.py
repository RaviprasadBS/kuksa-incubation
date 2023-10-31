# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: kuksa/val/v1/types.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18kuksa/val/v1/types.proto\x12\x0ckuksa.val.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\x9d\x01\n\tDataEntry\x12\x0c\n\x04path\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.kuksa.val.v1.Datapoint\x12\x30\n\x0f\x61\x63tuator_target\x18\x03 \x01(\x0b\x32\x17.kuksa.val.v1.Datapoint\x12(\n\x08metadata\x18\n \x01(\x0b\x32\x16.kuksa.val.v1.Metadata\"\xdc\x04\n\tDatapoint\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x10\n\x06string\x18\x0b \x01(\tH\x00\x12\x0e\n\x04\x62ool\x18\x0c \x01(\x08H\x00\x12\x0f\n\x05int32\x18\r \x01(\x11H\x00\x12\x0f\n\x05int64\x18\x0e \x01(\x12H\x00\x12\x10\n\x06uint32\x18\x0f \x01(\rH\x00\x12\x10\n\x06uint64\x18\x10 \x01(\x04H\x00\x12\x0f\n\x05\x66loat\x18\x11 \x01(\x02H\x00\x12\x10\n\x06\x64ouble\x18\x12 \x01(\x01H\x00\x12\x31\n\x0cstring_array\x18\x15 \x01(\x0b\x32\x19.kuksa.val.v1.StringArrayH\x00\x12-\n\nbool_array\x18\x16 \x01(\x0b\x32\x17.kuksa.val.v1.BoolArrayH\x00\x12/\n\x0bint32_array\x18\x17 \x01(\x0b\x32\x18.kuksa.val.v1.Int32ArrayH\x00\x12/\n\x0bint64_array\x18\x18 \x01(\x0b\x32\x18.kuksa.val.v1.Int64ArrayH\x00\x12\x31\n\x0cuint32_array\x18\x19 \x01(\x0b\x32\x19.kuksa.val.v1.Uint32ArrayH\x00\x12\x31\n\x0cuint64_array\x18\x1a \x01(\x0b\x32\x19.kuksa.val.v1.Uint64ArrayH\x00\x12/\n\x0b\x66loat_array\x18\x1b \x01(\x0b\x32\x18.kuksa.val.v1.FloatArrayH\x00\x12\x31\n\x0c\x64ouble_array\x18\x1c \x01(\x0b\x32\x19.kuksa.val.v1.DoubleArrayH\x00\x42\x07\n\x05value\"\xc3\x03\n\x08Metadata\x12)\n\tdata_type\x18\x0b \x01(\x0e\x32\x16.kuksa.val.v1.DataType\x12+\n\nentry_type\x18\x0c \x01(\x0e\x32\x17.kuksa.val.v1.EntryType\x12\x18\n\x0b\x64\x65scription\x18\r \x01(\tH\x01\x88\x01\x01\x12\x14\n\x07\x63omment\x18\x0e \x01(\tH\x02\x88\x01\x01\x12\x18\n\x0b\x64\x65precation\x18\x0f \x01(\tH\x03\x88\x01\x01\x12\x11\n\x04unit\x18\x10 \x01(\tH\x04\x88\x01\x01\x12\x39\n\x11value_restriction\x18\x11 \x01(\x0b\x32\x1e.kuksa.val.v1.ValueRestriction\x12*\n\x08\x61\x63tuator\x18\x14 \x01(\x0b\x32\x16.kuksa.val.v1.ActuatorH\x00\x12&\n\x06sensor\x18\x1e \x01(\x0b\x32\x14.kuksa.val.v1.SensorH\x00\x12,\n\tattribute\x18( \x01(\x0b\x32\x17.kuksa.val.v1.AttributeH\x00\x42\x10\n\x0e\x65ntry_specificB\x0e\n\x0c_descriptionB\n\n\x08_commentB\x0e\n\x0c_deprecationB\x07\n\x05_unit\"\n\n\x08\x41\x63tuator\"\x08\n\x06Sensor\"\x0b\n\tAttribute\"\xfe\x01\n\x10ValueRestriction\x12\x36\n\x06string\x18\x15 \x01(\x0b\x32$.kuksa.val.v1.ValueRestrictionStringH\x00\x12\x33\n\x06signed\x18\x16 \x01(\x0b\x32!.kuksa.val.v1.ValueRestrictionIntH\x00\x12\x36\n\x08unsigned\x18\x17 \x01(\x0b\x32\".kuksa.val.v1.ValueRestrictionUintH\x00\x12=\n\x0e\x66loating_point\x18\x18 \x01(\x0b\x32#.kuksa.val.v1.ValueRestrictionFloatH\x00\x42\x06\n\x04type\"a\n\x13ValueRestrictionInt\x12\x10\n\x03min\x18\x01 \x01(\x12H\x00\x88\x01\x01\x12\x10\n\x03max\x18\x02 \x01(\x12H\x01\x88\x01\x01\x12\x16\n\x0e\x61llowed_values\x18\x03 \x03(\x12\x42\x06\n\x04_minB\x06\n\x04_max\"b\n\x14ValueRestrictionUint\x12\x10\n\x03min\x18\x01 \x01(\x04H\x00\x88\x01\x01\x12\x10\n\x03max\x18\x02 \x01(\x04H\x01\x88\x01\x01\x12\x16\n\x0e\x61llowed_values\x18\x03 \x03(\x04\x42\x06\n\x04_minB\x06\n\x04_max\"c\n\x15ValueRestrictionFloat\x12\x10\n\x03min\x18\x01 \x01(\x01H\x00\x88\x01\x01\x12\x10\n\x03max\x18\x02 \x01(\x01H\x01\x88\x01\x01\x12\x16\n\x0e\x61llowed_values\x18\x03 \x03(\x01\x42\x06\n\x04_minB\x06\n\x04_max\"0\n\x16ValueRestrictionString\x12\x16\n\x0e\x61llowed_values\x18\x03 \x03(\t\"6\n\x05\x45rror\x12\x0c\n\x04\x63ode\x18\x01 \x01(\r\x12\x0e\n\x06reason\x18\x02 \x01(\t\x12\x0f\n\x07message\x18\x03 \x01(\t\"B\n\x0e\x44\x61taEntryError\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\"\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x13.kuksa.val.v1.Error\"\x1d\n\x0bStringArray\x12\x0e\n\x06values\x18\x01 \x03(\t\"\x1b\n\tBoolArray\x12\x0e\n\x06values\x18\x01 \x03(\x08\"\x1c\n\nInt32Array\x12\x0e\n\x06values\x18\x01 \x03(\x11\"\x1c\n\nInt64Array\x12\x0e\n\x06values\x18\x01 \x03(\x12\"\x1d\n\x0bUint32Array\x12\x0e\n\x06values\x18\x01 \x03(\r\"\x1d\n\x0bUint64Array\x12\x0e\n\x06values\x18\x01 \x03(\x04\"\x1c\n\nFloatArray\x12\x0e\n\x06values\x18\x01 \x03(\x02\"\x1d\n\x0b\x44oubleArray\x12\x0e\n\x06values\x18\x01 \x03(\x01*\xa9\x05\n\x08\x44\x61taType\x12\x19\n\x15\x44\x41TA_TYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10\x44\x41TA_TYPE_STRING\x10\x01\x12\x15\n\x11\x44\x41TA_TYPE_BOOLEAN\x10\x02\x12\x12\n\x0e\x44\x41TA_TYPE_INT8\x10\x03\x12\x13\n\x0f\x44\x41TA_TYPE_INT16\x10\x04\x12\x13\n\x0f\x44\x41TA_TYPE_INT32\x10\x05\x12\x13\n\x0f\x44\x41TA_TYPE_INT64\x10\x06\x12\x13\n\x0f\x44\x41TA_TYPE_UINT8\x10\x07\x12\x14\n\x10\x44\x41TA_TYPE_UINT16\x10\x08\x12\x14\n\x10\x44\x41TA_TYPE_UINT32\x10\t\x12\x14\n\x10\x44\x41TA_TYPE_UINT64\x10\n\x12\x13\n\x0f\x44\x41TA_TYPE_FLOAT\x10\x0b\x12\x14\n\x10\x44\x41TA_TYPE_DOUBLE\x10\x0c\x12\x17\n\x13\x44\x41TA_TYPE_TIMESTAMP\x10\r\x12\x1a\n\x16\x44\x41TA_TYPE_STRING_ARRAY\x10\x14\x12\x1b\n\x17\x44\x41TA_TYPE_BOOLEAN_ARRAY\x10\x15\x12\x18\n\x14\x44\x41TA_TYPE_INT8_ARRAY\x10\x16\x12\x19\n\x15\x44\x41TA_TYPE_INT16_ARRAY\x10\x17\x12\x19\n\x15\x44\x41TA_TYPE_INT32_ARRAY\x10\x18\x12\x19\n\x15\x44\x41TA_TYPE_INT64_ARRAY\x10\x19\x12\x19\n\x15\x44\x41TA_TYPE_UINT8_ARRAY\x10\x1a\x12\x1a\n\x16\x44\x41TA_TYPE_UINT16_ARRAY\x10\x1b\x12\x1a\n\x16\x44\x41TA_TYPE_UINT32_ARRAY\x10\x1c\x12\x1a\n\x16\x44\x41TA_TYPE_UINT64_ARRAY\x10\x1d\x12\x19\n\x15\x44\x41TA_TYPE_FLOAT_ARRAY\x10\x1e\x12\x1a\n\x16\x44\x41TA_TYPE_DOUBLE_ARRAY\x10\x1f\x12\x1d\n\x19\x44\x41TA_TYPE_TIMESTAMP_ARRAY\x10 *q\n\tEntryType\x12\x1a\n\x16\x45NTRY_TYPE_UNSPECIFIED\x10\x00\x12\x18\n\x14\x45NTRY_TYPE_ATTRIBUTE\x10\x01\x12\x15\n\x11\x45NTRY_TYPE_SENSOR\x10\x02\x12\x17\n\x13\x45NTRY_TYPE_ACTUATOR\x10\x03*}\n\x04View\x12\x14\n\x10VIEW_UNSPECIFIED\x10\x00\x12\x16\n\x12VIEW_CURRENT_VALUE\x10\x01\x12\x15\n\x11VIEW_TARGET_VALUE\x10\x02\x12\x11\n\rVIEW_METADATA\x10\x03\x12\x0f\n\x0bVIEW_FIELDS\x10\n\x12\x0c\n\x08VIEW_ALL\x10\x14*\x9c\x03\n\x05\x46ield\x12\x15\n\x11\x46IELD_UNSPECIFIED\x10\x00\x12\x0e\n\nFIELD_PATH\x10\x01\x12\x0f\n\x0b\x46IELD_VALUE\x10\x02\x12\x19\n\x15\x46IELD_ACTUATOR_TARGET\x10\x03\x12\x12\n\x0e\x46IELD_METADATA\x10\n\x12\x1c\n\x18\x46IELD_METADATA_DATA_TYPE\x10\x0b\x12\x1e\n\x1a\x46IELD_METADATA_DESCRIPTION\x10\x0c\x12\x1d\n\x19\x46IELD_METADATA_ENTRY_TYPE\x10\r\x12\x1a\n\x16\x46IELD_METADATA_COMMENT\x10\x0e\x12\x1e\n\x1a\x46IELD_METADATA_DEPRECATION\x10\x0f\x12\x17\n\x13\x46IELD_METADATA_UNIT\x10\x10\x12$\n FIELD_METADATA_VALUE_RESTRICTION\x10\x11\x12\x1b\n\x17\x46IELD_METADATA_ACTUATOR\x10\x14\x12\x19\n\x15\x46IELD_METADATA_SENSOR\x10\x1e\x12\x1c\n\x18\x46IELD_METADATA_ATTRIBUTE\x10(B\x0eZ\x0ckuksa/val/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'kuksa.val.v1.types_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\014kuksa/val/v1'
  _globals['_DATATYPE']._serialized_start=2306
  _globals['_DATATYPE']._serialized_end=2987
  _globals['_ENTRYTYPE']._serialized_start=2989
  _globals['_ENTRYTYPE']._serialized_end=3102
  _globals['_VIEW']._serialized_start=3104
  _globals['_VIEW']._serialized_end=3229
  _globals['_FIELD']._serialized_start=3232
  _globals['_FIELD']._serialized_end=3644
  _globals['_DATAENTRY']._serialized_start=76
  _globals['_DATAENTRY']._serialized_end=233
  _globals['_DATAPOINT']._serialized_start=236
  _globals['_DATAPOINT']._serialized_end=840
  _globals['_METADATA']._serialized_start=843
  _globals['_METADATA']._serialized_end=1294
  _globals['_ACTUATOR']._serialized_start=1296
  _globals['_ACTUATOR']._serialized_end=1306
  _globals['_SENSOR']._serialized_start=1308
  _globals['_SENSOR']._serialized_end=1316
  _globals['_ATTRIBUTE']._serialized_start=1318
  _globals['_ATTRIBUTE']._serialized_end=1329
  _globals['_VALUERESTRICTION']._serialized_start=1332
  _globals['_VALUERESTRICTION']._serialized_end=1586
  _globals['_VALUERESTRICTIONINT']._serialized_start=1588
  _globals['_VALUERESTRICTIONINT']._serialized_end=1685
  _globals['_VALUERESTRICTIONUINT']._serialized_start=1687
  _globals['_VALUERESTRICTIONUINT']._serialized_end=1785
  _globals['_VALUERESTRICTIONFLOAT']._serialized_start=1787
  _globals['_VALUERESTRICTIONFLOAT']._serialized_end=1886
  _globals['_VALUERESTRICTIONSTRING']._serialized_start=1888
  _globals['_VALUERESTRICTIONSTRING']._serialized_end=1936
  _globals['_ERROR']._serialized_start=1938
  _globals['_ERROR']._serialized_end=1992
  _globals['_DATAENTRYERROR']._serialized_start=1994
  _globals['_DATAENTRYERROR']._serialized_end=2060
  _globals['_STRINGARRAY']._serialized_start=2062
  _globals['_STRINGARRAY']._serialized_end=2091
  _globals['_BOOLARRAY']._serialized_start=2093
  _globals['_BOOLARRAY']._serialized_end=2120
  _globals['_INT32ARRAY']._serialized_start=2122
  _globals['_INT32ARRAY']._serialized_end=2150
  _globals['_INT64ARRAY']._serialized_start=2152
  _globals['_INT64ARRAY']._serialized_end=2180
  _globals['_UINT32ARRAY']._serialized_start=2182
  _globals['_UINT32ARRAY']._serialized_end=2211
  _globals['_UINT64ARRAY']._serialized_start=2213
  _globals['_UINT64ARRAY']._serialized_end=2242
  _globals['_FLOATARRAY']._serialized_start=2244
  _globals['_FLOATARRAY']._serialized_end=2272
  _globals['_DOUBLEARRAY']._serialized_start=2274
  _globals['_DOUBLEARRAY']._serialized_end=2303
# @@protoc_insertion_point(module_scope)
