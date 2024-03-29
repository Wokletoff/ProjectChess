import socket
import threading


class ChatServer:
    clients_list = []

    last_received_message = ""

    def __init__(self):
        self.server_socket = None
        self.create_listening_server()

    # listen for incoming connection/Проверяем входящее соединение
    def create_listening_server(self):

        self.server_socket = socket.socket(socket.AF_INET,
                                           socket.SOCK_STREAM)  # create a socket using TCP port and ipv4/с
        # спользуя порт ipv4
        local_ip = input("Your IP: ")
        local_port = 33000
        # this will allow you to immediately restart a TCP server/это позволит вам немедленно перезапустить TCP-сервер
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # this makes the server listen to requests coming from other computers on the network/это заставляет сервер прослушивать запросы, поступающие с других компьютеров в сети
        self.server_socket.bind((local_ip, local_port))
        print("Listening for incoming messages..")
        self.server_socket.listen(5)  # listen for incomming connections / max 5 clients/прослушивание входящих подключений / максимум 5 клиентов
        self.receive_messages_in_a_new_thread()


    def receive_messages(self, so):
        while True:
            incoming_buffer = so.recv(256)  # initialize the buffer/инициализируйте буфер
            if not incoming_buffer:
                break
            self.last_received_message = incoming_buffer.decode('utf-8')
            self.broadcast_to_all_clients(so)  # send to all clients/отправить всем клиентам
        so.close()

    # broadcast the message to all clients/передайте сообщение всем клиентам
    def broadcast_to_all_clients(self, senders_socket):
        for client in self.clients_list:
            socket, (ip, port) = client
            if socket is not senders_socket:
                socket.sendall(self.last_received_message.encode('utf-8'))

    def receive_messages_in_a_new_thread(self):
        while True:
            client = so, (ip, port) = self.server_socket.accept()
            self.add_to_clients_list(client)
            print('Connected to ', ip, ':', str(port))
            t = threading.Thread(target=self.receive_messages, args=(so,))
            t.start()

    # add a new client/добавьте нового клиента
    def add_to_clients_list(self, client):
        if client not in self.clients_list:
            self.clients_list.append(client)


if __name__ == "__main__":
    ChatServer()