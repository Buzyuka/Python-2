import json
import time


def build_presence_status_request(account_name, status=None):
    assert (len(account_name) <= 25)

    if status is None:
        return _build_request(
            action="presence",
            payload={
                "user": {
                    "account_name": account_name
                }
            }
        )
    else:
        return _build_request(
            action="presence",
            payload={
                "type": "status",
                "user": {
                    "account_name": account_name,
                    "status": status
                }
            }
        )


def build_probe_request():
    return _build_request("probe", {})


def build_quit_request():
    return _build_request("quit", {})


def build_message_request(account_name, room, message):
    return _build_request("msg", {
        "from": account_name,
        "to": "#" + room,
        "message": message
    })


def _build_request(action, payload):
    assert (len(action) <= 15)

    result = {
        "action": action,
        "time": time.ctime(time.time())
    }

    result.update(payload)
    return json.dumps(result).encode("ascii")


def build_response(status_code, message):
    assert (len(message) <= 500)

    if 299 >= status_code >= 100:
        return json.dumps({
            "response": status_code,
            "time": time.ctime(time.time()),
            "alert": message
        }).encode("ascii")

    if 599 >= status_code >= 400:
        return json.dumps({
            "response": status_code,
            "time": time.ctime(time.time()),
            "error": message
        }).encode("ascii")

    raise IOError("Unspecified status code")


def read_response(sock):
    data = sock.recv(1000000)
    return json.loads(data.decode('ascii'))
