# fail2slack.py

[![Build Status](https://travis-ci.org/asdfdotdev/fail2slack.svg?branch=master)](https://travis-ci.org/asdfdotdev/fail2slack) [![codecov](https://codecov.io/gh/asdfdotdev/fail2slack/branch/master/graph/badge.svg)](https://codecov.io/gh/asdfdotdev/fail2slack) 

A Python package for sending fail2ban jail status updates to Slack.

## Compatibility

[![Python Version](https://img.shields.io/pypi/pyversions/fail2slack)](https://pypi.org/project/fail2slack) [![Module Version](https://img.shields.io/pypi/v/fail2slack)](https://pypi.org/project/fail2slack)

fail2slack is developed for, and tested with, recent versions of Python.

## Installation

```
pip install fail2slack
```

Install fail2slack using the Python package installer.

## Usage

```
usage: fail2slack [-h] [-w WEBHOOK] [-d DELIVERY] [-j JAILS [JAILS ...]]

optional arguments:
  -h, --help            show this help message and exit
  -w WEBHOOK, --webhook WEBHOOK
                        Slack webhook URL. Required if delivery method is 1.
  -d DELIVERY, --delivery DELIVERY
                        Delivery method: 0 = print, 1 = Slack webhook.
  -j JAILS [JAILS ...], --jails JAILS [JAILS ...]
                        Jails to include in status report. Required.
```

## Tests

For instructions on running test check out the [README](./test#readme).

## Contributing

If you'd like to contribute to fail2slack please reference our [code of conduct](./.github/CODE_OF_CONDUCT.md) and [contributing](./.github/CONTRIBUTING.md) guides.
