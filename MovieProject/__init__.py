#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 11:09:56 2017

@author: Julian
"""
import sys
from os.path import dirname, join, abspath


dir =  dirname(abspath(__file__)).replace("\\","/")
root = dir[:dir.rfind('/')]
if root not in sys.path:
    sys.path.insert(0, join(root))
