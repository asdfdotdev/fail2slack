<p align="center"><img src="https://raw.githubusercontent.com/asdfdotdev/fail2slack/development/.github/images/logo.png" width="400"></p>

![Unit Tests](https://github.com/asdfdotdev/fail2slack/workflows/Unit%20Tests/badge.svg) [![downloads](https://img.shields.io/pypi/dm/fail2slack)](https://pypi.org/project/fail2slack)

fail2slack lets you send fail2ban jail status updates to Slack with ease.

## Compatibility

[![Python Version](https://img.shields.io/pypi/pyversions/fail2slack)](https://pypi.org/project/fail2slack) [![Module Version](https://img.shields.io/pypi/v/fail2slack)](https://pypi.org/project/fail2slack)

fail2slack is developed for and tested with recent versions of Python, including:

- 3.9, 3.10, 3.11, 3.12, 3.13

[Browse our build history at GitHub.](https://github.com/asdfdotdev/fail2slack/actions)

## Installation

```
pip install fail2slack
```

Install fail2slack using the Python package installer.

[Dependencies for using fail2slack are available in the requirements file.](https://github.com/asdfdotdev/fail2slack/blob/main/requirements.txt)

## Usage

```
usage: __main__.py [-h] [-w WEBHOOK] [-d DELIVERY] [-j JAILS [JAILS ...]] [-i IDENTIFIER]

options:
  -h, --help            show this help message and exit
  -w WEBHOOK, --webhook WEBHOOK
                        Slack webhook URL. Required if delivery method is 1.
  -d DELIVERY, --delivery DELIVERY
                        Delivery method: 0 = print, 1 = Slack webhook.
  -j JAILS [JAILS ...], --jails JAILS [JAILS ...]
                        Jails to include in status report. Required.
  -i IDENTIFIER, --identifier IDENTIFIER
                        Update identifier. STRING of identifier to use. Default is hostname.
```

### Result

<p style="padding-bottom:20px"><img src="https://raw.githubusercontent.com/asdfdotdev/fail2slack/development/.github/images/screenshot.png" width="350"></p>

## Tests

For instructions on running test check out the [README](https://github.com/asdfdotdev/fail2slack/tree/main/test/#readme).

## Contributing

Feedback, bug reports, feature requests, and pull requests are welcome!

If you'd like to contribute to fail2slack please reference our [code of conduct](https://github.com/asdfdotdev/fail2slack/blob/main/.github/code_of_conduct.md) and [contributing](https://github.com/asdfdotdev/fail2slack/blob/main/.github/contributing.md) guides.
