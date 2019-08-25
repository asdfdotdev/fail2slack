# fail2slack.py

[![Build Status](https://travis-ci.org/asdfdotdev/fail2slack.svg?branch=master)](https://travis-ci.org/asdfdotdev/fail2slack) [![codecov](https://codecov.io/gh/asdfdotdev/fail2slack/branch/master/graph/badge.svg)](https://codecov.io/gh/asdfdotdev/fail2slack)  [![downloads](https://img.shields.io/pypi/dm/fail2slack)](https://pypi.org/project/fail2slack)

fail2slack lets you send fail2ban jail status updates to Slack with ease.

## Compatibility

[![Python Version](https://img.shields.io/pypi/pyversions/fail2slack)](https://pypi.org/project/fail2slack) [![Module Version](https://img.shields.io/pypi/v/fail2slack)](https://pypi.org/project/fail2slack)

fail2slack is developed for and tested with recent versions of Python, including:

- 3.6, 3.7, 3.7.4, 3.8-dev

[Browse our build history at Travis-CI.](https://travis-ci.org/asdfdotdev/fail2slack)

## Installation

```
pip install fail2slack
```

Install fail2slack using the Python package installer.

[Dependencies for using fail2slack are available in the requirements file.](https://github.com/asdfdotdev/fail2slack/blob/master/requirements.txt)

## Usage

```
usage: __main__.py [-h] [-w WEBHOOK] [-d DELIVERY] [-j JAILS [JAILS ...]]
                   [-i IDENTIFIER]

optional arguments:
  -h, --help            show this help message and exit
  -w WEBHOOK, --webhook WEBHOOK
                        Slack webhook URL. Required if delivery method is 1.
  -d DELIVERY, --delivery DELIVERY
                        Delivery method: 0 = print, 1 = Slack webhook.
  -j JAILS [JAILS ...], --jails JAILS [JAILS ...]
                        Jails to include in status report. Required.
  -i IDENTIFIER, --identifier IDENTIFIER
                        Update identifier. STRING of identifier to use.
                        Default is hostname.
```

## Tests

For instructions on running test check out the [README](https://github.com/asdfdotdev/fail2slack/tree/master/test#readme).

[Test coverage reports are available on Codecov.](https://codecov.io/gh/asdfdotdev/fail2slack)

## Contributing

Feedback, bug reports, feature requests, and pull requests are welcome!

If you'd like to contribute to fail2slack please reference our [code of conduct](https://github.com/asdfdotdev/fail2slack/blob/master/.github/CODE_OF_CONDUCT.md) and [contributing](https://github.com/asdfdotdev/fail2slack/blob/master/.github/CONTRIBUTING.md) guides.
