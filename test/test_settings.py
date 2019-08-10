import unittest
import fail2slack
from fail2slack.settings import Settings


class TestSettings(unittest.TestCase):

    def setUp(self):
        pass

    def test_invalid_delivery_method(self):
        settings = {
            "delivery" : -1,
            "jail" : [],
            "webhook" : None,
        }

        test_settings = Settings()

        with self.assertRaises(SystemExit) as system_exit:
            test_settings.validate_settings(settings)
        self.assertEqual(system_exit.exception.code, "Delivery method should be 0 (Print) or 1 (Slack)")


if __name__ == '__main__':
    unittest.main()
