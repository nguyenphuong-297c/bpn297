# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:56:13 2024

@author: Admin
"""
a = int(input("Nhập vào số nguyên a: "))
b = int(input("Nhập vào số nguyên b: "))
c = int(input("Nhập vào số nguyên c: "))
d = int(input("Nhập vào số nguyên d: "))
min_value = a
if b < a:
    min_value = b
if c < a:
    min_value = c
if d < a:
    min_value = d
print(min_value)
