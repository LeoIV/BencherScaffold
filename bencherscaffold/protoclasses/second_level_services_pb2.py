# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bencherscaffold/protos/second_level_services.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bencherscaffold.protoclasses import bencher_pb2 as bencherscaffold_dot_protos_dot_bencher__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2bencherscaffold/protos/second_level_services.proto\x1a$bencherscaffold/protos/bencher.proto2N\n\x12SecondLevelBencher\x12\x38\n\x0e\x65valuate_point\x12\x11.BenchmarkRequest\x1a\x11.EvaluationResult\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bencherscaffold.protos.second_level_services_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_SECONDLEVELBENCHER']._serialized_start=92
  _globals['_SECONDLEVELBENCHER']._serialized_end=170
# @@protoc_insertion_point(module_scope)
