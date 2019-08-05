# -*- coding: utf-8 -*-


class Delivery:

    def __init__(self, settings):
        self._delivery_method = settings.get_delivery_method()
        self._webhook_url = settings.get_webhook_url()

    def output(self, jail_data):
        message = self.__generate_message(self, jail_data)

        if 1 == self._delivery_method:
            self.__slack_output(self, self.webhook_url, message)
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

        # todo:replace with proper error handling
        # if response.status_code != 200:
        #     now = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        #
        #     f = open('fail2slack.log','a')
        #     f.write('\n' + now + ' -- Slack webhook request error, status: {0}, message: {1}'.format(response.status_code, response.text))
        #     f.close()
