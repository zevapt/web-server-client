import socket
import os

# konfigurasi server
server_address = ('localhost', 8080)

# buat socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind socket ke alamat dan port tertentu
server_socket.bind(server_address)

# listen untuk koneksi masuk
server_socket.listen(1)

print(f"Sedang menunggu koneksi di {server_address}...")

while True:
    # terima koneksi dari client
    client_socket, client_address = server_socket.accept()

    print(f"Menerima koneksi dari {client_address}")

    # terima data dari client
    request_data = client_socket.recv(1024)

    # parsing HTTP request
    request_str = request_data.decode()
    request_method, request_path, request_protocol = request_str.split('\n')[0].split()

    print(f"HTTP request method: {request_method}")
    print(f"HTTP request path: {request_path}")
    print(f"HTTP request protocol: {request_protocol}")

    # cari file yang diminta oleh client (masih blum bisa tp hrsnya udh bener)
    file_path = "." + request_path
    if os.path.isfile(file_path):
        # buat HTTP response message dengan status code 200 OK (header + content)
        with open(file_path, 'rb') as file:
            response_data = b"HTTP/1.1 200 OK\r\n\r\n" + file.read()
    else:
        # buat HTTP response message dengan status code 404 Not Found
        response_data = b"HTTP/1.1 404 Not Found\r\n\r\nFile not found"

    # kirim response message ke client
    client_socket.sendall(response_data)

    # tutup koneksi dengan client
    client_socket.close()
