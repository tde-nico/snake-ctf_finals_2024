import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('cafe.challs.snakectf.org', 5875))
request = 'GET check HTTP/1.1\r\nHost: cafe.challs.snakectf.org\r\nConnection: close\r\nUser-Agent: õ²\tIúÖP\r\nAccept-Encoding: gzip, deflate\r\n\r\n'
client_socket.sendall(request.encode('latin'))

buf = client_socket.recv(102400)

print(buf)
