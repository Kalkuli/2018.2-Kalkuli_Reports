import json
import unittest
from project.tests.base import BaseTestCase


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

    def test_missing_total_cost(self):
        with self.client:
            response = self.client.post(
                '/add_report',
                data = json.dumps({
                    "date_to": "2018-02-12",
                    "date_from": "2018-02-22"
                }), 
                content_type = 'application/json',
            )

            data = json.loads(response.data.decode())

            self.assertEqual(response.status_code, 400)
        
if __name__ == '__main__':
    unittest.main()