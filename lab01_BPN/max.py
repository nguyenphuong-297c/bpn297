# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:58:11 2024

@author: Admin
"""
a = int(input("Nhập vào số nguyên a: "))
b = int(input("Nhập vào số nguyên b: "))
c = int(input("Nhập vào số nguyên c: "))
max_value = a
if max_value < b:
    max_value = b
if max_value < c:
    max_value = c
print(max_value)
