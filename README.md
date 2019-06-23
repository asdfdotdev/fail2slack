# fail2slack

A friendly little script that can package up your fail2ban vault statuses and send them to you over slack.

## Setup

Create fail2slackconfig.py

```
$ cp fail2slackconfig.dist.py fail2slackconfig.py
``` 

[Setup your Slack webhook](https://api.slack.com/incoming-webhooks) and add it to the config file:

```
webhook_url = 'https://hooks.slack.com/YOUR/WEBHOOK/URL'
```

Select the vaults you want to report on:

```
vaults = [
    'apache-auth', 'apache-badbots', 'apache-botsearch',
    'apache-fakegooglebot', 'apache-modsecurity', 'apache-nohome',
    'apache-noscript', 'apache-overflows', 'apache-shellshock',
    'php-url-fopen', 'sshd'
]
```

## Usage

fail2slack should play nicely with Python v2 & v3. It can be run as a file or from the shell.


## Output

The current failed/banned counts will be compiled for all selected vaults and sent via the webhook.

```
vault-name
    Failed: CURRENT (TOTAL), Banned: CURRENT (TOTAL)
```

## Providing Feedback

Please reference our [code of conduct](./.github/CODE_OF_CONDUCT.md) and [contributing](./.github/CONTRIBUTING.md) guides.
