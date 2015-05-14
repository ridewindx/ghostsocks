#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import argparse

from .log import log


def parse_args(is_server):

    if is_server:
        description = 'ghostsocks server'
    else:
        description = 'ghostsocks client'

    description += '\n\nA fast tunnel proxy that helps you bypass firewalls'

    parser = argparse.ArgumentParser(description=description)
    args = parser.parse_args()
