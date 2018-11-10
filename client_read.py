import argparse
from socket import *
from jmi_io import *
from log.client_log_config import *

log = logging.getLogger('app.main')

parser = argparse.ArgumentParser(description='Client')

parser.add_argument('-a', dest='addr', default="127.0.0.1", help='address to server')
parser.add_argument('-p', dest='port', default=7777, type=int, help='port')

args = parser.parse_args()

sock = socket(AF_INET, SOCK_STREAM)
sock.connect((args.addr, args.port))

try:
    log.info(f"Connected to {args.addr}:{args.port}")
    account_name = input("Input your account name: ")
    request = build_presence_status_request(account_name=account_name, status="read")
    sock.send(request)
    response = read_response(sock)
    log.info("receive response " + str(response))

    assert response["response"] == 100
    log.info(f"successfully logged in as '{account_name}'")

    while True:
        response = sock.recv(1000000).decode('ascii')
        if response != "":
            log.info("receive response " + response)

except KeyboardInterrupt:
    sock.close()
except Exception as e:
    log.critical(repr(e))
