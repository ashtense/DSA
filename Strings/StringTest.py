string_variable = "Geronimo"
#
# to select a substring based on index
#print(string_variable[1:4])
print(string_variable[1:4])

#string_variable = string_variable[0:3] + " Grump"
string_variable = string_variable[0:3] + " Grump"
#print(string_variable)
print(string_variable)

# string repitition
#string_variable = string_variable * 2
string_variable = string_variable * 2
#print("String repitited by multiplication: % s" %string_variable)
print("String repitited by multiplication: % s" %string_variable)

# membership check using in
#if('G' in string_variable):
if('G' in string_variable):
    print("yes")

# Unicode strings - Normal strings in python are stored as 8-bit ASCII. 
# But one can convert them into 16 bit UNICODE and get more breathing room.
unicode_string = u"Hello, World!"
print(unicode_string)

#Count of a character in given string
#g_counter = string_variable.count('G', 0, len(string_variable))
g_counter = string_variable.count('G')
print(g_counter)

# Finding a substring or a character
print(string_variable.find('Trump')) # returns the index number
print(string_variable.index('Grump')) # returns the index number only thing is that it raises an exception in case of error. Try changing the string matcher

# Check if string alphanumeric
new_string = "1231af"
print(new_string.isalnum())