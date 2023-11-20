# # CLASSES:
# class Point():
#     def __init__(self, input1, input2):
#         self.x = input1
#         self.y = input2
# p = Point(2,5)
# print(p.x)
# print(p.y)

# class Flight():        
#     def __init__(self, capacity):
#         self.capacity= capacity
#         self.passengers = []

#     def add_passengers(self,names):
#         if not self.open_seats():
#             return False
#         self.passengers.append(names)
#         return True
    
#     def open_seats(self):
#         return self.capacity - len(self.passengers)
    
# flight = Flight(4)

# people = ["harry","ginny","uhfh","uohd","hhh"]
# for person in people:
#     success = flight.add_passengers(person)
# if success:
#     print(f"Added {person} to flight successfully")
# else:
#     print(f"No available seat for {person}")


# # DECORATORS: --> (FUNCTIONAL PROGRAMMING PARADIGM) where function are themselves values
# # THE FUNCTION WHICH TAKES A FUNCTION MODIFIES IT BY ADDING SOME ADDITIONAL CAPABILITIES TO IT,AND THE GIVES US BACK SOME O/P
# def announce(f):
#     def wrapper():
#         print("About to run the program...")
#         f()
#         print("Done with the function.")
#     return wrapper
# @announce
# # To add the decorator we use @ also it is called function is wrapped by using @
# def hello():
#     print("Hello world!")

# hello()
# #  USE OF A DECORATOR: If we want only some specific fun need to be run when the user logged in the we can use DECORATOR in the web apllication

 

# NOTE: Sort function will not apply for dictionary in that case we will pass the sort function
# people = [
#     {"name":"aaa", "house":"hdhdh"},
#     {"name":"nid", "house":"zsokncn"},
#     {"name":"uji2pdok", "house":"slljc"}
# ]

# # def f(person):
# #     return person["house"]
# # people.sort(key=f)
# # Instead of using the function like this we can use lambda in order to pass the value

# people.sort(key=lambda person:person["name"])
# print(people)


# EXCEPTIONS:
import sys
# In case we give words instead of values as i/p then we will get ValueError to overcome this we use try and exception in aking the i/p also
try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Invalid input.")
    sys.exit(1)

try:
    result = x/y
except ZeroDivisionError:
    print("Cannot divide by 0.")
    sys.exit(1)
    # status code of 1 indicates that something went wrong in the program

print(f"{x} / {y} is {result}")