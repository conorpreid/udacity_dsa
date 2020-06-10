"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re
from collections import defaultdict

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def AggregateBangaloreCallTargets (callList):
    """
    Take a list of call data (list of list) and
    return a dictionary that contains an aggregated
    view of what area codes and mobile prefixs are called
    by Bangalore numbers

    The rules to identify fixed line, mobile and telemarketer numbers
    are as strict as possible.
    """
    bangaloreCalls = list(filter(lambda x: x[0][:5] == '(080)', callList))
    codes = defaultdict(int)

    for call in bangaloreCalls:
      # Fixed lines
      fixedLineCheck = re.match(r"\(0([0-9]+)\)", call[1])
      if fixedLineCheck:
          codes[fixedLineCheck.group().strip("()")] += 1

      # Mobile Numbers
      elif call[1].startswith(('7', '8', '9')) and ' ' in call[1]:
          codes[call[1][:4]] += 1

      # Telemarketers
      elif str(call[1]).startswith('140'):
          codes['140'] += 1

    return codes

def DerivePercentBangaloreToBangaloreCalls(callList):
    bangaloreOriginCallTargets = AggregateBangaloreCallTargets(callList)
    return float(bangaloreOriginCallTargets['080']) / sum(bangaloreOriginCallTargets.values())

print \
    "The numbers called by people in Bangalore have codes:", \
    "\n".join(sorted(AggregateBangaloreCallTargets(calls).keys()))

print \
    "{0:.0f}%".format(DerivePercentBangaloreToBangaloreCalls(calls) * 100), \
    "of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."
