import argparse
from socket import *
from jmi_io import *
from log.server_log_config import *
import log.decorators
import select

log = logging.getLogger('app.main')

parser = argparse.ArgumentParser(description='Server')

parser.add_argument('-a', dest='addr', default='', help='address to server')
parser.add_argument('-p', dest='port', default=7777, type=int, help='port')

args = parser.parse_args()


readers_clients = []


def new_listen_socket(address, port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((address, port))
    sock.listen(5)
    sock.settimeout(0.2)

    return sock


def read_requests(clients):
    requests = {}

    for sock in clients:
        try:
            data = sock.recv(1000000)
            requests[sock] = data
        except Exception as e:
            log.info("READ ERROR:" + repr(e))
            log.info('client {} {} was disconnected'.format(sock.fileno(), sock.getpeername()))
            clients.remove(sock)

    # print(requests)
    return requests


def write_responses(requests, clients):
    for sock in clients:
        if sock in requests:
            try:
                # log.info("OK")
                handle_request(requests[sock], sock)
                # resp = requests[sock]
                # test_len = sock.send(resp.upper())
            except Exception as e:
                log.info("WRITE ERROR:" + repr(e))
                log.info('client {} was disconnected'.format(sock.getpeername()))
                sock.close()
                clients.remove(sock)


def handle_request(data, initiator):
    global readers_clients

    response_str = data.decode('ascii')
    log.info(f"receive request '{response_str}'")

    request = json.loads(response_str)
    action = request["action"]

    if action == "presence":
        initiator.send(build_response(100, "Hello"))
        client = {
            "sock": initiator,
            "user": request["user"]
        }

        if request["user"]["status"] == "read":
            readers_clients.append(client)

        log.info(f"logged in new account: {client}")

    elif action == "msg":
        message = request["message"]
        from_account = request["from"]
        log.info(f"receive message: {message} from {from_account}")

        for reader in readers_clients:
            reader["sock"].send(build_response(100, f"{from_account}: {message}"))

    else:
        initiator.send(build_response(400, f"unspecified action: {action}"))
        log.error(f"unspecified action: {action}")


def mainloop():
    sock = new_listen_socket(args.addr, args.port)
    log.info(f"Started server at {args.addr}:{args.port}")

    try:
        clients = []

        while True:
            try:
                conn, addr = sock.accept()
            except OSError:
                # Await
                pass
            else:
                log.info(f"receive request to connection from {addr}")
                clients.append(conn)
            finally:
                wait = 0
                r = []
                w = []

                try:
                    r, w, e = select.select(clients, clients, [], wait)
                except Exception as e:
                    pass

                requests = read_requests(r)
                write_responses(requests, w)

    except KeyboardInterrupt:
        sock.close()


try:
    mainloop()
except Exception as e:
    log.critical(str(e))

# s = socket(AF_INET, SOCK_STREAM)

# try:
#     s.bind((args.addr, args.port))
#     s.listen(5)
#
#     log.info(f"Started server at {args.addr}:{args.port}")
#
#     while True:
#         client, addr = s.accept()
#         data = client.recv(1000000)
#         request = json.loads(data.decode('ascii'))
#         action = request["action"]
#         decoded_data = data.decode('ascii')
#
#         log.info(f"Message: {decoded_data}, was receiveS by client: {addr}")
#
#         if request["action"] == "presence":
#             client.send(build_response(100, "Hello"))
#         else:
#             client.send(build_response(400, f"Unspecified action: {action}"))
#             log.error(f"Unspecified action: {action}")
#
#         client.close()
# except KeyboardInterrupt:
#     s.close()
# except Exception as e:
#     log.critical(str(e))
