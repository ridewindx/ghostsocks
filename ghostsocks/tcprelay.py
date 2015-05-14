#!/usr/bin/python
# -*- coding: utf-8 -*-


import socket
from itertools import cycle
from .config import config


class TCPRelay(object):
    def __init__(self, eventloop, dns_resolver, is_server):
        self._eventloop = eventloop
        self._dns_resolver = dns_resolver
        self._is_server = is_server

        listen_

        family, socktype, proto, canonname, sockaddr = socket.getaddrinfo(listen_addr, listen_port, 0,
                                   socket.SOCK_STREAM, socket.SOL_TCP)

