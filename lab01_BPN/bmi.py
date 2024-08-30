# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:07:39 2024

@author: Student
"""
can_nang = float(input("Nhập cân nặng (kg): "))
chieu_cao = float(input("Nhập chiều cao (m): "))
bmi = can_nang / (chieu_cao * chieu_cao)
print (" Kiểm tra sức khỏe BMI là: ", bmi)
