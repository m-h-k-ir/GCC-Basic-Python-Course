#خلاصه جلسه
#lib:math
#int,float,bool,str
#+,-,*,/,//,%,**
#var:name,op,type,fstring,profile exam
#\n \t
#input:type,split
#print:sep,end


#استفاده از کتابخونه
# import math
# math.sqrt(2)

# from math import sqrt,pi
# sqrt(2)


#نکات اسامی متغیرها
# a=10
# a1=5
# A1=8
# a2=6
# user1_name=
# userName

#تبدیل type
# a=input()
# print(a*2)
# print(int(a)*2)


#نکات تکمیلی و اصلی این دو بخش در کلاس گفته شده


#انواع ورودی گرفتن
# name=input("Enter Your Name: ")
# last=input()
# age=input()

# name,last,age=input("Enter name-last-age:").split(sep="-")

# print(name)
# print(last)
# print(age)


#انواع نمایش خروجی و فرمت بندی
name="mohammad"
last="mohammadi"
age=35
# print(name,last,age,sep="-",end="\n\n")
# print(name,end=" ")
# print(last,end=" ")
# print(age)
# print(name,end="\n"+20*"-"+"\n")
# print(last,end="\n"+20*"-"+"\n")
# print(age)
s=f"salam {name} {last}\nage:{age}years old"
print(s)
