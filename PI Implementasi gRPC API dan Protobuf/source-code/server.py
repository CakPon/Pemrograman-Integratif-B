import grpc
import pymongo
from bson.objectid import ObjectId

import user_pb2
import user_pb2_grpc

import concurrent.futures

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['users']
collection = db['users']

class UserService(user_pb2_grpc.UserServiceServicer):
    def GetUser(self, request, context):
        user_id = ObjectId(request.id)
        user = collection.find_one({'_id': user_id})
        if user:
            return user_pb2.User(
                id=str(user['_id']),
                name=user['name'],
                email=user['email'],
                password=user['password']
            )
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('User not found')
            return user_pb2.User()

    def CreateUser(self, request, context):
        user = request.user
        result = collection.insert_one({
            'name': user.name,
            'email': user.email,
            'password': user.password
        })
        user_id = str(result.inserted_id)
        return user_pb2.User(
            id=user_id,
            name=user.name,
            email=user.email,
            password=user.password
        )

    def UpdateUser(self, request, context):
        user = request.user
        user_id = ObjectId(user.id)
        result = collection.update_one(
            {'_id': user_id},
            {'$set': {
                'name': user.name,
                'email': user.email,
                'password': user.password
            }}
        )
        if result.modified_count > 0:
            return user_pb2.User(
                id=user.id,
                name=user.name,
                email=user.email,
                password=user.password
            )
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('User not found')
            return user_pb2.User()

    def DeleteUser(self, request, context):
        user_id = ObjectId(request.id)
        result = collection.delete_one({'_id': user_id})
        if result.deleted_count > 0:
            return user_pb2.User(id=request.id)
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('User not found')
            return user_pb2.User()

def serve():
    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Server started...')
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
