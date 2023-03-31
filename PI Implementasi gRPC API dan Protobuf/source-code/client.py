import grpc
import user_pb2
import user_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = user_pb2_grpc.UserServiceStub(channel)

def get_user(user_id):
    request = user_pb2.GetUserRequest(id=user_id)
    response = stub.GetUser(request)
    if response.id:
        print(f'User ID: {response.id}')
        print(f'Name: {response.name}')
        print(f'Email: {response.email}')
        print(f'Password: {response.password}')
    else:
        print('User not found')

def create_user(name, email, password):
    user = user_pb2.User(name=name, email=email, password=password)
    request = user_pb2.CreateUserRequest(user=user)
    response = stub.CreateUser(request)
    print(f'User created with ID: {response.id}')

def update_user(user_id, name=None, email=None, password=None):
    user = user_pb2.User(id=user_id, name=name, email=email, password=password)
    request = user_pb2.UpdateUserRequest(user=user)
    response = stub.UpdateUser(request)
    if response.id:
        print(f'User ID: {response.id}')
        print(f'Name: {response.name}')
        print(f'Email: {response.email}')
        print(f'Password: {response.password}')
    else:
        print('User not found')

def delete_user(user_id):
    request = user_pb2.DeleteUserRequest(id=user_id)
    response = stub.DeleteUser(request)
    if response.id:
        print(f'User ID: {response.id} deleted')
    else:
        print('User not found')

if __name__ == '__main__':
    get_user('616496d38a695b97d4c8e4e4')
    create_user('John Doe', 'john.doe@example.com', 'password')
    update_user('616496d38a695b97d4c8e4e4', name='Jane Doe')
    delete_user('616496d38a695b97d4c8e4e4')
