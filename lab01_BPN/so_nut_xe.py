# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:14:21 2024

@author: Student
"""
so_xe = int(input("Nhập số xe (4 chữ số): "))
tong_cac_chu_so = sum(int(chu_so) for chu_so in str(so_xe))
so_nut = tong_cac_chu_so % 10
if so_xe < 1000 or so_xe > 9999:
  print("Số xe phải có 4 chữ số.")
else:
  print(f"Số nút của biển số xe {so_xe} là:", so_nut)   