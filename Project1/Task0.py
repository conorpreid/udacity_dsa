import csv

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

def fileHeadAndTail (filename):
  """
  Returns the first line and last line of a given file
  """
  with open(filename, 'r') as f:
    reader = csv.reader(f)
    lines = list(reader)
    results = {}
    results['first_record'] = lines[0]
    results['last_record'] = lines[len(lines)-1]

  return results

if __name__ == '__main__':
  texts = fileHeadAndTail('texts.csv')
  calls = fileHeadAndTail('calls.csv')

  print (
    "First records of texts,",
    texts['first_record'][0],
    "texts",
    texts['first_record'][1],
    "at time",
    texts['first_record'][2]
    )

  print (
    "Last records of calls,",
    calls['first_record'][0],
    "texts",
    calls['last_record'][1],
    "at time",
    calls['last_record'][2]
    )
