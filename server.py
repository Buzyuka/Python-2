# Программа сервера для получения приветствия от клиента и отправки ответа
import json
import argparse
from socket import *
from jmi_io import *

parser = argparse.ArgumentParser(description='Client')

parser.add_argument('-a', dest='addr', default='', help='address to server')
parser.add_argument('-p', dest='port', default=7777, type=int, help='port')

args = parser.parse_args()

s = socket(AF_INET, SOCK_STREAM)
s.bind((args.addr, args.port))

print(f"Started server at {args.addr}:{args.port}")

s.listen(5)

try:
    while True:
        client, addr = s.accept()
        data = client.recv(1000000)
        request = json.loads(data.decode('ascii'))
        action = request["action"]

        print('Сообщение: ', data.decode('ascii'), ', было отправлено клиентом: ', addr)

        if request["action"] == "presence":
            client.send(build_response(100, "Hello"))
        else:
            client.send(build_response(400, f"Unspecified action: {action}"))

        client.close()
except KeyboardInterrupt:
    s.close()
