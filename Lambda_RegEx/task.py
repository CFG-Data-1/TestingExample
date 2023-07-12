
"""
Simply a useful example to know.

Task:
Search through a list of dictionaries to find the only one
dictionary that you need by value.

Let's say we need to find some info on a specific CFG student.
Our data structure is as follows: every student is represented as a dictionary
and all dictionaries are held in a list.
We need to find one student by her name.
"""

students = [
    {'name': "Jane", 'age': 24, 'specialisation': 'Software'},
    {'name': "Priya", 'age': 24, 'specialisation': 'Data'},
    {'name': "Priya", 'age': 34, 'specialisation': 'Data'},
    {'name': "Priya", 'age': 36, 'specialisation': 'Software'},
    {'name': "Diana", 'age': 18, 'specialisation': 'Data'}
]


# get info for a student called 'Priya' ( a search criteria can be anything:
# an ID, a name, name and surname together and many more)

result = list(filter(lambda x :x["name"] == "Priya" and x["age"]== 24 , students))

print(result)