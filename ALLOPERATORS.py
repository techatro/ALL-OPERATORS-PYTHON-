import operator
# Arithematic Operators
# Add Operator
a,b= list (map (int,(input('Enter the two values')).split()))
print('Arithematic Operators') 
Add = a + b
print('The addition of two numbers is:',Add)
# Sub Operator
sub = a - b
print('The Subtraction of two numbers is:',sub)
# Mul Operator
M = a * b
print('The Multiplication of two numbers is:',M)
# Div Operator 
Div = a / b
print('The Division of two numbers is:',Div)
# Mod Operator
Mod = a // b
print('The Modulus of two numbers is:',Mod)
#Relational Operators
print('Relational Operators')
if(a>b):
    print('The value of a is greater than b ')
if(a<b):
    print('The value of a is lesser than b ')
if(a>=b):
    print('The value of a is greater than or equal to than b ')
if(a<=b):
    print('The value of a is lesser than or equal to b ')
if(a==b):
    print('The value of a is equal to b ')
# logical Operators
print('logical Operators')
c = True
d = False
# logical and 
print(c and d)
# logical or
print(c or d)
# logical not
print(not c)
# Bitwise Operator
print('Bitwise Operator')
# Print bitwise AND operation   
print('The bitwise AND operator of two values is:', a & b) 
# Print bitwise OR operation 
print('The bitwise OR operator of two values is:',a | b) 
# Print bitwise NOT operation  
print('The bitwise NOT operator of two values is:',~a) 
# print bitwise XOR operation  
print('The bitwise XOR operator of two values is:',a ^ b) 
# print bitwise right shift operation  
print('The bitwise Right shift o operator of two values is:',a >> 2) 
# print bitwise left shift operation  
print('The bitwise left shift operator of two values is:',a << 2) 
#Identity Operators
print('Identity Operators')
a1 = 3
b1 = 3
a2 = 'Alloperatorinpython'
b2 = 'Alloperatorinpython'
a3 = [1,2,3] 
b3 = [1,2,3] 
print(a1 is not b1)
print(a2 is b2)
# Output is False, since lists are mutable.
print(a3 is b3)
#Membership Operator
print('Membership Operator')
e = 'All Operators in Python'
f = {3:'a',4:'b'} 
print('A' in e) 
print('all' not in e) 
print('All' not in e) 
print(3 in f) 
print('b' in f) 
#Operator Precedence
print('Operator Precedence')
# Precedence of '+' & '*'  
expr = 10 + 20 * 30
print(expr)  
# Precedence of 'or' & 'and'  
name = "Alex"
age = 0
if name == "Alex" or name == "John" and age >= 2 :   
    print("Hello! Welcome.")  
else :  
    print("Good Bye!!") 
#Operator Associativity
print('Operator Associativity')
# Left-right associativity  
# 100 / 10 * 10 is calculated as   
# (100 / 10) * 10 and not   
# as 100 / (10 * 10)  
print(100 / 10 * 10)  
# Left-right associativity  
# 5 - 2 + 3 is calculated as   
# (5 - 2) + 3 and not   
# as 5 - (2 + 3)  
print(5 - 2 + 3)  
# left-right associativity  
print(5 - (2 + 3))  
# right-left associativity  
# 2 ** 3 ** 2 is calculated as   
# 2 ** (3 ** 2) and not   
# as (2 ** 3) ** 2  
print(2 ** 3 ** 2) 
#Ternary Operator in Python
# Copy value of a in min if a < b else copy b 
print('Ternary Operator')
min = a if a < b else b 
print(min)
#Direct Method by using tuples, Dictionary and lambda
# Use tuple for selecting an item 
# (if_test_false,if_test_true)[test] 
print( (b, a) [a < b] ) 
  # Use Dictionary for selecting an item 
print({True: a, False: b} [a < b]) 
# lamda is more efficient than above two methods 
#  because in lambda  we are assure that 
# only one expression will be evaluated unlike in 
# tuple and Dictionary 
print((lambda: b, lambda: a)[a < b]()) 
#Ternary operator can be written as nested if-else:
print ("Both a and b are equal" if a == b else "a is greater than b"
        if a > b else "b is greater than a")
# Conditional in Ternaray operator
# If a is less than b, then a is assigned 
# else b is assigned (Note : it doesn't  
# work if a is 0. 
print('Conditional in Ternaray operator')
min = a < b and a or b 
print(min)  
# A Python program to demonstrate the use of 
# "//" for integers
print('"//" for integers')
print (a//b)
print (-a//b)
# concatenate two strings 
print('concatenate two strings ')
print("Operators"+"in Python") 
# Repeat the String
print('Repeat the String') 
print(" All operators "*4) 
#Any All in Python
print('Any All in Python')
# Since all are false, false is returned 
print(any([False, False, False, False])) 
# Here the method will short-circuit at the 
# second item (True) and will return True. 
print(any([False, True, False, False])) 
# Here the method will short-circuit at the 
# first (True) and will return True. 
print(any([True, False, False, False])) 
# Python code to demonstrate working of  
# truediv(), floordiv(), pow(), mod() 
# using truediv() to divide two numbers 
print("The true division of numbers is : ",end=""); 
print(operator.truediv(a,b)) 
# using floordiv() to divide two numbers 
print("The floor division of numbers is : ",end=""); 
print (operator.floordiv(a,b)) 
# using pow() to exponentiate two numbers 
print("The exponentiation of numbers is : ",end=""); 
print(operator.pow(a,b)) 
# using mod() to take modulus of two numbers 
print("The modulus of numbers is : ",end=""); 
print(operator.mod(a,b)) 
#Python code to demonstrate working of  
# setitem(), delitem() and getitem()
# Initializing list 
li = [1, 5, 6, 7, 8] 
  
# printing original list  
print ("The original list is : ",end="") 
for i in range(0,len(li)): 
    print (li[i],end=" ") 
print ("\r") 
# using setitem() to assign 3 at 4th position 
operator.setitem(li,3,3) 
# printing modified list after setitem() 
print ("The modified list after setitem() is : ",end="") 
for i in range(0,len(li)): 
    print (li[i],end=" ") 
print ("\r") 
# using delitem() to delete value at 2nd index 
operator.delitem(li,1) 
# printing modified list after delitem() 
print ("The modified list after delitem() is : ",end="") 
for i in range(0,len(li)): 
    print (li[i],end=" ") 
print ("\r") 
# using getitem() to access 4th element 
print ("The 4th element of list is : ",end="") 
print (operator.getitem(li,3)) 
# Python program to illustrate 
# Finding common member in list  
# using 'in' operator
print('Overlapping operators') 
list1=[1,2,3,4,5] 
list2=[6,7,8,9] 
for item in list1: 
    if item in list2: 
        print("overlapping")       
else: 
    print("not overlapping")
#END 





        
                



