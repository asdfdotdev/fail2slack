import io
import random
import string
import unittest
import unittest.mock
import fail2slack
from fail2slack.settings import Settings
from fail2slack.delivery import Delivery


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
        }

        test_settings = Settings()
        test_settings.validate_settings(settings)

        self.assertEqual(0, test_settings.get_delivery_method())

    def test_invalid_webhook_no_protocol(self):
        settings = {
            "delivery" : 0,
            "jails" : ['test', 'also-test'],
            "webhook" : "webhook.url",
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
        }

        test_settings = Settings()

        with self.assertRaises(SystemExit) as system_exit:
            test_settings.validate_settings(settings)
        self.assertEqual(system_exit.exception.code, "Webhook required for delivery setting 1 (Slack)")

    #
    # Delivery Tests
    #

    def test_message_format(self):
        test_settings = Settings()
        test_settings.validate_settings({
            "delivery" : 0,
            "jails" : ['test', 'also-test'],
            "webhook" : "https://webhook.url",
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

        test_message = delivery.generate_message(self, [test_data])

        self.assertEqual(test_message, "*{0}*\n\tFailed: {1} ({2}), Banned: {3} ({4})\n".format(*test_data))

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_output_print(self, mock_stdout):
        test_message = ''.join(random.choices(string.ascii_uppercase + string.digits, k=50))
        Delivery.print_output(self, test_message)

        self.assertEqual(mock_stdout.getvalue().rstrip(), test_message.rstrip())


if __name__ == '__main__':
    unittest.main()
