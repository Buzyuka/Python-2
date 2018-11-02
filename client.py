import argparse
from socket import *
from lesson_5.jmi_io import *
from lesson_5.log.client_log_config import *

log = logging.getLogger('app.main')

parser = argparse.ArgumentParser(description='Client')

parser.add_argument('-a', dest='addr', default="127.0.0.1", help='address to server')
parser.add_argument('-p', dest='port', default=7777, type=int, help='port')

args = parser.parse_args()

try:
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((args.addr, args.port))

    log.info(f"Connected to {args.addr}:{args.port}")

    s.send(build_presence_status_request(account_name="C0deMaver1ck", status="Yep, I am here!"))
    data = s.recv(1000000)

    print('Сообщение от сервера: ', json.loads(data.decode('ascii')), ', длиной ', len(data), ' байт')
    decoded_message = data.decode('ascii')
    log.info(f"Message was receive from server {decoded_message}, length: {len(data)} bytes")

    s.close()
except Exception as e:
    log.critical(repr(e))
