import socket,sys

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

def send_message(user, msg):
    MESSAGE = user + ':' + msg
    
    print "Conectado ", UDP_IP, ":", UDP_PORT
    print "<<<"
    print "  Mensagem Enviada\n  user:", user, "message:", msg
    print "<<<"

    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

if len(sys.argv) == 3:
    USER = sys.argv[1]
    MESSAGE = sys.argv[2]
    send_message(USER, MESSAGE)
else:
    print "Aperte Ctrl + C para finalizar"
    USER = raw_input("Digite o nome do usuario: ")
    while True:
        MESSAGE = raw_input("Digite a mensagem: ")
        if MESSAGE:
            send_message(USER, MESSAGE)
