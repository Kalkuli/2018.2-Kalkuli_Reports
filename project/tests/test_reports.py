import json
import unittest
from project.tests.base import BaseTestCase
from project.api.models import Report
from datetime import datetime
from project import db
from project.tests.utils import add_report

class TestReportService(BaseTestCase):

    def test_add_report(self):
        with self.client:
            response = self.client.post(
                '/add_report',
                data = json.dumps({
                    "category_id": "1234",
                    "tag_id": "1",
                    "date_to": "2018-02-23",
                    "date_from": "2018-02-12"
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


    def test_get_all_reports(self):
        start = "22-09-2018"
        end = "22-11-2018"

        dateStart = datetime.strptime(start, '%d-%m-%Y').date()
        dateEnd = datetime.strptime(end, '%d-%m-%Y').date()

        start = datetime.strptime(start, '%d-%m-%Y').strftime('%a, %d %b %Y %H:%M:%S GMT')
        end = datetime.strptime(end, '%d-%m-%Y').strftime('%a, %d %b %Y %H:%M:%S GMT')

        add_report(1, 2, dateStart, dateEnd)
        add_report(2, 3, dateStart, dateEnd)

        with self.client:
            response = self.client.get('/1/get_reports')
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

        report = add_report(1, 2, dateStart, dateEnd)

        with self.client:
            response = self.client.delete(f'/1/report/{report.id}')
            data = json.loads(response.data.decode())

            self.assertEqual(response.status_code, 200)
            self.assertIn('Success', data['status'])
            self.assertIn('Report deleted', data['data']['message'])

    def test_remove_report_report_not_found(self):
        start = "22-09-2018"
        end = "22-11-2018"

        dateStart = datetime.strptime(start, '%d-%m-%Y').date()
        dateEnd = datetime.strptime(end, '%d-%m-%Y').date()

        start = datetime.strptime(start, '%d-%m-%Y').strftime('%a, %d %b %Y %H:%M:%S GMT')
        end = datetime.strptime(end, '%d-%m-%Y').strftime('%a, %d %b %Y %H:%M:%S GMT')

        report = add_report(1, 2, dateStart, dateEnd)

        with self.client:
            response = self.client.delete(f'/1/report/123')
            data = json.loads(response.data.decode())

            self.assertEqual(response.status_code, 404)
            self.assertIn('Fail', data['status'])
            self.assertIn('Report not found', data['message'])

if __name__ == '__main__':
    unittest.main()