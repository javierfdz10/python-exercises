#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 14:36:03 2018

@author: Javier
"""


def linear(element, lst):
    for i in range(len(lst)):
        if element == lst[i]:
            return i
    
    return None