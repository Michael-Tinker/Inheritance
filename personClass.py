class Person:

    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone
    
    def print_person(self):
        print("I am", self.__name)
        print("I live at", self.__address)
        print("My number is", self.__phone)

class Customer(Person):
    def __init__(self,name,address,phone,cust_num,mailing):
        
        Person.__init__(self,name,address,phone)

        self.__cust_num = cust_num
        self.__mail = mailing

    def print_person(self):
        Person.print_person(self)
        print("My cust_num is", self.__cust_num)
        if self.__mail == True:
            print("On the mailing list")
        else:
            print("Not on the mailing list")

