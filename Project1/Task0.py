"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import unittest
with open('data/texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('data/calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

def SumMyNumbers(x, y, z):
	return x + y + z

def myfunction(filename):
    f=open(filename)
    maximum = 0
    for line in f:
        if maximum < len(line):
            maximum = len(line)
        pass
    f.close()
    return maximum
