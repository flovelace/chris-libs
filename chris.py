# for notation in python code, use the hash symbol

# create a string variable
# person = "Chris"

# create the string
# method 1
# print("Do mean things to " + person)
# method 2
# print("Do mean things to {}".format(person))
# method 3 (f string)
# print(f"Do mean things to {person}")

# String variables that hold the user's input
adj1 = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
adj2 = input("Adjective: ")

# String variable using the f string method. Use curly braces to insert the var
chrislib = f"Sometimes when I think about Chris, I realise that she is so {adj1}. That then leads me to think about the things that she has done. \
She really seems to {verb1} a lot. Do you remember that time when she tried to {verb2}? That was pretty {adj2}..."

## prints out the string
print(chrislib)