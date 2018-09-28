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

    def test_empty_json(self):
        with self.client:
            response = self.client.post(
                '/report',
                data = json.dumps({
                }), 
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
        
if __name__ == '__main__':
    unittest.main()