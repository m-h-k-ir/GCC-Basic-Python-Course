#other operators
#number str
#and or not
#if block elif else
#if with int str
#exm password
#exm ticket price
#while break continue
#exm word game
#random.randint
#exm number game
#exm menu
#exm sum of numbers
#exm counter
#time.sleep()
#exm pattern


#عملگرها
#توضیحات و مثال ها در کلاس مطرح شده
# a=10
# b=20
# b=b+a
# print(b)
# b+=a
# print(b)

# ==
# >=
# <=
# >
# <
# !=


#شرط ساده
# a=10
# if "":
#     print("OK")
#     print("OK")
#     print("OK")
# print("end")


#شرط با حالت بندی
# a=8
# if a==10:
#     print("a:10")
# elif a>10:
#     print("a>10")
# elif a<10:
#     print("a<10")

# a=10
# if a==10:
#     print("OK")
# # elif a!=10:
# else:
#     print("!!!")

# a=9
# if a==10:
#     print("OK")
# elif a>10:
#     print("a>10")
# else:
#     print("!!!")

# t=100
# if t<=0:
#     print("ice")
# elif t<100:
#     print("water")
# else:
#     print("gas")


#شرط تو در تو
# a=0
# if a>=0:
#     if a==0:
#         print("000")
#     else:
#         print("pos")


#بازی حدس کلمه
# word="gcc"
# s=input()
# if s==word:
#     print(":)")
# else:
#     print(":(")


#بازی حدس عدد
# from random import randint
# import random
# n=random.randint(1,100)
# s=int(input())

# if s>n:
#     print(">")
# elif s<n:
#     print("<")
# else:
#     print("OK")
# print(n)


#دستورات کنترلی حلقه
# break
# continue


#مثال از حلقه
# a=10
# while a>0:
#     a-=1
#     if a==5:
#         continue
#     print(a)
#     # break
#     # if a==5:
#     #     break


#بازی حدس عدد پیشرفته
# from random import randint
# n=randint(1,100)
# print("Hi :)")
# print("Answer is a number from 1 to 100")
# print("Let's Go!!!")
# print(f"answer:{n}")

# try_num=5

# while try_num>0:
#     s=int(input())

#     if s>n:
#         print(">")
#     elif s<n:
#         print("<")
#     else:
#         print("OK")
#         break   
#     try_num-=1


#ساخت منو ساده
# a=10
# while True:
#     print("1) Hello")
#     print("2) print number")
#     print("3) exit")

#     menu=int(input("Enter menu number:"))

#     if menu==1:
#         print("Helloooooooooo")
#     elif menu==2:
#         print(f"a={a}")
#     elif menu==3:
#         print("Bye :(")
#         break
#     else:
#         print("only 1 to 3 :/")


#مثال محاسباتی از حلقه برای مجموع و میانگین
# summ=0
# count=0
# while True:
#     inn=int(input())
#     if inn==0:
#         break
#     summ+=inn
#     print(f"sum:{summ}")
#     count+=1
#     print(summ/count)
# print(f"total:{count}")


#مثال شمارنده تاخیر دار
# import time
# num=10
# while num>0:
#     print(num)
#     num-=1
#     time.sleep(1)


#چاپ یک الگوی ساده مثلثی
# num=10
# while num>0:
#     print(num*"* ")
#     num-=1