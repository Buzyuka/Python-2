import argparse
from socket import *
from jmi_io import *
from log.server_log_config import *
import log.decorators


@log.decorators.log()
def test_log(x, y):
    pass


def main():
    test_log(1, 2)
    test_log(x=1, y=2)


main()


log = logging.getLogger('app.main')

parser = argparse.ArgumentParser(description='Server')

parser.add_argument('-a', dest='addr', default='', help='address to server')
parser.add_argument('-p', dest='port', default=7777, type=int, help='port')

args = parser.parse_args()

s = socket(AF_INET, SOCK_STREAM)

try:
    s.bind((args.addr, args.port))
    s.listen(5)

    log.info(f"Started server at {args.addr}:{args.port}")

    while True:
        client, addr = s.accept()
        data = client.recv(1000000)
        request = json.loads(data.decode('ascii'))
        action = request["action"]
        decoded_data = data.decode('ascii')

        log.info(f"Message: {decoded_data}, was receiveS by client: {addr}")

        if request["action"] == "presence":
            client.send(build_response(100, "Hello"))
        else:
            client.send(build_response(400, f"Unspecified action: {action}"))
            log.error(f"Unspecified action: {action}")

        client.close()
except KeyboardInterrupt:
    s.close()
except Exception as e:
    log.critical(str(e))
