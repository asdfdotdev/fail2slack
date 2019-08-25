# -*- coding: utf-8 -*-

import re
import subprocess
import sys


class Jails:
    """
    Retrieve command output and prepare jail data to be reported for selected jails
    """

    def __init__(self, settings):
        self._jails = settings.get_jails()

    def get_jails_status(self):
        jails_status = []

        for jail in self._jails:
            try:
                jails_status.append(
                    self.prepare_jails_data(
                        jail,
                        subprocess.check_output(
                            "fail2ban-client status " + jail,
                            shell=True,
                            stderr=subprocess.DEVNULL
                        ).decode('utf-8')
                    )
                )
            except subprocess.CalledProcessError:
                sys.exit("fail2ban-client status failed. Confirm it is available and you have permission to use it.")

        return jails_status

    def prepare_jails_data(self, jail, jail_output):
        current_failed_count = 0
        total_failed_count = 0
        current_banned_count = 0
        total_banned_count = 0

        current_failed = re.search(r"Currently failed:(.*\b)", jail_output, re.IGNORECASE | re.MULTILINE)
        total_failed = re.search(r"Total failed:(.*\b)", jail_output, re.IGNORECASE | re.MULTILINE)
        current_banned = re.search(r"Currently banned:(.*\b)", jail_output, re.IGNORECASE | re.MULTILINE)
        total_banned = re.search(r"Total banned:(.*\b)", jail_output, re.IGNORECASE | re.MULTILINE)

        if current_failed:
            current_failed_count = current_failed.group(1).strip()

        if total_failed:
            total_failed_count = total_failed.group(1).strip()

        if current_banned:
            current_banned_count = current_banned.group(1).strip()

        if total_banned:
            total_banned_count = total_banned.group(1).strip()

        return [
            jail,
            current_failed_count,
            total_failed_count,
            current_banned_count,
            total_banned_count
        ]
