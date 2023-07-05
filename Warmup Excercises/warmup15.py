"""
TASK 1 (copy-paste this task in the dialog window to share with the student)

Use the string "CodeFirstGirls" and only take a part of it: "Girls". The turn
the word "Girls" into "G-i-r-l-s".

NB: it is entirely up to you whether to write function or just write script
in the console.
"""

# EXAMPLE SOLUTION

string = "CodeFirstGirls"
word = string[-5:]  # use slicing or anything else
chars = list(word)  # split the word into individual chars
result = "-".join(chars)
print(result)


############################################################


"""
TASK 2 (copy-paste this task in the dialog window to share with the student)

Spice Girls ("Wannabe")

'''
Yo, I'll tell you what I want, what I really, really want
So tell me what you want, what you really, really want
I'll tell you what I want, what I really, really want
So tell me what you want, what you really, really want
I wanna, (ha) I wanna, (ha) I wanna, (ha) I wanna, (ha)
I wanna really, really, really wanna zigazig ah"
'''

Count how many times the word "really" appears in the Spice Girls lyrics.

NB: it is entirely up to you whether to write function or just write script
in the console.
"""

# EXAMPLE SOLUTION
# (just a quick solution that doesn't handle special cases)

lyrics = '''
Yo, I'll tell you what I want, what I really, really want
So tell me what you want, what you really, really want
I'll tell you what I want, what I really, really want
So tell me what you want, what you really, really want
I wanna, (ha) I wanna, (ha) I wanna, (ha) I wanna, (ha)
I wanna really, really, really wanna zigazig ah"
'''

words = lyrics.split(' ')  # split the text into words
words = [w.strip(',') for w in words]  # remove comas
# (well, ideally all punctuation, but in this example we care about comas only)

result = words.count('really')
print(result)
