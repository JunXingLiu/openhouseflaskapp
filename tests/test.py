import re
import requests
import unittest

class TestAPI(unittest.TestCase):
    GETURL = 'http://localhost:5000/api/retrievelogs'
    POSTURL = 'http://localhost:5000/api/submitlogs'

    def test_submit_logs(self):
        response = requests.post(self.POSTURL, json={'userId': 'CBC123XYZ', 'sessionId': 'ABC123XYZ', 'actions': [{'type': 'click', 'time': '2018-10-19T00:00:00.000Z', 'properties': {'locationX': 1, 'locationY': 2}}]})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'status': 'logs submitted'})
    
    def test_submit_logs_with_invalid_logType(self):
        response = requests.post(self.POSTURL, json={'userId': 'CBC123XYZ', 'sessionId': 'ABC123XYZ', 'actions': [{'type': 'views', 'time': '2018-10-19T00:00:00.000Z', 'properties': {'locationX': 1, 'locationY': 2}}]})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'status': 'logs submitted'})
        response = requests.get(self.GETURL + '?userId=CBC123XYZ&logType=views')
        self.assertEqual(response.status_code, 400)

    def test_get_logs_by_userId(self):
        response = requests.get(self.GETURL + '?userId=CBC123XYZ')
        self.assertEqual(response.status_code, 200)

    def test_get_logs_by_userId_and_logType(self):
        response = requests.get(self.GETURL + '?userId=CBC123XYZ&logType=click')
        self.assertEqual(response.status_code, 200)

    def test_get_logs_by_userId_and_logType_and_time(self):
        response = requests.get(self.GETURL + '?userId=CBC123XYZ&logType=view&fromTime=2018-10-19&toTime=2018-10-21')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_get_logs_by_logType(self):
        response = requests.get(self.GETURL + '?logType=click')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)


if __name__ == '__main__':
    test = TestAPI()

    test.test_submit_logs()
    test.test_submit_logs_with_invalid_logType()
    test.test_get_logs_by_userId()
    test.test_get_logs_by_userId_and_logType()
    test.test_get_logs_by_userId_and_logType_and_time()
    test.test_get_logs_by_logType()
    test.test_submit_logs_with_invalid_logType()
