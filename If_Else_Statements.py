#Boolean Expression	-> True or False

print(20 > 10)
print(20 == 10)
print(20 < 10)
print(bool("Hello World"))
print(bool(20))


Python Conditions

Equals						-> x == y
Not Equals					-> x != y
Less than 					-> x <  y
Less than or equal to		-> x <= y
Greater than 				-> x > y
Greater than or equal to 	-> x >= y
Boolean OR 					-> x or y , x | y
Boolean AND					-> x and y, x & y
Boolean NOT 				-> not x

if -
else -


#If Statement

x = 70
y = 60

if x > y:
	print("x is greater than y ")

#Elif

x = 70
y = 70
 if x < y:
...     print("x is greater than y")
... else:
...     print("x is not greater than y")
...
x is not greater than y
>>> if x > y:
...     print("x is greater than y")
... elif x >= y:
...     print("x is greater or equal to y")
... elif y < x:
...     print("y is smaller than x")
... else:
...     print("x is nothing")


#Short Hand If

if x > y: print("x is greater than y")

#Short Hand If...Else

print(x) if x > y else print(y)

#And is logical operator

x = 50
y = 40
z = 100
if x > y and z > x:
	print("All Conditions are True")

if x < y and z > x:
	print("All Conditions are True")
else:
	print("Some Conditions are False")

#Or is logical operator

x = 50
y = 40
z = 100
if x > y or z < y:
	print("One of the conditions is True")
elif x > y and z > y:
	print("All conditions are True")
else:
	print("nothing else")

if x > y and z > y and x > z:
	print("Answer 1")
elif x == y or z == y or z > y and x > y:
	print("Answer 2")
elif z > y and y < x or z > y:
	print("Answer 3")
else:
	print("Default")

x = int(input("Please Enter exam result: "))
if x < 101 and x > 89 or x == 100:
	print("A")
elif x < 89 and x > 79:
	print("B")
elif x < 79 and x > 59:
	print("C")
elif x < 59 and x > 49:
	print("D")
elif x < 49 and x > 0 or x == 0 or x == 49:
	print("F")
else:
	print("Check Again")

x = int(input("Please Enter your number:"))
if 100 > and 90 <
	print("A")

#Nested If is if statements in if statements

x = 50

if x > 10:
	print("x is ten")
	if x > 20:
		print("x is greater than 20")
	else:
		print("No,x is not greater than 20")

if x > 10 and x != 10 or x > 20:
	print("x is greater than 10 and 20")
else:
	print("x is not greater than 10 & 20")


if student
	if batch
		if gender
else
	not

student = "SFU"
	batch = "3"
		gender = "male"
		