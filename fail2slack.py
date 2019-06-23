#!/usr/bin/env python

import json
import os.path
import re
import requests
import subprocess
import time

def compile_status(vaults):
    current_status = ''

    for vault in vaults:
        vault_status = subprocess.check_output("fail2ban-client status " + vault, shell=True).decode('utf-8')

        current_failed_count = 0
        total_failed_count = 0
        current_banned_count = 0
        total_banned_count = 0

        current_failed = re.search(r"Currently failed:(.*\b)", vault_status, re.IGNORECASE | re.MULTILINE)
        total_failed = re.search(r"Total failed:(.*\b)", vault_status, re.IGNORECASE | re.MULTILINE)
        current_banned = re.search(r"Currently banned:(.*\b)", vault_status, re.IGNORECASE | re.MULTILINE)
        total_banned = re.search(r"Total banned:(.*\b)", vault_status, re.IGNORECASE | re.MULTILINE)

        if current_failed:
            current_failed_count = current_failed.group(1).strip()

        if total_failed:
            total_failed_count = total_failed.group(1).strip()

        if current_banned:
            current_banned_count = current_banned.group(1).strip()

        if total_banned:
            total_banned_count = total_banned.group(1).strip()

        current_status += "*{}*\n\tFailed: {} ({}), Banned: {} ({})\n".format(
            vault,
            current_failed_count,
            total_failed_count,
            current_banned_count,
            total_banned_count
        )

    return current_status

def send_to_slack(webhook_url):
    response = requests.post(
        webhook_url,
        data=json.dumps({'text': current_status}),
        headers={'Content-Type': 'application/json'}
    )

    if response.status_code != 200:
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

        f = open('fail2slack.log','a')
        f.write('\n' + now + ' -- Slack webhook request error, status: {}, message: {}'.format(response.status_code, response.text))
        f.close()

if os.path.exists('fail2slackconfig.py'):
    import fail2slackconfig as config
    current_status = compile_status(config.vaults)

    if current_status:
        send_to_slack(config.webhook_url)

else:
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())

    f = open('fail2slack.log','a')
    f.write('\n' + now + ' -- Config file missing, cannot run.')
    f.close()
