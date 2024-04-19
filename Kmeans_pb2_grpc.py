# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import Kmeans_pb2 as kmeans__pb2


class KmeansStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.MasterToMapper = channel.unary_unary(
                '/Kmeans/MasterToMapper',
                request_serializer=kmeans__pb2.MasterToMapperReq.SerializeToString,
                response_deserializer=kmeans__pb2.MasterToMapperRes.FromString,
                )
        self.MasterToReducer = channel.unary_unary(
                '/Kmeans/MasterToReducer',
                request_serializer=kmeans__pb2.MasterToReducerReq.SerializeToString,
                response_deserializer=kmeans__pb2.MasterToReducerRes.FromString,
                )
        self.ReducerToMapper = channel.unary_unary(
                '/Kmeans/ReducerToMapper',
                request_serializer=kmeans__pb2.ReducerToMapperReq.SerializeToString,
                response_deserializer=kmeans__pb2.ReducerToMapperRes.FromString,
                )


class KmeansServicer(object):
    """Missing associated documentation comment in .proto file."""

    def MasterToMapper(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MasterToReducer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReducerToMapper(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_KmeansServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'MasterToMapper': grpc.unary_unary_rpc_method_handler(
                    servicer.MasterToMapper,
                    request_deserializer=kmeans__pb2.MasterToMapperReq.FromString,
                    response_serializer=kmeans__pb2.MasterToMapperRes.SerializeToString,
            ),
            'MasterToReducer': grpc.unary_unary_rpc_method_handler(
                    servicer.MasterToReducer,
                    request_deserializer=kmeans__pb2.MasterToReducerReq.FromString,
                    response_serializer=kmeans__pb2.MasterToReducerRes.SerializeToString,
            ),
            'ReducerToMapper': grpc.unary_unary_rpc_method_handler(
                    servicer.ReducerToMapper,
                    request_deserializer=kmeans__pb2.ReducerToMapperReq.FromString,
                    response_serializer=kmeans__pb2.ReducerToMapperRes.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Kmeans', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Kmeans(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def MasterToMapper(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Kmeans/MasterToMapper',
            kmeans__pb2.MasterToMapperReq.SerializeToString,
            kmeans__pb2.MasterToMapperRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MasterToReducer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Kmeans/MasterToReducer',
            kmeans__pb2.MasterToReducerReq.SerializeToString,
            kmeans__pb2.MasterToReducerRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReducerToMapper(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Kmeans/ReducerToMapper',
            kmeans__pb2.ReducerToMapperReq.SerializeToString,
            kmeans__pb2.ReducerToMapperRes.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
