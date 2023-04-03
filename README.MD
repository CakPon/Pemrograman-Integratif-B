
# Implementasi gRPC API dan Protobuf

## Tools yang Digunakan
- Python
- Firebase
- HTML
- Flask

## Langkah-Langkah
- Install library yang diperlukan `pip install grpcio grpcio-tools protobuf firebase-admin flask`
- Buat file protobuf `student.proto`
- Generate kode Python dari file `student.proto` menggunakan protoc `python -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. student.proto`
- Buat file `server.py` untuk membuat server gRPC
- Buat file `client.py` untuk membuat client gRPC
- Buat file `app.py` untuk membuat UI sederhana dengan `Flask`
- Buat file `index.html`, `add.html`, `edit.html` di folder `templates` untuk membuat tampilan UI
- Jalankan server dengan perintah `python server.py` di terminal
- Jalankan aplikasi `Flask` dengan perintah `python app.py` di terminal
- Buka browser dan akses `http://localhost:5000` untuk mengakses UI aplikasi

## Screenshots

![App Screenshot](https://i.ibb.co/47hwXsM/Whats-App-Image-2023-04-03-at-10-39-32.jpg)


![App Screenshot](https://i.ibb.co/HdrsHJh/Whats-App-Image-2023-04-03-at-10-40-57.jpg)


![App Screenshot](https://i.ibb.co/28YDPh1/Whats-App-Image-2023-04-03-at-10-41-51.jpg)


![App Screenshot](https://i.ibb.co/dcG5xxB/Whats-App-Image-2023-04-03-at-10-42-24.jpg)
