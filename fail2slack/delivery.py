# -*- coding: utf-8 -*-
"""
Delivery class for fail2slack module
"""

import sys
import json
import requests


class Delivery:
    """
    Delivers update containing current information about fail2ban jails
    """

    def __init__(self, settings):
        self._delivery_method = settings.get_delivery_method()
        self._identifier = settings.get_identifier()
        self.webhook_url = settings.get_webhook_url()

    def output(self, jail_data):
        """
        Output update message based on current settings.
        :param jail_data: array of jail data (failed/banned)
        :return: void
        """
        message = self.generate_message(jail_data)

        if self._delivery_method == 1:
            self.slack_output(message, self)
        else:
            self.print_output(message)

    def generate_message(self, jail_data):
        """
        Generate update message using jail data.
        :param jail_data: array of jail data (failed/banned)
        :return: string formatting update message
        """
        message = ''

        if self._identifier:
            message += f'*Stats for {self._identifier}*\n'

        for jail in jail_data:
            message += f">*{jail[0]}*\n>\tFailed: {jail[1]} ({jail[2]}), Banned: {jail[3]} ({jail[4]})\n"

        return message

    @staticmethod
    def print_output(message):
        """
        Output message to a stream, or to sys.stdout by default.
        :param message: string message
        :return: void
        """
        print(message)

    @staticmethod
    def slack_output(message, self):
        """
        Send message to slack via webhook.
        :param message: string message
        :return: void
        """

        response = requests.post(
            self.webhook_url,
            data=json.dumps({'text': message}),
            headers={'Content-Type': 'application/json'},
            timeout=120
        )

        if response.status_code != 200:
            sys.exit(f"Slack webhook connection failed with error: {response.text} ({response.status_code})")
