# -*- coding: utf-8 -*-
"""
Settings class for fail2slack module
"""

import argparse
import platform
import sys
import validators


class Settings:
    """
    Accept settings from user, validate values, and make available for use.
    """

    def __init__(self):
        self._webhook_url = None
        self._jails = None
        self._delivery_method = None
        self._identifier = None

    def process_args(self, args):
        """
        Create dict of setting values from provided args.

        :param args: sys.argv containing provided values
        :return: void
        """

        parser = argparse.ArgumentParser()

        parser.add_argument(
            "-w",
            "--webhook",
            type=str,
            default="",
            help="Slack webhook URL. Required if delivery method is 1."
        )

        parser.add_argument(
            "-d",
            "--delivery",
            type=int,
            default=0,
            help="Delivery method: 0 = print, 1 = Slack webhook."
        )

        parser.add_argument(
            "-j",
            "--jails",
            nargs="+",
            help="Jails to include in status report. Required."
        )

        parser.add_argument(
            "-i",
            "--identifier",
            type=str,
            help="Update identifier. STRING of identifier to use. Default is hostname."
        )

        args = parser.parse_args()

        self.validate_settings({
            "webhook" : args.webhook,
            "delivery" : args.delivery,
            "jails" : args.jails,
            "identifier" : args.identifier
        })

    def validate_settings(self, settings):
        """
        Validate settings values, exit with appropriate warning when settings
        won't allow us to continue.
        :param settings: Dict of settings.
        :return: void
        """

        webhook = settings.get('webhook')
        delivery = settings.get('delivery')
        jails = settings.get('jails')
        identifier = settings.get('identifier')

        if webhook:
            if validators.url(webhook):
                self.set_webhook_url(webhook)
            else:
                sys.exit("Webhook value is not a value URL.")

        if 0 <= delivery <= 1:
            self.set_delivery_method(delivery)
        else:
            sys.exit("Delivery method should be 0 (Print) or 1 (Slack)")

        if jails:
            self.set_jails(jails)
        else:
            sys.exit("One or more Jails are required.")

        if identifier:
            self.set_identifier(identifier)
        else:
            self.set_identifier(platform.node())

        if delivery == 1 and not webhook:
            sys.exit("Webhook required for delivery setting 1 (Slack)")

    #
    # Setters & Getters
    #

    def set_webhook_url(self, url):
        """
        Set webhook value
        :param url: string webhook url
        :return: void
        """
        self._webhook_url = url

    def get_webhook_url(self):
        """
        Get webhook value
        :return: string
        """
        return self._webhook_url

    def set_delivery_method(self, method):
        """
        Set delivery method value
        :param url: integer delivery method
        :return: void
        """
        self._delivery_method = method

    def get_delivery_method(self):
        """
        Get delivery method value
        :return: integer
        """
        return self._delivery_method

    def set_jails(self, jails):
        """
        Set active jails
        :param url: string webhook url
        :return: void
        """
        self._jails = jails

    def get_jails(self):
        """
        Get active jails
        :return: string
        """
        return self._jails

    def set_identifier(self, identifier):
        """
        Set server identifier
        :param identifier: string identifier
        :return: void
        """
        self._identifier = identifier

    def get_identifier(self):
        """
        Get identifier
        :return: string
        """
        return self._identifier
