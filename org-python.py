#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import orgpython
import doctest
from time import time

class Regex(object):
    newline = re.compile(r'^$')
    heading = re.compile(r'^(?P<level>\*+)')
