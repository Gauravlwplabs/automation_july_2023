# '''
# a=10 # int
# b=10.5 # float
# c='123' # string
# d=False # boolean
# e=10+20j # complex


# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))

# '''
# # a=10

# # print(dir(int))

# # name="Oti Edema"

# # # print(type(name))
# # print(dir(name))
# # # print(name.split())


# # Python everything is an object

# # List, Tuple, Set, Dict

# # List/Array: collection of elements ordered

# # l1=[1,"Ram",False] 
# # l2=[1,2,3,4,5]
# # l3=[]
# # print(type(l1))
# # print(l1.__len__())
# # # l1.insert(1,"Rahul")
# # print(dir(list))
# # s="Gaurav Pathak"
# # print(dir(s))
# # print(l1.__repr__())
# # print(l1.__str__())

# # print(s)

# # function independent

# # method inside class 

# # def add(x,y):
# #     return x+y

# # sum=add(1,9)
# # print(sum)

# # class student:
# #     def add(self, x,y):
# #         self.x=x
# #         self.y=y
# #         return x+y
    

# # s1=student()
# # s2=student()
# # s3=student()
# # print(s1.add(2,3))
# # print(s2.add(5,4))

# #l1=[10,20,30,40]
# # print(l1[1])

# # print(dir(l1))

# # print(l1)

# # l1.pop()

# # print(l1)

# # l1.pop()

# # print(l1)

# # l1=[10,20,30,40]
# # l1.remove(20)
# # l1.remove(30)
# # print(l1)


# # Tuple a collection of elements, hetrogeneous type, ordered. Immutable list

# # l=[10,20,"abc", True]
# # l[2]="xyz"
# # print(l)

# # t=(10,20,"abc", True)
# # t[2]="xyz"
# # print(t)

# #immutability: primitvite data types are immutable in nature: int, float, string, bool

# # a=10
# # b=10
# # c=10
# # print(id(a))
# # print(id(b))
# # print(id(c))
# # l1=[10,20,30,40]
# # l2=[10,20,30,40]
# # print(id(l1))
# # print(id(l2))

# # t1=(1,2,3)
# # t2=(1,2,3)
# # print(id(t1))
# # print(id(t2))
# # print(t1 is t2)

# # tuple is nothing but a immutable list

# # t=(1,"Naveen",2,True, "Naveen")
# # # print(dir(tuple))

# # print(t.count(True))
# # print(t.index(True))

# # l1=[1,2,3,4,2,5]
# # print(l1)
# # duplication is not allowed, unordered
# # s1={10,20,"Rahul",True,"Chaitanya", "Rahul", 20}
# # s1.add("lwplabs")
# # s1.add("Gaurav")
# # print(s1)
# # # # s1.discard("Rahul")
# # # s1.pop()
# # # # s1.pop()
# # s1.remove("Chaitanya")
# # print(s1)
# # # print(dir(set))

# # dict => dictionary, map, hash-map key: value pairs
# # [](){}
# # d={}
# # s=set()
# # print(type(d))
# # print(type(s))
# # d1={"Names":["Gaurav","Rahul","Kunal"],"Branches":{"IT","CS","Mech"},"Roll_No":30,(1,2):{"abc":"xyz"}}

# # print(d1.get("Names"))
# # print(d1.fromkeys("Branches"))
# # d1["Name"]="Oti"
# # d1["Branch"]="CS"
# # print(d1)
# # a=10.2
# # b=[10,20,30]
# # s={10,20,30}
# # print(hash(s))

# # only immutable data types which are int, float, str, bool, tuple can be key of a dictionary
# # values can be anything

# # print(dir(dict))

# # k=("name","roll_no")
# # v="gaurav"
# # d=dict.fromkeys(k,v)
# # print(d)

# # operators in python

# #   - Airthemtic operator (Add, Sub, mul, div)
# #   - logical operator
# #   - membership operator
# #   - bitwise operator 
# #   - identity operator

# # a=20
# # b=10

# # print(a+b)
# # print(a-b)
# # print(a*b)
# # print(a/b)
# # print(a//b)

# # a= True
# # b= True

# # print(a or b)

# # print(a and b)

# # print(not a)

# # in , not in

# # l=[10,20,30,"India", True, "USA"]

# # print("India" not in l)

# # a=10
# # b=20

# # print( a is b)

# # comparison opeartor >=, ==, <=

# # indexing and slicing

# # l=[10,20,30, "India", "Happy", "USA", True] #[30, "Happy", True]

# # print(l[8])
# # print(l[-6])
# #6th index
# # print(l[1:7:1]) # 20,30, "India", "Happy", "USA", True
# # print(l[1:7:2]) # 20, "India", "USA"
# # print(l[2:8:3]) # 30, "USA"

# # print(l[2:7:2]) # 30, "Happy",True
# #         1, 7-1=6, 3
# # print(l[1:7:3]) # 20, "Happy"

# # print(l[-1:-7:1])

# # conditions
# # loops
# # functions
# # exception handelling
# # packages 
# # oops
# # lambda


# # l1=[10,20,30,40,50,60,70]

# # # print(l1[5:1:-1]) (begin index: end index: step)

# # # step is +ve : 1, 2, 3 endindex-1
# # # step is -ve : -1, -2, -3 endindex+1

# # # print(7,2,-1)

# # # 7th index 
# # # end+1 2+1 =3

# # print(l1[7:2:-1])


# # Conditions

# # if you want that a particualr action is perfromed only when a particualr condition is matching:

# # #even number, odd number and prime number
# # a=3
# # if a%2 == 0:
# #     print("Provided number is even number")
# # elif a%2 != 0:
# #     print("provided number is an odd number")
# # else:
# #     print("provided number is an prime number")

# # honeymoon_destinations=input("Enter your honeymoon destination: ")

# # if honeymoon_destinations == "":
# #     print("It is very common in indian middle class to go on honeymmon")
# # elif honeymoon_destinations == "404":
# #     print("It's overrated due to high markting")
# # elif honeymoon_destinations == "Kerala":
# #     print("It's god's own country..it's great!")
# # else:
# #     print("These are good but not so much famous")

# # loops: executing block of statements for each element from  a collection of elements/ sequential data

# # loop: collection list,set, range, dict

# # for loop

# # l1=[10,20,30,50,40] # iteration
# # # list, dict, set, tuple , range
# # a=10 # iterate over a single element
# # l1=[10,20,30,40]
# # s1={20,"name",True} # order is not important, unordered
# # d1={"Name":"Gaurav","Work":"Trainer"}
# # a=3
# # for x in range(3,10,2):
# #     if a%x==0:
# #         print("number is not a prime number")

# # for x in range(3,10,2):
# #     print(x)
# # i=0
# # while i<=10:
# #     print(i)
# #     i=i+1

# # for loop and while loop

# # [10,20,30,40]
# # {"Name":"Gaurav", "Class":"10th"}


# # a=10
# # b=20

# # print(a+b)
# # print(a-b)
# # print(a*b)
# # c=20
# # d=30
# # print(c+d)

# # def add(x,y):
# #     print(x+y)

# # add(10,20)
# # add(20,30)
# # def arth(x,y):
# #     if ops=="add":
# #         print(x+y)
# #     elif ops=="sub":
# #         print(x-y)
# #     elif ops == "mul":
# #         print(x*y)
# #     else:
# #         print(x//y)

# # ops="sub"
# # a=20
# # b=30
# # arth(a,b)

# # def add(*args):
# #     sum=0
# #     for x in args:
# #         sum=sum+x
# #     print(sum)

# # add(10,20)
# # add(10,20,30)
# # add(10,20,30,40)

# # def add(**kwargs):
# #     sum=0
# #     for x in kwargs.values():
# #         sum=sum+x
# #     print(sum)

# # # method overloading not available in python


# # add(a=10,b=20)
# # add(a=10,b=20,c=30)
# # add(a=10,b=20,c=30,d=40)

# # exception hanedlling

# # a=10
# # b=2

# # try:
# #     print(a/b)
# # except ZeroDivisionError:
# #     print("Please provide non-zero number as denominator")
# # except TypeError:
# #     print("Please only provide integers")
# # except Exception as err:
# #     print(f"Error is: {err}")
# # finally:
# #     print("program execution stopped")


# # collection of modules is called packages

# # python provides you some pre-written codes that you can directly use into your code and you do not have to write the functionality from scratch


# # modules: os module

# # import os

# # print(os.system("ls -ltr"))

# # OOPS => object oriented programming

# class Employees:
#     def __init__(this, EmpID, branch, Desgination):
#         this.emp_id=EmpID
#         this.branch=branch
#         this.designation=Desgination
#     def display_info(this):
#         print(f"{this.emp_id}..{this.branch}")

# Rahul=Employees(1, "IT", "Solution Architect")

# Kiran=Employees(2, "Admin", "Controller")

# Rahul.display_info()
# Kiran.display_info()

# # class method, static method, instance method
# # local variables, class varaibles, instance variables

d={"Names":[{"x":"y","z":{"e":"f"}}], "Trainer":"Role"}

print(d["Names"][0]["z"]["e"])