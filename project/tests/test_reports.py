import json
import unittest
from project.tests.base import BaseTestCase
from project.api.models import Report
from datetime import datetime
from project import db
from project.tests.utils import add_report

class TestReportService(BaseTestCase):
    
    def test_reports(self):
        response = self.client.get('/')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('Welcome to Kalkuli Reports Service!', data['data'])

    def test_reports(self):
        with self.client:
            response = self.client.post(
                '/report',
                data = json.dumps({
                    'receipts': [
                        {
                            'total_price': 12
                        },
                        {
                            'total_price': 13
                        }
                    ]
                }),
                content_type = 'application/json',
            )

            data = json.loads(response.data.decode())

            self.assertEqual(response.status_code, 200)
            self.assertIn( '25', data['total_cost'])

    def test_empty_json_report(self):
        with self.client:
            response = self.client.post(
                '/report',
                data = json.dumps({}), 
                content_type = 'application/json',
            )

            data = json.loads(response.data.decode())

            self.assertEqual(response.status_code, 400)

    def test_missing_total_price(self):
        with self.client:
            response = self.client.post(
                '/report',
                data = json.dumps({
                    'receipts': [
                        {

                        }, 
                        {
                            'total_price': 12
                        }
                    ]
                }), 
                content_type = 'application/json',
            )

            data = json.loads(response.data.decode())

            self.assertEqual(response.status_code, 400)

    def test_add_report(self):
        with self.client:
            response = self.client.post(
                '/add_report',
                data = json.dumps({
                    "date_to": "2018-02-23",
                    "date_from": "2018-02-12",
                    "total_cost": "123"
                }),
                content_type = 'application/json',
            )

            data = json.loads(response.data.decode())

            self.assertEqual(response.status_code, 200)
            self.assertIn('success', data['status'])
            self.assertIn('Report was created!', data['data']['message'])

    def test_empty_json_add_report(self):
        with self.client:
            response = self.client.post(
                '/add_report',
                data = json.dumps({}), 
                content_type = 'application/json',
            )

            data = json.loads(response.data.decode())

            self.assertEqual(response.status_code, 400)

    def test_missing_date_to(self):
        with self.client:
            response = self.client.post(
                '/add_report',
                data = json.dumps({
                    "date_from": "2018-02-12",
                    "total_cost": "123"
                }), 
                content_type = 'application/json',
            )

            data = json.loads(response.data.decode())

            self.assertEqual(response.status_code, 400)

    def test_missing_date_from(self):
        with self.client:
            response = self.client.post(
                '/add_report',
                data = json.dumps({
                    "date_to": "2018-02-12",
                    "total_cost": "123"
                }), 
                content_type = 'application/json',
            )

            data = json.loads(response.data.decode())

            self.assertEqual(response.status_code, 400)

    def test_get_all_receipts(self):
        start = "22-09-2018"
        end = "22-11-2018"

        dateStart = datetime.strptime(start, '%d-%m-%Y').date()
        dateEnd = datetime.strptime(end, '%d-%m-%Y').date()

        start = datetime.strptime(start, '%d-%m-%Y').strftime('%a, %d %b %Y %H:%M:%S GMT')
        end = datetime.strptime(end, '%d-%m-%Y').strftime('%a, %d %b %Y %H:%M:%S GMT')

        add_report(None, dateStart, dateEnd, None, None)

        with self.client:
            response = self.client.get('/get_reports')
            data = json.loads(response.data.decode())

            self.assertEqual(response.status_code, 200)
            self.assertEqual(len(data['data']['reports']), 1)

            self.assertEqual(start, data['data']['reports'][0]['date_from'])
            self.assertEqual(end, data['data']['reports'][0]['date_to'])

    def test_remove_report(self):
        start = "22-09-2018"
        end = "22-11-2018"

        dateStart = datetime.strptime(start, '%d-%m-%Y').date()
        dateEnd = datetime.strptime(end, '%d-%m-%Y').date()

        start = datetime.strptime(start, '%d-%m-%Y').strftime('%a, %d %b %Y %H:%M:%S GMT')
        end = datetime.strptime(end, '%d-%m-%Y').strftime('%a, %d %b %Y %H:%M:%S GMT')

        report = add_report(None, dateStart, dateEnd, None, None)

        with self.client:
            response = self.client.delete(f'/report/{report.id}')
            data = json.loads(response.data.decode())

            self.assertEqual(response.status_code, 200)
            self.assertIn('Success', data['status'])
            self.assertIn('Report deleted', data['data']['message'])

if __name__ == '__main__':
    unittest.main()