'''
a=10 # int
b=10.5 # float
c='123' # string
d=False # boolean
e=10+20j # complex


print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

'''
# a=10

# print(dir(int))

# name="Oti Edema"

# # print(type(name))
# print(dir(name))
# # print(name.split())


# Python everything is an object

# List, Tuple, Set, Dict

# List/Array: collection of elements ordered

# l1=[1,"Ram",False] 
# l2=[1,2,3,4,5]
# l3=[]
# print(type(l1))
# print(l1.__len__())
# # l1.insert(1,"Rahul")
# print(dir(list))
# s="Gaurav Pathak"
# print(dir(s))
# print(l1.__repr__())
# print(l1.__str__())

# print(s)

# function independent

# method inside class 

# def add(x,y):
#     return x+y

# sum=add(1,9)
# print(sum)

# class student:
#     def add(self, x,y):
#         self.x=x
#         self.y=y
#         return x+y
    

# s1=student()
# s2=student()
# s3=student()
# print(s1.add(2,3))
# print(s2.add(5,4))

#l1=[10,20,30,40]
# print(l1[1])

# print(dir(l1))

# print(l1)

# l1.pop()

# print(l1)

# l1.pop()

# print(l1)

# l1=[10,20,30,40]
# l1.remove(20)
# l1.remove(30)
# print(l1)


# Tuple a collection of elements, hetrogeneous type, ordered. Immutable list

# l=[10,20,"abc", True]
# l[2]="xyz"
# print(l)

# t=(10,20,"abc", True)
# t[2]="xyz"
# print(t)

#immutability: primitvite data types are immutable in nature: int, float, string, bool

# a=10
# b=10
# c=10
# print(id(a))
# print(id(b))
# print(id(c))
# l1=[10,20,30,40]
# l2=[10,20,30,40]
# print(id(l1))
# print(id(l2))

# t1=(1,2,3)
# t2=(1,2,3)
# print(id(t1))
# print(id(t2))
# print(t1 is t2)

# tuple is nothing but a immutable list

# t=(1,"Naveen",2,True, "Naveen")
# # print(dir(tuple))

# print(t.count(True))
# print(t.index(True))

# l1=[1,2,3,4,2,5]
# print(l1)
# duplication is not allowed, unordered
# s1={10,20,"Rahul",True,"Chaitanya", "Rahul", 20}
# s1.add("lwplabs")
# s1.add("Gaurav")
# print(s1)
# # # s1.discard("Rahul")
# # s1.pop()
# # # s1.pop()
# s1.remove("Chaitanya")
# print(s1)
# # print(dir(set))

# dict => dictionary, map, hash-map key: value pairs
# [](){}
# d={}
# s=set()
# print(type(d))
# print(type(s))
# d1={"Names":["Gaurav","Rahul","Kunal"],"Branches":{"IT","CS","Mech"},"Roll_No":30,(1,2):{"abc":"xyz"}}

# print(d1.get("Names"))
# print(d1.fromkeys("Branches"))
# d1["Name"]="Oti"
# d1["Branch"]="CS"
# print(d1)
# a=10.2
# b=[10,20,30]
# s={10,20,30}
# print(hash(s))

# only immutable data types which are int, float, str, bool, tuple can be key of a dictionary
# values can be anything

# print(dir(dict))

# k=("name","roll_no")
# v="gaurav"
# d=dict.fromkeys(k,v)
# print(d)

# operators in python

#   - Airthemtic operator (Add, Sub, mul, div)
#   - logical operator
#   - membership operator
#   - bitwise operator 
#   - identity operator

# a=20
# b=10

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)

# a= True
# b= True

# print(a or b)

# print(a and b)

# print(not a)

# in , not in

# l=[10,20,30,"India", True, "USA"]

# print("India" not in l)

# a=10
# b=20

# print( a is b)

# comparison opeartor >=, ==, <=

# indexing and slicing

l=[10,20,30, "India", "Happy", "USA", True] #[30, "Happy", True]

# print(l[8])
# print(l[-6])
#6th index
# print(l[1:7:1]) # 20,30, "India", "Happy", "USA", True
# print(l[1:7:2]) # 20, "India", "USA"
# print(l[2:8:3]) # 30, "USA"

# print(l[2:7:2]) # 30, "Happy",True
#         1, 7-1=6, 3
# print(l[1:7:3]) # 20, "Happy"

# print(l[-1:-7:1])

# conditions
# loops
# functions
# exception handelling
# packages 
# oops
# lambda