import io
import random
import socket
import string
import unittest.mock
from fail2slack.settings import Settings
from fail2slack.delivery import Delivery
from fail2slack.jails import Jails

class TestSettings(unittest.TestCase):

    def setUp(self):
        pass

    #
    # Settings Tests
    #

    def test_invalid_delivery_method(self):
        settings = {
            "delivery" : -1,
            "jails" : ['test', 'also-test'],
            "webhook" : "https://webhook.url",
            "identifier" : None
        }

        test_settings = Settings()

        with self.assertRaises(SystemExit) as system_exit:
            test_settings.validate_settings(settings)
        self.assertEqual(system_exit.exception.code, "Delivery method should be 0 (Print) or 1 (Slack)")

    def test_invalid_jails(self):
        settings = {
            "delivery" : 0,
            "jails" : None,
            "webhook" : "https://webhook.url",
            "identifier" : None
        }

        test_settings = Settings()

        with self.assertRaises(SystemExit) as system_exit:
            test_settings.validate_settings(settings)
        self.assertEqual(system_exit.exception.code, "One or more Jails are required.")

    def test_invalid_webhook_print(self):
        settings = {
            "delivery" : 0,
            "jails" : ['test', 'also-test'],
            "webhook" : None,
            "identifier" : None
        }

        test_settings = Settings()
        test_settings.validate_settings(settings)

        self.assertEqual(0, test_settings.get_delivery_method())

    def test_invalid_webhook_no_protocol(self):
        settings = {
            "delivery" : 0,
            "jails" : ['test', 'also-test'],
            "webhook" : "webhook.url",
            "identifier" : None
        }

        test_settings = Settings()

        with self.assertRaises(SystemExit) as system_exit:
            test_settings.validate_settings(settings)
        self.assertEqual(system_exit.exception.code, "Webhook value is not a value URL.")

    def test_invalid_webhook_missing_slack(self):
        settings = {
            "delivery" : 1,
            "jails" : ['test', 'also-test'],
            "webhook" : None,
            "identifier" : None
        }

        test_settings = Settings()

        with self.assertRaises(SystemExit) as system_exit:
            test_settings.validate_settings(settings)
        self.assertEqual(system_exit.exception.code, "Webhook required for delivery setting 1 (Slack)")

    def test_identifier_default(self):
        test_settings = Settings()
        test_settings.validate_settings({
            "delivery" : 1,
            "jails" : ['test', 'also-test'],
            "webhook" : "https://webhook.url",
            "identifier" : None
        })

        self.assertEqual(test_settings.get_identifier(), socket.gethostname())

    #
    # Delivery Tests
    #

    def test_message_format(self):
        test_settings = Settings()
        test_settings.validate_settings({
            "delivery" : 0,
            "jails" : ['test', 'also-test'],
            "webhook" : "https://webhook.url",
            "identifier" : "Testing"
        })

        delivery = Delivery(test_settings)

        test_jail = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
        test_current_failed_count = random.randint(1,1000)
        test_total_failed_count = random.randint(1001,2000)
        test_current_banned_count = random.randint(2001,3000)
        test_total_banned_count = random.randint(3001,4000)

        test_data = [
            test_jail,
            test_current_failed_count,
            test_total_failed_count,
            test_current_banned_count,
            test_total_banned_count,
        ]

        test_message = delivery.generate_message([test_data])
        expected_message = "*Stats for {0}*\n".format(test_settings.get_identifier()) + \
                           ">*{0}*\n>\tFailed: {1} ({2}), Banned: {3} ({4})\n".format(*test_data)

        self.assertEqual(test_message, expected_message)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_output_print(self, mock_stdout):
        test_message = ''.join(random.choices(string.ascii_uppercase + string.digits, k=50))
        Delivery.print_output(test_message)

        self.assertEqual(mock_stdout.getvalue().rstrip(), test_message.rstrip())

    def test_jail_error(self):
        test_settings = Settings()
        test_settings.validate_settings({
            "delivery" : 0,
            "jails" : ['test', 'also-test'],
            "webhook" : "https://webhook.url",
            "identifier" : "Testing"
        })

        test_jails = Jails(test_settings)

        with self.assertRaises(SystemExit) as system_exit:
            test_jails.get_jails_status()
        self.assertEqual(
            system_exit.exception.code,
            "fail2ban-client status failed. Confirm it is available and you have permission to use it."
        )

    def test_jail_prepare_data(self):
        test_settings = Settings()
        test_settings.validate_settings({
            "delivery" : 0,
            "jails" : ['test', 'also-test'],
            "webhook" : "https://webhook.url",
            "identifier" : "Testing"
        })

        test_jails = Jails(test_settings)

        test_jail = 'my-test-jail'
        test_current_failed_count = random.randint(1,1000)
        test_total_failed_count = random.randint(1,1000)
        test_current_banned_count = random.randint(1,1000)
        test_total_banned_count = random.randint(1,1000)

        test_status = """Status for the jail: {0}
|- Filter
|  |- Currently failed:	{1}
|  |- Total failed:	{2}
|  `- File list:	/var/log/test/fake.log
`- Actions
   |- Currently banned:	{3}
   |- Total banned:	{4}
   `- Banned IP list:	111.222.333.444""".format(
            test_jail,
            test_current_failed_count,
            test_total_failed_count,
            test_current_banned_count,
            test_total_banned_count,
        )

        test_data = [
            test_jail,
            str(test_current_failed_count),
            str(test_total_failed_count),
            str(test_current_banned_count),
            str(test_total_banned_count),
        ]

        test_response = test_jails.prepare_jails_data(test_jail, test_status)

        self.assertEqual(test_response, test_data)

if __name__ == '__main__':
    unittest.main()
