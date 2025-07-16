#while in while
#basic function
#str
#slicing
#lower upper capitalize title swapcase
#count startswith endswith find rfind index replace
#split rsplit splitlines join
#strip lstrip rstrip center ljust rjust
#isalnum isalpha isdigit isnumeric isspace islower isupper istitle
#format


#حلقه تو در تو
# j=0
# while j<=4:
#     i=1
#     while i<=5:
#         print(f"{i+5*j} ",end="")
#         # print(i+5*j,end=" ")
#         i+=1
#     print()
#     j+=1


#تعریف تابع
# def my_func(x:int) -> int:
#     x*=5
#     print(f"my_func running with number {x}")

# def my_pow(x,y):
#     return x**y

# my_func(10)
# a=my_pow(2,4)*2
# print(a)
# print(my_pow(5,2))
# my_func(10.5)


#بررسی برش رشته
# s="salam inja gcc hast"
# print(s[6])
# print(len(s))
# print(s[0:5])
# ss=s[0:5]
# print(s[0:15:2])
# print(s[::2])
# print(s[:5])
# print(s[::-1])


#بررسی متدهای رشته
# s="nlgn DUjkn kIo55 9s9KHB"
# print(s.upper())
# print("salam".upper())
# print(s.swapcase())
# print(str(123).upper())

# print(s.count("n"))
# print(s.startswith("nlg"))
# print(s.endswith("B"))
# print(s.find("n"))
# print(s.rfind("n"))
# print(s.find("mkfykm"))
# # print(s.index("mkfykm"))
# print(s.replace("n","m"))
# print(s.replace(" ",""))

# print(s.split(sep="n"))
# print(s.rsplit(sep="n"))

# s="salam\nchetori\n?"
# print(s.splitlines())

# s="25272"
# print(s.center(10,"-"))
# print(s.ljust(10,"-"))
# print(s.rjust(10,"-"))

# print(s.isdigit())

# s="name:{}\nage:{}"
# print(s.format("ali",25))


#نمونه بررسی کاراکتر به کاراکتر رشته
# s="nlgn DUjkn kIo55 9s9KHB"
# i=0
# s_num=""
# s_low=""
# s_upp=""
# while i<len(s):
#     if s[i].isdigit():
#         s_num+=s[i]
#     elif s[i].islower():
#         s_low+=s[i]
#     elif s[i].isupper():
#         s_upp+=s[i]
#     i+=1
# print(s_num)
# print(s_low)
# print(s_upp)

# s_without_num=""
# i=0
# while i<len(s):
#     if not s[i].isdigit():
#         s_without_num+=s[i]
#     i+=1
# print(s_without_num)