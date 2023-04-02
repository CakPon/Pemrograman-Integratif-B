from flask import Flask, render_template, request, redirect
import client
import grpc
import student_pb2
import student_pb2_grpc

app = Flask(__name__, template_folder='templates')


@app.route('/')
def list_students():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = student_pb2_grpc.StudentServiceStub(channel)
        students = client.list_students(stub)
        return render_template('index.html', students=students)

@app.route('/<id>')
def index(id):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = student_pb2_grpc.StudentServiceStub(channel)
        student = client.read_student(stub, str(id))
        if student:
            return render_template('index.html', student=student)
        else:
            return 'Student not found'
        

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        age = request.form['age']
        student = student_pb2.Student(id=id, name=name, age=age)
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = student_pb2_grpc.StudentServiceStub(channel)
            success = client.create_student(stub, student)
            if success:
                return redirect('/')
            else:
                return 'Student already exists'
    else:
        return render_template('add.html')


@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        age = request.form['age']
        with grpc.insecure_channel('localhost:50051') as channel:
            stub = student_pb2_grpc.StudentServiceStub(channel)
            success = client.update_student(stub, id, name, age)
            if success:
                return redirect('/')
            else:
                return 'Failed to update student'
    else: 
        return render_template('edit.html')


@app.route('/delete/<id>')
def delete(id):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = student_pb2_grpc.StudentServiceStub(channel)
        success = client.delete_student(stub, id)
        if success:
            return redirect('/')
        else:
            return 'Student not found'


if __name__ == '__main__':
    app.run(debug=True)
