# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:24:34 2024

@author: Admin
"""
so_nguyen = int(input("Nhập một số nguyên dương n: "))
if so_nguyen > 0:
    S = 0
    for i in range(1, so_nguyen + 1):
        S = S + i
    print("Kết quả là: ", S)
else:
    print("Vui lòng nhập số nguyên dương")
