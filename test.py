# str = 'Hello World!'

# print (str)          # Prints complete string
# print (str[0])       # Prints first character of the string
# print (str[2:5])     # Prints characters starting from 3rd to 5th
# print (str[2:])      # Prints string starting from 3rd character
# print (str * 2)      # Prints string two times
# print (str + "TEST") # Prints concatenated string

# list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
# tinylist = [123, 'john']

# print (list)          # Prints complete list
# print (list[0])       # Prints first element of the list
# print (list[1:3])     # Prints elements starting from 2nd till 3rd 
# print (list[2:])      # Prints elements starting from 3rd element
# print (tinylist * 2)  # Prints list two times
# print (list + tinylist) # Prints concatenated lists


# tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
# tinytuple = (123, 'john')

# print (tuple)           # Prints complete tuple
# print (tuple[0])        # Prints first element of the tuple
# print (tuple[1:3])      # Prints elements starting from 2nd till 3rd 
# print (tuple[2:])       # Prints elements starting from 3rd element
# print (tinytuple * 2)   # Prints tuple two times
# print (tuple + tinytuple) # Prints concatenated tuple


# dict = {}
# dict['one'] = "This is one"
# dict[2]     = "This is two"

# tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


# print (dict['one'])       # Prints value for 'one' key
# print (dict[2])           # Prints value for 2 key
# print (tinydict)          # Prints complete dictionary
# print (tinydict.keys())   # Prints all the keys
# print (tinydict.values()) # Prints all the values


# a= 7
# b= 2

# print(2**b)

# var = 100

# if ( var  == 100 ) :
	# print ("Value of expression is 100")

# print ("Good bye!")

# var1 = 'Hello World!'
# var2 = "Python Programming"

# print ("var1[0]: ", var1[0])

# print ("My name is %s and weight is %d kg!" % ('Zara', 21)) 


# list = ['physics', 'chemistry', 1997, 2000]
# print ("Value available at index 2 : ", list[2])

# list[2] = 2001
# print ("New value available at index 2 : ", list[2])


# list = ['physics', 'chemistry', 1997, 2000]

# print (list)
# del list[2]
# print (list)

# tup1 = ('physics', 'chemistry', 1997, 2000)
# tup2 = (1, 2, 3, 4, 5, 6, 7 )

# print ("tup1[0]: ", tup1[0])
# print ("tup2[1:5]: ", tup2[1:5])


# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# print ("dict['Name']: ", dict['Name'])
# print ("dict['Age']: ", dict['Age'])


# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# dict['Age'] = 8; # update existing entry
# dict['School'] = "DPS School" # Add new entry

# print ("dict['Age']: ", dict['Age'])
# print ("dict['School']: ", dict['School'])

# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# del dict['Name'] # remove entry with key 'Name'
# dict.clear()     # remove all entries in dict
# del dict         # delete entire dictionary

# print (dict['Name'])
# print ("dict['School']: ", dict['School'])


# import time;  # This is required to include time module.

# ticks = time.time()
# print (ticks)

# import time
# print (time.localtime());

# import time

# localtime = time.localtime(time.time())
# print ("Local current time :", localtime)

# import calendar

# cal = calendar.month(2020, 1)
# print ("Here is the calendar:")
# print (cal)

# def functionname():
#    var = "JK"
#    return var

# print(functionname())


# # Function definition is here
# def printme( str ):
#    "This prints a passed string into this function"
#    print (str)
#    return

# # Now you can call printme function
# printme("This is first call to the user defined function!")
# printme("Again second call to the same function")

# Function definition is here
# def changeme( mylist ):
#    # "This changes a passed list into this function"
#    print ("Values inside the function before change: ", mylist)
#    mylist[2]=50
#    print ("Values inside the function after change: ", mylist)
#    return

# # Now you can call changeme function
# mylist = [10,20,30]
# changeme( mylist )
# print ("Values outside the function: ", mylist)


# Function definition is here
# def printinfo(  age1 ,name1):
#    "This prints a passed info into this function"
#    print ("Name: ", name1,"Age ", age1)
#    # print ()
#    return

# # Now you can call printinfo function
# printinfo(  name1 = "miki" ,age1 = 50,)

# total = 0 # This is global variable.
# # Function definition is here
# def sum( arg1, arg2 ):
#    # Add both the parameters and return them."
#    total = arg1 + arg2; # Here total is local variable.
#    print ("Inside the function local total : ", total)
#    return total

# # Now you can call sum function
# sum( 10, 20 )
# print ("Outside the function global total : ", total )

# def fib(n): # return Fibonacci series up to n
#    result = []
#    a, b = 0, 1
#    while b < n:
#       result.append(b)
#       a, b = b, a + b
#    return result

# from fib import fib
# print(fib(100))
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


# def fib(n): # return Fibonacci series up to n
#    result = []
#    a, b = 0, 1
#    while b < n:
#       result.append(b)
#       a, b = b, a + b
#    return result

# if __name__ == "__main__":
#    f = fib(100)
#    print(f[10:])

# import math

# content = dir(math)

# print (content[1])

# import Phone

# Phone.Pots()
# Phone.Isdn()
# Phone.G3()

# fo = open("foo.txt", "wb")
# print ("Name of the file: ", fo.name)
# print ("Closed or not : ", fo.closed)
# print ("Opening mode : ", fo.mode)
# fo.close()

# def KelvinToFahrenheit(Temperature):
	# assert (Temperature >= 0),"Colder than absolute zero!"
    # return ((Temperature-273)*1.8)+32

# print (KelvinToFahrenheit(273))
# print (int(KelvinToFahrenheit(505.78)))
# print (KelvinToFahrenheit(-5))


# try:
#    fh = open("testfile", "w")
#    fh.write("This is my test file for exception handling!!")
# except IOError:
#    print ("Error: can\'t find file or read data")
# else:
#    print ("Written content in the file successfully")
#    fh.close()

# Define a function here.
# def temp_convert(var):
#    try:
#       return int(var)
#    except ValueError as Argument:
#       print ("The argument does not contain numbers\n", Argument)

# # Call above function here.
# temp_convert("xyz")

# class Employee:
#    # 'Common base class for all employees'
#    empCount = 0

#    def __init__(self, name, salary):
#       self.name = name
#       self.salary = salary
#       Employee.empCount += 1
   
#    def displayCount(self):
#      print "Total Employee %d" % Employee.empCount

#    def displayEmployee(self):
#       print "Name : ", self.name,  ", Salary: ", self.salary

# emp1 = Employee("Zara", 2000)
# # emp1.displayCount()
# # This would create second object of Employee class
# emp2 = Employee("Manni", 5000)

# emp1.displayEmployee()

# class Employee:
#    'Common base class for all employees'
#    empCount = 0

#    def __init__(self, name, salary):
#       self.name = name
#       self.salary = salary
#       Employee.empCount += 1
   
#    def displayCount(self):
#      print ("Total Employee %d" % Employee.empCount)

#    def displayEmployee(self):
#       print ("Name : ", self.name,  ", Salary: ", self.salary)

# emp1 = Employee("Zara", 2000)
# emp2 = Employee("Manni", 5000)
# print ("Employee.__doc__:", Employee.__doc__)
# print ("Employee.__name__:", Employee.__name__)
# print ("Employee.__module__:", Employee.__module__)
# print ("Employee.__bases__:", Employee.__bases__)
# print ("Employee.__dict__:", Employee.__dict__ )

# class Point:
#    def __init__( self, x=0, y=0):
#       self.x = x
#       self.y = y
#    def __del__(self):
#       class_name = self.__class__.__name__
#       print (class_name, "destroyed")

# pt1 = Point()
# pt2 = pt1
# pt3 = pt1
# print (id(pt1), id(pt2), id(pt3));   # prints the ids of the obejcts
# del pt1
# del pt2
# del pt3

# class Parent:        # define parent class
#    def myMethod2(self):
#       print ('Calling parent method')

# class Child(Parent): # define child class
#    def myMethod(self):
#       print ('Calling child method')

# c = Child()          # instance of child
# c.myMethod2() 

# class Vector:
#    def __init__(self, a, b):
#       self.a = a
#       self.b = b

#    def __str__(self):
#       return 'Vector (%d, %d)' % (self.a, self.b)
   
#    def __add__(self,other):
#       return Vector(self.a + other.a, self.b + other.b)

# v1 = Vector(2,10)
# v2 = Vector(5,-2)
# print (v1 + v2)

# import re

# line = "Cats are smarter than dogs"

# matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

# if matchObj:
#    print ("matchObj.group() : ", matchObj.group())
#    print ("matchObj.group(1) : ", matchObj.group(1))
#    print ("matchObj.group(2) : ", matchObj.group(2))
# else:
#    print ("No match!!")



# print ("Content-type:text/html")
# print()
# print ("<html>")
# print ('<head>')
# print ('<title>Hello Word - First CGI Program</title>')
# print ('</head>')
# print ('<body>')
# print ('<h2>Hello Word! This is my first CGI program</h2>')
# print ('</body>')
# print ('</html>')

# import os

# print ("Content-type: text/html")
# print ()
# print ("<font size=+1>Environment</font><\br>")
# for param in os.environ.keys():
#   print ("<b>%20s</b>: %s<\br>" % (param, os.environ[param]))


# import PyMySQL

# # Open database connection
# db = PyMySQL.connect("localhost","testuser","test123","TESTDB" )

# # prepare a cursor object using cursor() method
# cursor = db.cursor()

# # execute SQL query using execute() method.
# cursor.execute("SELECT VERSION()")

# # Fetch a single row using fetchone() method.
# data = cursor.fetchone()

# print ("Database version : %s " % data)

# # disconnect from server
# db.close()

# import _thread
# import time

# Define a function for the thread
# def print_time( threadName, delay):
#    count = 0
#    while count < 5:
#       time.sleep(delay)
#       count += 1
#       print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

# # Create two threads as follows
# try:
#    _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
#    _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
# except:
#    print ("Error: unable to start thread")

# while 1:
#    pass

# import threading
# import time

# exitFlag = 0

# class myThread (threading.Thread):
#    def __init__(self, threadID, name, counter):
#       threading.Thread.__init__(self)
#       self.threadID = threadID
#       self.name = name
#       self.counter = counter
#    def run(self):
#       print ("Starting " + self.name)
#       print_time(self.name, self.counter, 5)
#       print ("Exiting " + self.name)

# def print_time(threadName, delay, counter):
#    while counter:
#       if exitFlag:
#          threadName.exit()
#       time.sleep(delay)
#       print ("%s: %s" % (threadName, time.ctime(time.time())))
#       counter -= 1

# # Create new threads
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)

# # Start new Threads
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print ("Exiting Main Thread")

# import queue
# import threading
# import time

# exitFlag = 0

# class myThread (threading.Thread):
#    def __init__(self, threadID, name, q):
#       threading.Thread.__init__(self)
#       self.threadID = threadID
#       self.name = name
#       self.q = q
#    def run(self):s np
# import matplotlib as plt

# x = np.arange(0, 5, 0.1)
# y = np.sin(x)
# plt.plot(x, y)
#       print ("Starting " + self.name)
#       process_data(self.name, self.q)
#       print ("Exiting " + self.name)

# def process_data(threadName, q):
#    while not exitFlag:
#       queueLock.acquire()
#       if not workQueue.empty():
#          data = q.get()
#          queueLock.release()
#          print ("%s processing %s" % (threadName, data))
#       else:
#          queueLock.release()
#          time.sleep(1)

# threadList = ["Thread-1", "Thread-2", "Thread-3"]
# nameList = ["One", "Two", "Three", "Four", "Five"]
# queueLock = threading.Lock()
# workQueue = queue.Queue(10)
# threads = []
# threadID = 1

# # Create new threads
# for tName in threadList:
#    thread = myThread(threadID, tName, workQueue)
#    thread.start()
#    threads.append(thread)
#    threadID += 1

# # Fill the queue
# queueLock.acquire()
# for word in nameList:
#    workQueue.put(word)
# queueLock.release()

# # Wait for queue to empty
# while not workQueue.empty():
#    pass

# # Notify threads it's time to exit
# exitFlag = 1

# # Wait for all threads to complete
# for t in threads:
#    t.join()
# print ("Exiting Main Thread")

# import tkinter # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
# top = tkinter.Tk()
# # Code to add widgets will go here...
# top.mainloop()

def area(x,y = 3.14): 
   a = y*x*x
   print (a)
   return a

def hello(greetings):
	print (greetings,"WORLD")

hello("HELLO") 

# def area(x,y = 3.14): # formal parameters
#    a = y*x*x
#    print (a)
#    return a

# a = area(10)
# print("area",a)


# import sys

# try:
#    # open file stream
#    file = open(file_name, "w")

# except IOError:
#    print ("There was an error writing to", file_name)
#    sys.exit()
# print ("Enter ", file_finish,)
# print (" When finished")

# while file_text != file_finish:
#    	file_text = raw_input("Enter text: ")
#    	if file_text == file_finish:
      	# close the file
	  	# file.close
    	# break

# file.write(file_text)
# file.write("\n")
# file.close()
# file_name = input("Enter filename: ")

# if len(file_name) == 0:
#    print ("Next time please enter something")
#    sys.exit()

# try:
#    file = open(file_name, "r")

# except IOError:
#    print ("There was an error reading file")
#    sys.exit()
# file_text = file.read()
# file.close()
# print (file_text)

# import numpy as np 
# a = 'hello world' 
# print a

# import numpy as np
# import matplotlib as plt

# x = np.arange(0, 5, 0.1)
# y = np.sin(x)
# plt.plot(x, y)