#!/usr/bin/python
# -*- coding: utf-8 -*-


import select
from select import EPOLLERR, EPOLLET, EPOLLHUP, EPOLLIN, EPOLLMSG, EPOLLONESHOT,\
                   EPOLLOUT, EPOLLPRI, EPOLLRDBAND, EPOLLRDNORM, EPOLLWRBAND, EPOLLWRNORM
import errno
from .log import log


class EventLoop(object):
    def __init__(self):
        self._epoll = select.epoll()

        self._fd_to_f = {}
        self._handlers = []
        self._handlers_to_remove = []
        self._in_handling = False

    def poll(self, timeout=None):
        return [(self._fd_to_f[fd], fd, event) for fd, event in self._epoll.poll(timeout)]

    def add(self, f, mode):
        fd = f.fileno()
        self._fd_to_f[fd] = f
        self._epoll.register(fd, mode)

    def remove(self, f):
        fd = f.fileno()
        del self._fd_to_f[fd]
        self._epoll.unregister(fd)

    def modify(self, f, mode):
        fd = f.fileno
        self._epoll.modify(fd, mode)

    def add_handler(self, handler):
        self._handlers.append(handler)

    def remove_handler(self, handler):
        self._handlers.remove(handler)
        if self._in_handling:
            self._handlers_to_remove.append(handler)
        else:
            self._handlers.remove(handler)

    def run(self):
        while self._handlers:
            try:
                events = self.poll(1)
            except (OSError, IOError) as e:
                if getattr(e, 'errno', None) in (errno.EPIPE, errno.EINTR):
                    # EPIPE: Happens when the client closes the connection
                    # EINTR: Happens when received a signal
                    log.debug('poll: %s', e)
                else:
                    log.exception('poll: %s', e)
                continue

            self._in_handling = True

            for handler in self._handlers:
                try:
                    handler(events)
                except (OSError, IOError) as e:
                    log.exception('poll: %s', e)

            for handler in self._handlers_to_remove:
                self._handlers.remove(handler)
            self._handlers_to_remove = []

            self._in_handling = False
