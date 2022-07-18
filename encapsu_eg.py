# __a  # private variable

class A():
    __a=34
    def f1(self):
        print(self.__a)

ob=A()
ob.f1()
# print(ob.__a)     invalid

# def __ff():       private function

class first:
    def __ff(self):
        a=34
        print(a)
    def ff2(self):
        self.__ff()
ob=first()
# ob.__ff()  invalid

# Bean classes  GetterSetter
class Emp:
    __empid=11

    def setEid(self,empid):
        self.__empid=empid
    def getEid(self):
        return self.__empid
ee=Emp()
print(ee.getEid())
ee.setEid(78)
print(ee.getEid())

class A:
    num1,num2=10,20

class B:
    a=A()
    def add(self):
        # a=A()
        print(self.a.num1+self.a.num2)
    def mul(self):
        # a=A()
        print(self.a.num1*self.a.num2)
ob=B()
ob.add()
ob.mul()
