import socket
from _thread import *
import sys

server = "IP do Servidor"
port = 5515
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("esperando por uma conexão, servidor ligado.")

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

pos = [(0,0),(100,100)]
def threaded_client(conn, player):
    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode())
            pos[player] = data
            if not data:
                print("Disconectado!")
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]

                print("Recebido: ",data)
                print("Enviando: ",reply)
            conn.sendall(str.encode(make_pos(reply)))
        
        except:
            break


currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Conectado a:",conn)
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1