# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:05:04 2024

@author: Student
"""

ngay=int(input("Nhập vào ngày: "))
thang=int(input("Nhập vào tháng: "))
nam=int(input("Nhập vào năm: "))
#Ngày/tháng/năm (Nhập 26 8 2024 thì xuất 26/8/2024)
print(f"{ngay}/{thang}/{nam}")
#Ngày/tháng/năm (Nhập 26 8 2024 thì xuất 26/8/24)
print(f"{ngay}/{thang}/{str(nam)[-2:]}")
#Ngày/tháng/năm (Nhập 26 8 2024 thì xuất 2024/8/26)
print(f"{nam}/{thang}/{ngay}")

#Ngược lại
ngay=int(input("Nhập vào ngày: "))
thang=int(input("Nhập vào tháng: "))
nam=int(input("Nhập vào năm: "))
print(f"{ngay}/{thang}/{nam}")
