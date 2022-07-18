# a=10
# print(a/0)

# try:
#     exceptional code
# except:
#     alternate code
# except ZeroDivisionError:
#     al
# except ZeroDivisionError as qw:
#     print("fsdfs")
from NewException import NegativeAgeException

n=int(input("Enter value"))
def f1():
    try:
        a=10
        print(a/n)
        print("hello"+"hhh")
    except (ZeroDivisionError,TypeError) as qw:
        print(qw)
    else:
        print("hello")
f1()

def f1():

        a=10
        print(a/n)
        print("hello"+"hhh")
try:
    f1()
except (ZeroDivisionError, TypeError) as qw:
    print(qw)
else:
    print("hello")

try:
    a=10
    print(a/n)
    print("hello"+"hhh")
except (ZeroDivisionError,TypeError) as qw:
    print(qw)
else:
    print("hello")
finally:
    print("finally")

def m1():
    try:
        return 9
    except:
        return 20
print(m1())


# raise ZeroDivisionError("divide by zero")
age=int(input("enter ur age"))
if age <0:
    raise NegativeAgeException("Enter valid age")
else:
    print("eligible")