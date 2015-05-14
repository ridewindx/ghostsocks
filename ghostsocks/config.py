#!/usr/bin/python
# -*- coding: utf-8 -*-


import argparse
from functools import partial


def _addr_ports(multiple, string):
    addr, ports = string.split(':')
    ports = [p for p in ports.split(',') if p]
    if multiple:
        return addr, tuple(ports)
    else:
        return addr, ports[0]


config = argparse.Namespace()


def parse_args(is_server):

    if is_server:
        description = 'ghostsocks server'
    else:
        description = 'ghostsocks client'

    description += '\n\nA fast tunnel proxy that helps you bypass firewalls'

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                     description=description,
                                     epilog='Online help: github.com/ghostsocks/ghostsocks',
                                     add_help=False)

    proxy_group = parser.add_argument_group('Proxy options')
    proxy_group.add_argument('-c', '--config', default='./config.py', help='path to config file')
    if is_server:
        proxy_group.add_argument('-l', '--listen', type=partial(True, _addr_ports), default='0.0.0.0:9000',
                                 help='listening address and port(s), e.g., 138.128.200.120:9000,9080')
    else:
        proxy_group.add_argument('-l', '--listen', type=partial(True, _addr_ports), default='0.0.0.0:1080',
                                 help='listening address and port(s), e.g., 127.0.0.1:1000,1080')
        proxy_group.add_argument('-r', '--remote', type=partial(False, _addr_ports), default='0.0.0.0:9000',
                                 help='remote address and port, e.g., 138.128.200.120:9000')
    proxy_group.add_argument('-p', '--password', nargs='+', help='validation passwords, one-one mapping to ports')
    proxy_group.add_argument('-e', '--encryption', default='aes-256-cfb', help='encryption method')
    proxy_group.add_argument('-t', '--timeout', type=int, default=300, help='timeout in seconds')
    proxy_group.add_argument('-f', '--fastopen', action='store_true', help='use TCP_FASTOPEN, requires Linux 3.7+')

    general_group = parser.add_argument_group('General options')
    general_group.add_argument('-d', '--daemon', choices=['start', 'stop', 'restart'], help='operate in daemon')
    general_group.add_argument('--pid-file', dest='pidfile', help='pid file in daemon')
    general_group.add_argument('--log-file', dest='logfile', help='log file in daemon')
    general_group.add_argument('-v', '--verbose', action='count', help='verbose logging level')
    general_group.add_argument('--user', help='user to run as')
    general_group.add_argument('--version', action='version', version='%(prog)s 1.0')
    general_group.add_argument('-h', '--help', action='help', help='show this help message and exit')

    global config
    config = parser.parse_args()
