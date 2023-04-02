# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import student_pb2 as student__pb2


class StudentServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateStudent = channel.unary_unary(
                '/student.StudentService/CreateStudent',
                request_serializer=student__pb2.CreateStudentRequest.SerializeToString,
                response_deserializer=student__pb2.CreateStudentResponse.FromString,
                )
        self.ReadStudent = channel.unary_unary(
                '/student.StudentService/ReadStudent',
                request_serializer=student__pb2.ReadStudentRequest.SerializeToString,
                response_deserializer=student__pb2.ReadStudentResponse.FromString,
                )
        self.UpdateStudent = channel.unary_unary(
                '/student.StudentService/UpdateStudent',
                request_serializer=student__pb2.UpdateStudentRequest.SerializeToString,
                response_deserializer=student__pb2.UpdateStudentResponse.FromString,
                )
        self.DeleteStudent = channel.unary_unary(
                '/student.StudentService/DeleteStudent',
                request_serializer=student__pb2.DeleteStudentRequest.SerializeToString,
                response_deserializer=student__pb2.DeleteStudentResponse.FromString,
                )
        self.ListStudent = channel.unary_unary(
                '/student.StudentService/ListStudent',
                request_serializer=student__pb2.ListStudentRequest.SerializeToString,
                response_deserializer=student__pb2.ListStudentResponse.FromString,
                )


class StudentServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateStudent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadStudent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateStudent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteStudent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListStudent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StudentServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateStudent': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateStudent,
                    request_deserializer=student__pb2.CreateStudentRequest.FromString,
                    response_serializer=student__pb2.CreateStudentResponse.SerializeToString,
            ),
            'ReadStudent': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadStudent,
                    request_deserializer=student__pb2.ReadStudentRequest.FromString,
                    response_serializer=student__pb2.ReadStudentResponse.SerializeToString,
            ),
            'UpdateStudent': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateStudent,
                    request_deserializer=student__pb2.UpdateStudentRequest.FromString,
                    response_serializer=student__pb2.UpdateStudentResponse.SerializeToString,
            ),
            'DeleteStudent': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteStudent,
                    request_deserializer=student__pb2.DeleteStudentRequest.FromString,
                    response_serializer=student__pb2.DeleteStudentResponse.SerializeToString,
            ),
            'ListStudent': grpc.unary_unary_rpc_method_handler(
                    servicer.ListStudent,
                    request_deserializer=student__pb2.ListStudentRequest.FromString,
                    response_serializer=student__pb2.ListStudentResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'student.StudentService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StudentService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateStudent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/student.StudentService/CreateStudent',
            student__pb2.CreateStudentRequest.SerializeToString,
            student__pb2.CreateStudentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadStudent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/student.StudentService/ReadStudent',
            student__pb2.ReadStudentRequest.SerializeToString,
            student__pb2.ReadStudentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateStudent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/student.StudentService/UpdateStudent',
            student__pb2.UpdateStudentRequest.SerializeToString,
            student__pb2.UpdateStudentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteStudent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/student.StudentService/DeleteStudent',
            student__pb2.DeleteStudentRequest.SerializeToString,
            student__pb2.DeleteStudentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListStudent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/student.StudentService/ListStudent',
            student__pb2.ListStudentRequest.SerializeToString,
            student__pb2.ListStudentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
