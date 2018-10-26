#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 14:36:03 2018

@author: Javier
"""


def linear(elem, lst):
    for i in range(len(lst)):
        if elem == lst[i]:
            return i
    
    return None