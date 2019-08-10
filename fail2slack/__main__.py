#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# fail2slack
#
# Copyright 2018-present Chris Carlevato (https://github.com/asdfdotdev)
# License http://www.gnu.org/licenses/gpl-2.0.html
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; version 2.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

import sys
import jails
from settings import Settings
from delivery import Delivery


def main():
    settings = Settings()
    settings.process_args(sys.argv)
    delivery = Delivery(settings)

    delivery.output(
        jails.get_jails_status(
            settings.get_jails()
        )
    )


if __name__ == '__main__':
    main()