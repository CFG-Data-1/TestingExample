import re

# Example 1  re.match(<regex>, s):
# str = "Nano Degree is fun."
# regex = "Nano\s\w+\s"
#
#
# matched = re.match(regex, str)
# print(matched)
#
# print(matched.span())
# print(matched.group())



# Example 2  re.search(<regex>, s):
# str = "Nano Degree is fun."
# regex = "Degree\s\w+\s"
#
#
# matched = re.search(regex, str)
# print(matched)
#
# print(matched.span())
# print(matched.group())


# # Example 3 : re.finditer(<regex>, s):
#
# """
# matches all of the regex patterns in the input string and
# returns an iterator containing all the re.Match
# objects of the matched substrings.
# """
#
# my_str = "Software and data science 777 are fun. " \
#          "I especially like doing data analysis and processing."
#
# regex = "data\s\w+\s"
# '''
# In the regex above: match 'data' followed by a space char,
# followed by at least one alphanumeric char, followed by a space char'
# '''
#
# for matched in re.finditer(regex, my_str):
#     print(matched)

#Example 4 findall
# my_str = "Software and data science 777 are fun. " \
#          "I especially like doing data analysis and processing."
#
# regex = "data\s\w+\s"
#
# for matched in re.finditer(regex, my_str):
#     print(matched)
#
# for matched in re.findall(regex, my_str):
#     print(matched)
#
# result = re.sub(regex, 'SQL queries ', my_str)
# print(my_str)
# print(result)


# EXAMPLE 6 --- GROUPING

# """
# Sometimes we might want to match a regex pattern but only capture a
# portion (or group) of it. Regex provides a simple way of doing this
# by using the parenthesis (). We can define the group we want to capture
# by surrounding it with () within the regex pattern.
# """
#
# my_str = "Software and data science 777 are fun. " \
#          "I especially like doing data analysis and processing."
#
# regex = "data\s(\w+)\s"
# '''
# Match the word after 'data'
# '''
# for matched in re.findall(regex, my_str):
#     print(matched)


# EXAMPLE 7 --- COMPILING

"""
SO FAR, we have mainly used module-level functions provided by re directly. 
Another way to perform regex pattern matching is to *compile* the pattern first
and then call the functions on the compiled object. 

In general, we can use the compiled approach if we are going to use 
the pattern MULTIPLE times; otherwise, it’s simpler to use the module-level
(non-compiled) functions.
"""

my_str = "Software and data science 777 are fun. " \
         "I especially like doing data analysis and processing."

regex = "data\s(\w+)\s"
pattern = re.compile(regex)
'''
Match the word after 'data'
'''
print("COMPILED EXAMPLE")
for matched in pattern.findall(my_str):
    print(matched)












