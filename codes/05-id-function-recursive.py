#in id is

#function:
#return tuple
#input default
#input name
#*args **kwargs
#local global var
#type of vars in funcs

#recursive:
#print n to 1
#factorial
#list sum


#در مورد آیدی و دوعملگر دیگر در کلاس کامل بحث شد
#بسیار بسیار مهم برای کار با ساختار داده ها


#برگرداندن بیش از یک خروجی از تابع
# def my_cal(a,b):
#     return a+b,a*b
# print(my_cal(2,3))
# s,z=my_cal(2,3)
# print(s,z)
# t=my_cal(2,3)
# print(t[0],t[1])


#مقدار پیشفرض برای ورودی های تابع
# def signup(name="moshtari mohtaram",printv2=False):
#     if printv2==False:
#         print(f"Hello {name}")
#     else:
#         print(f"Hello {name} :)")
# signup("ali",True)
# signup(printv2=True)


#ورودی تابع به تعداد دلخواه
# def sum_all(*args):
#     # print(args)
#     return sum(args)
# print(sum_all(1,2,3,4))


#ورودی برچسب دار تابع به تعداد دلخواه
# def print_info(**kwargs):
#     # print(kwargs)
#     for k,v in kwargs.items():
#         print(f"{k}:{v}")
# print_info(name="ali",age=25,city="isfahan")


#استفاده از همه نوع ورودی به صورت یکجا
# def test(a,b,c=False,*args,**kwargs):
#     print(a,b)
#     print(c)
#     print(args)
#     print(kwargs)
# test(1,2,True,5,6,name="ali")


#بررسی متغیرهای لوکال و گلوبال
# number=100
# def test():
#     # global number
#     # number=10
#     number_local=number+10
#     print(number_local)
# test()
# print(number)


#مشخص کردن نوع داده ورودی و خروجی تابع
# def to_upper(s:str) -> str:
#     # return 2*s
#     return s.upper()
# print(to_upper(2))
# print(to_upper("test"))


#بررسی کامل 3 مثال از تابع بازگشتی
#توضیحات تکمیلی در کلاس داده شد


#مثال چاپ اعداد نزولی
# def print_numbers(n):
#     print(n)
#     if n>0:
#         print_numbers(n-1)
# n=10
# print_numbers(n)


#مثال فاکتوریل
# def rec_fact(n):
#     if n>0:
#         return n*rec_fact(n-1)
#     else:
#         return 1
# n=4
# print(rec_fact(n))


#مثال جمع اعداد یک لیست
# def rec_sum(nums):
#     if len(nums)>1:
#         return nums[0]+rec_sum(nums[1:])
#     else:
#         return nums[0]
# nums=[1,5,7,10]
# print(rec_sum(nums))