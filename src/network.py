import socket

class Network:
    def __init__(self):
        self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "IP do Servidor"
        self.port = 5515
        self.addr = (self.server, self.port)
        self.pos = self.connect()
    
    def getPos(self):
        return self.pos

    def connect(self):
        try:
            self.cliente.connect(self.addr)
            return self.cliente.recv(2048).decode()
        except:pass

    def send(self, data):
        try:
            self.cliente.send(str.encode(data))
            return self.cliente.recv(2048).decode()
        except socket.error as e:
            print(e)