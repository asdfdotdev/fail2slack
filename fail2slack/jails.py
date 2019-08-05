# -*- coding: utf-8 -*-

import re
import subprocess
import sys


def get_jails_status(active_jails):
    jails_status = []

    try:
        for jail in active_jails:
            jail_output = subprocess.check_output("fail2ban-client status " + jail, shell=True).decode('utf-8')

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

            jails_status.append([
                jail,
                current_failed_count,
                total_failed_count,
                current_banned_count,
                total_banned_count
            ])
    except subprocess.CalledProcessError:
        sys.exit("Unable to get fail2ban-client status. Confirm it is available and you have permission to use it.")

    return jails_status
