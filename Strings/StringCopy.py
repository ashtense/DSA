# The following method makes a lot of unwanted strings which will be left to die in memory. Immutable string object.
def string_copy_garbage(string_to_copy):
    string_to_copy_in = ""
    for char_index in range(0, len(string_to_copy)):
        string_to_copy_in += string_to_copy[char_index]
    return string_to_copy_in

def string_copy_function(string_to_copy):
    string_to_copy_in = ['']* len(string_to_copy)
    for char_index in range(len(string_to_copy)):
        string_to_copy_in[char_index] = string_to_copy[char_index]
    return "".join(string_to_copy_in)

string_to_copy="geronimo"
#string_to_copy_in = string_copy_garbage(string_to_copy)
print(string_copy_function(string_to_copy))