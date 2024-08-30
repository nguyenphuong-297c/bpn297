# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 19:09:07 2024

@author: Student
"""
a= float(input(" Nhập giá trị của a(a<>0): "))
b= float(input(" Nhập giá trị của b: "))
c = float(input(" Nhập giá trị của c: "))
delta=b**2-4*a*c
if delta <0:
    print(" Phương trình vô nghiệm ")
if delta == 0:
    print(" Phương trình có nghiệm kép x1=x2=," -b/(2*a))
if delta >0:
    print(" Phương trình có hai nghiệm x1= ", (-b+ delta**0.5)/2*a, " x2 =", (-b- delta**0.5)/2*a  )
    
