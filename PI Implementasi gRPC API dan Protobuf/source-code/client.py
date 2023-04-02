import grpc
import student_pb2
import student_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = student_pb2_grpc.StudentServiceStub(channel)

def create_student(stub, student):
    request = student_pb2.CreateStudentRequest(student=student)
    response = stub.CreateStudent(request)
    return response.success
    
def read_student(stub, id):
    print(type(id))
    request = student_pb2.ReadStudentRequest(id=str(id))
    response = stub.ReadStudent(request)
    if response.HasField('student'):
        return response.student
    else:
        return None
    

def list_students(stub):
    request = student_pb2.ListStudentRequest()
    response = stub.ListStudent(request)
    return response.students


def update_student(stub, id, name, age):
    request = student_pb2.UpdateStudentRequest(
        id=id,
        name=name,
        age=age
    )
    response = stub.UpdateStudent(request)
    return response.success


def delete_student(stub, id):
    request = student_pb2.DeleteStudentRequest(id=str(id))
    response = stub.DeleteStudent(request)
    return response.success

