# -*- coding: utf-8 -*-

import sys


class Delivery:

    def __init__(self, settings):
        self._delivery_method = settings.get_delivery_method()
        self._webhook_url = settings.get_webhook_url()

    def output(self, jail_data):
        message = self.__generate_message(self, jail_data)

        if 1 == self._delivery_method:
            self.__slack_output(self, message)
        else:
            self.__print_output(self, message)

    @staticmethod
    def __generate_message(self, jail_data):
        message = ''

        for jail in jail_data:
            message += "*{0}*\n\tFailed: {1} ({2}), Banned: {3} ({4})\n".format(*jail)

        return message

    @staticmethod
    def __print_output(self, message):
        print(message)

    @staticmethod
    def __slack_output(self, message):
        import requests
        import json

        response = requests.post(
            self._webhook_url,
            data=json.dumps({'text': message}),
            headers={'Content-Type': 'application/json'}
        )

        if response.status_code != 200:
            sys.exit("Slack webhook connection failed with error: {0} ({1})".format(response.text, response.status_code))
