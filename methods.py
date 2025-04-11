### List Methods

a = [1,2,3]
a.append(4) # [1,2,3,4]
b = a.copy() # b = [1,2,3,4]
count = a.count(2) # count = 1
a.extend(b) # [1,2,3,4,1,2,3,4] 
index = a.index(3) # index = 3. First occurence.
a.insert(2, "elma") # [1,2, "elma ",3,4,1,2,3,4]
a.remove("elma") # [1,2,3,4,1,2,3,4] first occurence.
a.pop(2) # [1,2,4,1,2,3,4]  Default is last item
a.reverse() # [4,3,2,1,4,2,1]
a.sort() # [1,1,2,2,3,3]
a.sort(reverse=True) # [3,3,2,2,1,1]
a.clear() # []

def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]
cars.sort(key=myFunc)
# cars.sort(key= lambda x: x["year"])
print(cars)
########################################

## String Methods

my_string = "hello, sinan."
my_string.capitalize() # Hello, sinan. 
my_string.casefold() # similar to lower but it can lower additioanal characters. Use it when you compare casefolded variables(case-insensitive string comparison)
my_string.lower()
my_string.center(20) # center the word in 20 character lentgth string. '   hello, sinan.    '
my_string.center(20, "x") # 'xxxhello, sinan.xxxx'
my_string.count("hello") # count how many substring in the string
my_string.count("si", 2, 5) # (<substring>, start_index, stop_index)
my_string.encode("ascii", errors="ignore") # encode the string
my_string.endswith("sinan.") # boolean.
my_string.endswith(("sinan.","hello")) # can check in tuple.
my_string.endswith("sinan",3,5) # can check specific position
second_string = "selma\tahmet\t"
second_string.expandtabs(5) # expand the tabe size.
print(second_string.expandtabs(4))
my_string.find("ello") # Find the first occurrence. Return -1 if it doesnt find anything.
txt1 = "My name is {name} and my age is {age}".format(name = "sinan", age = 24)

## Formatting Types:
"We have {:<8} chickens".format(49) # Left align. We have 49       chickens.
"We have {:>8} chickens".format(49) # Right align. We have       49 chickens.
"We have {:^8} chickens".format(49) # Center align. We have    49    chickens.
"We have {:=8} chickens".format(-49) # Sign to left align. We have -     49 chickens.
"We have {:+8} chickens".format(49) # Use a plus sign to indicate if its positive or negative . We have      +49 chickens
"We have {:-8} chickens".format(-49) # Use a negative sign for negative values only . We have      -49 chickens
"We have {: } and {: } chickens".format(-49,54) # Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers. We have -49 and  54 chickens
"We have {:,} chickens.".format(12343) # Use comma as thousand seperator. We have 12,343 chickens.
"We have {:_} chickens.".format(12343) # Use underscore as thousand seperator. We have 12_343 chickens.
"Result is {:b} in binary.".format(5) # Binary format. Result is 101 in binary.
"Unicode of 77 is {:c}".format(77) # Value to unicode character. Unicode of 77 is M
"Decimal of 0b101 is {:d}".format(0b101) # decimal format
"Big number is {:e}".format(124124) # Scientifiv format with lower e. Big number is 1.241240e+05
"Fixed number is {:.2f}".format(12.32323) # fixed number. Fixed number is 12.32
"Floating format for {:g}".format(21312) # General format.
# {:o} -> octal format {:x} ->hexa format {:n} -> number format {:%} -> percentage format
#####

person = {"person1": {"name":"sinan", "age":29}}
"One person is {person1[name]} and age is {person1[age]}".format_map(person) # Map the dict to string. One person is sinan and age is 29
"Selamlar sinan".index("lamlar") # Similar to find but can return exception error. 2

## Boolean String methods
# isalnum() -> Checks if alphanumerical (a-z) and numbers (0-9). not alphanumeric: (space)!#%&? etc.
# isalpha() -> in alphabet.
# isascii() -> in ASCII characters.
# isdecimal() -> decimal characters
# isdigit() -> similar decimal but also include exponents
# isidentifier() -> alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.
# islower() -> All lower case
# isnumeric() -> another for number inclues square or rootsquare
# isprintable() ->  \n, \t etc returns false
# isspace() -> returns True if it includes only whitespaces
# istitle() -> title case
# isupper() -> all upper case

my_tuple = ("sinan", "erbezci")
x = "#".join(my_tuple) # takes all items in an iterable and joins them into one string. sinan#erbezci
"banana".ljust(20) # left adjust with character (default is space). other one is rjust()
"    banana".lstrip() # strip left leading characters (default is space). other one is rstrip()


# lower(), upper()