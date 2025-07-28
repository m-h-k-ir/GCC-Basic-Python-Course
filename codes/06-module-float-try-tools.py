#module
#from * import *
#import * as *
#__name__ == "__main__"
#vars in module
#change module vars
#del vars

#Docstring def module

#float64
#telorance for ==
#Decimal module

#try except

#map
#i for i
#zip enumerate

# import math
# math.sin()
# from math import sin,pi
# sin()
# import math as m
# m.sin()

#بررسی متغیر داخل ماژول
# import math
# print(math.pi)
# math.pi=4
# print(math.pi)
# math.pii=5
# print(math.pii)
# del(math.pi)
# print(math.pi)

#بررسی بقیه ویژگی های ماژول و ماژول نویسی
# import my_module as m
# # from my_module import my_sum
# print(m.a)
# m.test()


#بررسی کامل ساختار و محدودیت های اعداد اعشاری در کلاس و نکات مربوط به آن

#معرفی ماژول دسیمال
# from decimal import Decimal
# a=Decimal("4524523734425.1788872727272782545455327825772")
# b=Decimal("277827522587.272257872736572735")
# print(a+b)


#معرفی ابزار کنترل ارورها در قالب دو مثال
# while True:
#     try:
#         a=input()
#         if a=="exit":break
#         a=int(a)
#     except:
#         print("try again!!!")
#         continue
#     print(1300+a)

# while True:
#     try:
#         a,b=input().split()
#         print(int(a)/int(b))
#     except:
#         print("try again!!!")


#معرفی تابع مپ
# a=[1,5,-5,-7,0]
# b=map(abs,a)
# print(b)
# # for i in b:
# #     print(i)
# print(list(b))

# a,b,c=map(int,input().split())
# print(a+b+c)
# # print(list(a))


#معرفی حلقه تک خطی برای ساخت لیست
# a=[i*i for i in range(10)]
# print(a)


#معرفی توابع زیپ و شماره گذاری

# names=["Ali","Sara","Reza"]
# last_names=["Ahmadi","Mohammadi","Karimi"]
# ages=[20,25,30]
# for name,last,age in zip(names,last_names,ages):
#     print(f"{last} {name}: {age}")
# for a,b in zip(range(10),range(10,20)):
#     print(a,b)

# names=["Ali", "Sara", "Reza"]
# for i in range(len(names)):
#     print(f"{i+1}:{names[i]}")
# for i,name in enumerate(names,start=1):
#     print(f"{i}:{name}")