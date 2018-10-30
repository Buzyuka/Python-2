# Программа сервера для отправки приветствия сервера и получения ответа
import json
import argparse
from socket import *
from .jmi_io import *

parser = argparse.ArgumentParser(description='Client')

parser.add_argument('-a', dest='addr', default="127.0.0.1", help='address to server')
parser.add_argument('-p', dest='port', default=7777, type=int, help='port')

args = parser.parse_args()

s = socket(AF_INET, SOCK_STREAM)
s.connect((args.addr, args.port))

print(f"Connected to {args.addr}:{args.port}")

s.send(build_presence_status_request(account_name="C0deMaver1ck", status="Yep, I am here!"))
data = s.recv(1000000)
print('Сообщение от сервера: ', json.loads(data.decode('ascii')), ', длиной ', len(data), ' байт')
s.close()
