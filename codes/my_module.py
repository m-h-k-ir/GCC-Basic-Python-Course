#نوشتن راهنما برای ماژول
"""
this is a test module!!!
"""

#تعریف متغیر داخل ماژول
a=10

#تعریف تابع داخل ماژول
def test():
    #نوشتن راهنما برای تابع
    """
    this is a test def!!!
    """
    #معرفی دستور جدید
    pass

def my_sum(a,b):
    return 2*a+2*b


#معرفی یکی از متغیرهای داخلی پایتون
# print(__name__)

#نوشتن تست برای ماژول
if __name__ == "__main__":
    print(my_sum(2,4))
    print(my_sum(3,4))
    print(my_sum(4,4))
    print(my_sum(2,8))
    print(my_sum(2,10))
    print(my_sum(10,10))