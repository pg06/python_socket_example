import socket

my_ip = socket.gethostbyname(socket.gethostname())  # IP local
my_address = (my_ip, 5005)
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind(my_address)

print " Servidor iniciado %s:%s" % my_address
print ">>>"
while True:
    data, (addr, port) = sock.recvfrom(1024) # buffer size is 1024 bytes
    user, msg = '', ''
    if ':' in data:
        user = data.split(':')[0]
        msg = ''.join(data.split(':')[1:])
    print "  User IP:", addr, ":", port, "\n  User:", user, "\n  Mensagem:", msg
    print ">>>"
