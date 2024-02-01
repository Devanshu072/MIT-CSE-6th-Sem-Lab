print("1. Updating a string")
print("var1 = 'Hello World!'")
var1 = 'Hello World!'
print ("Updated String :", var1[:6] + 'Python')
print(" ")
print(" ")

print("2. String formatting operator")
print("My name is %s and weight is %d kg!" % ('Abay', 55))
print(" ")
print(" ")

print("3. Built−in String methods")
print("capitalize() , the first character of the string is converted to upper case.")
str = "this is string example wow!!!"
print("str = this is string example wow!!!")
print(str.capitalize())
print(" ")
print(" ")


#at 15 th index, the substring ‘example’ is placed.
print("lower(),returns a copy of the string in which all case−based characters have been lowercased.")
str = "THIS IS STRING EXAMPLE ... WOW!!!"
print("str = THIS IS STRING EXAMPLE ... WOW!!!")
print (str.lower())
print(" ")
print(" ")


print("replace(), this method returns a copy of the string with all occurrences of substring old replaced by new.")
str = "this is string example ... wow!!! this is really string"
print("str = this is string example ... wow!!! this is really string")
print(str.replace("is", "was"))
print(" ")
print(" ")


print("swapcase(), this method returns a copy of the string in which al l the case−based characters have had their case swapped.")
str = "this is STRING example ... wow!!!"
print("str = this is STRING example ... wow!!!")
print (str.swapcase())
print(" ")
print(" ")


print("title(),returns a copy of the string in which first characters of all the words are capitalized.")
str = "this is string example ... wow!!!"
print("str = this is string example ... wow!!!")
print (str.title())
