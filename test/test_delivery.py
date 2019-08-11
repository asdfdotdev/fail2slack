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
