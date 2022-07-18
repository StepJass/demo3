# # class name():
# #     variables
# #     const
# #     functions
# #     str function
# #     del function
# #
# # object
# # ob=name()
# a=99
# class firstclass():
#     a,b=334,56
#     def f1(self):
#         print("hello")
#     def f2(self,a):
#         print(a)
#         print(self.a+self.b)
# ob=firstclass()
# ob.f1()
# ob.f2(12)
# print(ob.a)
# print(ob.b)
# print(a)


# Constructor
def __init__():
    pass

class Sec():
    a,b=99,1

    def f1(self):
        print("hello")
    def __init__(self,a,b):
        print(a+b)
        print(self.a+self.b)
        self.a=a
        print(a)
qq=Sec(56,78)  #object
qq.f1()
print(qq.a)


def __str__():
    pass

class erd():

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __str__(self):
        return "value of a %i and b is %s " %(self.a,self.b)

c=erd(4,'jjj')
print(c)

def __del__():
    pass


class erd():

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "value of a %i and b is %s " % (self.a, self.b)

    def __del__(self):
        print("deleted")

c = erd(4, 'jjj')
d=erd(4,'yyy')
print(c)
del c



class Test():
    a,b=10,20                  #class variables
    def f1(self):               #function
        print("gggggggggg")
    def __init__(self):            #constructor
        print("constructor")
    def __str__(self):           #string function
        return "yyyyyy"
    def __del__(self):                  #delete function
        print("destroyed")

cc=Test()                #call constructor
print(cc.a,cc.b)
print(cc)            #call string
cc.f1()           #call funtion
del cc               #call delete


hasattr()
setattr()
getattr()
delattr()