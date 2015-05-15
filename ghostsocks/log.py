#!/usr/bin/python
# -*- coding: utf-8 -*-


import logging as log

def config_log(filename, level=log.WARNING, filemode='a'):
    log.basicConfig(filename=filename, filemode=filemode, level=level,
                    format='%(asctime)s %(levelname)s: %(message)s [tid:%(thread)d][%(filename)s,%(lineno)d]')
