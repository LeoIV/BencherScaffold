# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from bencher.protos import bencher_pb2 as bencher__pb2


class BencherStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.EvaluatePoint = channel.unary_unary(
                '/Bencher/EvaluatePoint',
                request_serializer=bencher__pb2.BenchmarkRequest.SerializeToString,
                response_deserializer=bencher__pb2.EvaluationResult.FromString,
                )


class BencherServicer(object):
    """Missing associated documentation comment in .proto file."""

    def EvaluatePoint(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BencherServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'EvaluatePoint': grpc.unary_unary_rpc_method_handler(
                    servicer.EvaluatePoint,
                    request_deserializer=bencher__pb2.BenchmarkRequest.FromString,
                    response_serializer=bencher__pb2.EvaluationResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Bencher', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Bencher(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def EvaluatePoint(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Bencher/EvaluatePoint',
            bencher__pb2.BenchmarkRequest.SerializeToString,
            bencher__pb2.EvaluationResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
