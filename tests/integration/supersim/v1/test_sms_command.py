# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class SmsCommandTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.supersim.v1.sms_commands.create(sim="HSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", payload="payload")

        values = {'Sim': "HSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", 'Payload': "payload", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://supersim.twilio.com/v1/SmsCommands',
            data=values,
        ))

    def test_create_command_minimal_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "payload": "checkin: firmware update",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "sim_sid": "HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sid": "HCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "status": "queued",
                "direction": "to_sim",
                "url": "https://supersim.twilio.com/v1/SmsCommands/HCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.supersim.v1.sms_commands.create(sim="HSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", payload="payload")

        self.assertIsNotNone(actual)

    def test_create_command_full_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "payload": "Report location: (52.520008, 13.404954)",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "sim_sid": "HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sid": "HCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "status": "queued",
                "direction": "to_sim",
                "url": "https://supersim.twilio.com/v1/SmsCommands/HCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.supersim.v1.sms_commands.create(sim="HSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX", payload="payload")

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.supersim.v1.sms_commands("HCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://supersim.twilio.com/v1/SmsCommands/HCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "HCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "payload": "content of the command",
                "sim_sid": "HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "status": "queued",
                "direction": "to_sim",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "url": "https://supersim.twilio.com/v1/SmsCommands/HCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.supersim.v1.sms_commands("HCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.supersim.v1.sms_commands.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://supersim.twilio.com/v1/SmsCommands',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sms_commands": [],
                "meta": {
                    "first_page_url": "https://supersim.twilio.com/v1/SmsCommands?Status=queued&Sim=HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&PageSize=50&Page=0",
                    "key": "sms_commands",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://supersim.twilio.com/v1/SmsCommands?Status=queued&Sim=HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.supersim.v1.sms_commands.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "first_page_url": "https://supersim.twilio.com/v1/SmsCommands?Status=queued&Sim=HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&PageSize=50&Page=0",
                    "key": "sms_commands",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://supersim.twilio.com/v1/SmsCommands?Status=queued&Sim=HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&PageSize=50&Page=0"
                },
                "sms_commands": [
                    {
                        "sid": "HCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "payload": "content of the command",
                        "sim_sid": "HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "status": "queued",
                        "direction": "from_sim",
                        "date_created": "2015-07-30T20:00:00Z",
                        "date_updated": "2015-07-30T20:00:00Z",
                        "url": "https://supersim.twilio.com/v1/SmsCommands/HCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ]
            }
            '''
        ))

        actual = self.client.supersim.v1.sms_commands.list()

        self.assertIsNotNone(actual)
