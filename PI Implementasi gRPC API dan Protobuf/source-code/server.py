import grpc
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from concurrent import futures
import student_pb2
import student_pb2_grpc
import time

class StudentService(student_pb2_grpc.StudentServiceServicer):
    def CreateStudent(self, request, context):
        db = firestore.client()
        student = request.student
        doc_ref = db.collection('students').document(str(student.id))
        doc_ref.set({
            'id':student.id,
            'name': student.name,
            'age': student.age
        })
        return student_pb2.CreateStudentResponse(success=True)

    def ReadStudent(self, request, context):
        db = firestore.client()
        doc_ref = db.collection('students').document(str(request.id))
        doc = doc_ref.get()

        if doc.exists:
            data = doc.to_dict()
            student = student_pb2.Student(
                id=doc.id,
                name=data['name'],
                age=data['age']
            )
            return student_pb2.ReadStudentResponse(student=student)
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Student not found')
            return student_pb2.ReadStudentResponse()
        
    def ListStudent(self, request, context):
        db = firestore.client()
        docs = db.collection('students').stream()
        students = []
        for doc in docs:
            data = doc.to_dict()
            student = student_pb2.Student(
                id=doc.id,
                name=data['name'],
                age=data['age']
            )
            students.append(student)
        return student_pb2.ListStudentResponse(students=students)


    def UpdateStudent(self, request, context):
        db = firestore.client()
        doc_ref = db.collection('students').document(str(request.id))
        try:
            doc_ref.update({
                'id': request.id,
                'name': request.name,
                'age': request.age
            })
            return student_pb2.UpdateStudentResponse(success=True)
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(str(e))
            return student_pb2.UpdateStudentResponse(success=False)
        
    def DeleteStudent(self, request, context):
        db = firestore.client()
        doc_ref = db.collection('students').document(str(request.id))
        doc = doc_ref.get()

        if doc.exists:
            doc_ref.delete()
            return student_pb2.DeleteStudentResponse(success=True)
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Student not found')
            return student_pb2.DeleteStudentResponse(success=False)


    
    

def serve():
    key = {
  "type": "service_account",
  "project_id": "students-47e7e",
  "private_key_id": "e50e9561dba1d546e3aa6f0b7242c54eb98978fa",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCxe4U4oz02fOGo\nbKqnqmHoNBcppN3C/N/8nhmXpgCXE00vkQe26UFtbzzcVeNVxTOVxY3AaHL252+b\nZi1CvKcQK9jbInciqPvEjiNh+I/5Ec/kVZG1d3PLwuvtRaPM35a6el44stA/K4/x\n61uhIZy3qM2FrSxuL+rtLj2VOR9bQEblb9/pM3df/2a6Wuk3zW/tYaTT6YbyYZkh\nNw5L97+oWyZ6tLfOmJnfM/GOVj4EcWzuS7fVw1IdhrDp98VDFXhVLZWTpyJL8ji0\njGlJuRhIBIzXRdd6xd9h0WS+yFSmj9EagRiFmOe0RGY8xvUh1boud2aAhUlANAhZ\n/eLte7DjAgMBAAECggEADMcDPszFwJFPX6Q/HvtYZB1dQ4gVLQ9ZLXh7stwRHnnr\nFyRo+pqitWG07ySXIsV5OBb1DxKV9ZTmMeOybiO4dU9qznqV5XQRTW5xjqvp6uOv\nj1U3vGmWomdB5p7vssqwBnR+fwokjZUHHm1ezI69F8h6eggPHaRWf0Unytabcs1i\n17ZtTbSE+nazJKMuEbu0rBgiVTxzduRxub6XNdI26ISq5P1aM8E7m62Ul0FXgG83\nAoead8NGZh+qLbwBGa3QoD8INYSTjoxCt9lUZZ7Yip/3ZqekXFaSYuab0/HVB1PX\nDrmwXrGPB+7UyyDqkrlfUa29XxEg0g3OOeLBkxiDNQKBgQDqtJRqdm+RxUAlVae2\nTDq7uegzIacG03KKWhOIHrzB6iBs7LyJAybHRN2w97lPKOOENpeNQzKLXc6CRHUj\nHPyEARDjt190UwFtG/jLTr+/rKRvvZVsMokdTm7SUGSRP5bcdsPqVOVmUkWkXDDm\n7v/mliTxtg8hjqmvUIjyn4rfZwKBgQDBldg2IXNZdL9eAWFwPKNiat1WdOVvvkla\n9ue3PXUwXNA9DNt6j4mx2o8+wvIdIAHxjrboDxyJgXj9sV+30vpvhNPYpwl8hKpx\npdTG8GhXRSiR3eczeoCYlB9QvVFhVKPpcNTOBg7YoXUw6QC+W9uHxnTjtJhvMjdh\nb8VcW+YBJQKBgEQ/iFzA3caElheFJcSTvAx0jbm4kmoguFDUypMtZPP6Ub16xYQN\n34vYUaKxFjiXijka6szP+nWeLHuiznEMb70u1itxWhdoP6Trmlf8KTPiTtqTRUz2\nEPrtoLoVWHkIBaVL/8I3N5GeYNPfXvT4EH+Lr2h96T53zo3FHF142RgHAoGBALtI\n6QCVpC8rj+i2lTossDULBlAaj85n3jgvH0ZcIwBDCwPFaKFONPzoYiVqHSqoSLkW\nRUaFOCqgJBnsfJovdzJk4z97euYIw41nzk8ZTxj/Q5y7fm6DWd5Dj3hhcFYluN6j\n1n3rxnk221YSVjHUVLMrAPM7SS5q+sE9jUcpcYAxAoGAc5GymrVxpePu0S1dqw1y\nzEBodWC6uKOtSW+CEOy0djHffcstEyYgdruVgOzBDEZ3GG2oaSB4DDugY6D4dA0Z\nzp+TRlxBABnpWkc6ZrcK0BCrzFizrl7fbWHrpdjrBtldG1+I6DeEC/UEbdSwNA++\neVE/VXcpc9ykZ2rxuylUYUs=\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-4zty3@students-47e7e.iam.gserviceaccount.com",
  "client_id": "105062832901227921932",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-4zty3%40students-47e7e.iam.gserviceaccount.com"
}

# Initialize Firebase SDK
    cred = credentials.Certificate(key)
    firebase_admin.initialize_app(cred)
    
    # Create gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    # Add servicer to server
    student_pb2_grpc.add_StudentServiceServicer_to_server(StudentService(), server)
    
    # Start the server
    server.add_insecure_port('[::]:50051')
    server.start()
    
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
