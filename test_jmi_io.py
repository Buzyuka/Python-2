from unittest import TestCase

from lesson_5.jmi_io import *


class Test(TestCase):
    def _now(self):
        return time.ctime(time.time())

    def test_build_probe_request(self):
        self.assertEqual('{"action": "probe", "time": "%s"}' % self._now(), build_probe_request().decode("utf"))

    def test_build_quit_request(self):
        self.assertEqual('{"action": "quit", "time": "%s"}' % self._now(), build_quit_request().decode("utf"))

    def test_build_presence_status_request(self):
        request = build_presence_status_request(account_name="C0deMaver1ck", status="Yep, I am here!")
        expected = '{"action": "presence", "time": "%s", "type": "status",' \
                   ' "user": {"account_name": "C0deMaver1ck", "status": "Yep, I am here!"}}' % self._now()
        self.assertEqual(expected, request.decode("utf"))

    def test_build_success_response(self):
        self.assertEqual('{"response": 200, "time": "%s", "alert": "Success"}' % self._now(), build_response(200, "Success").decode("utf"))

    def test_build_error_response(self):
        self.assertEqual('{"response": 400, "time": "%s", "error": "Error"}' % self._now(), build_response(400, "Error").decode("utf"))
