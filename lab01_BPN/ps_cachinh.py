# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:15:36 2024

@author: Admin
"""
nhap = input("Nhập hình: ")
"n" == "Hình chữ nhật"
"v" == "Hình vuông"
"t" == "Hình tròn"
if nhap == "n":
    print("Tính P và S của hình chữ nhật")
    a = int(input("Nhập chiểu rộng = "))
    b = int(input("Nhập chiểu dài = "))
    P = (a + b) * 2
    S = a * b
    print(f"Kết quả {P}  {S} ")
elif nhap == "v":
    print("Tính P và S của hình vuông")
    a = int(input("Nhập độ dài của cạnh = "))
    P = a * 4
    S = pow(a, 2)
    print(f"Kết quả {P}  {S} ")
else:
    r = int(input("Nhập bán kính đường tròn: "))
    r = int(input("Nhập bán kính đường tròn: "))
print("Chu vi hình tròn: ",r*2*3.14)
print("Diện tích hình tròn: ",r*r*3.14)
