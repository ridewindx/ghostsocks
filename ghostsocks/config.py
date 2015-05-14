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

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     description=description,
                                     epilog='Online help: github.com/ghostsocks/ghostsocks')
    proxy_group = parser.add_argument_group('Proxy options')
    proxy_group.add_argument('-c', '--config', default='./config.py', help='path to config file')
    general_group = parser.add_argument_group('General options')
    args = parser.parse_args()
