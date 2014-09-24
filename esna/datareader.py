#@+leo-ver=5-thin
#@+node:peckj.20140923100049.4061: * @file datareader.py
#@@language python

#@+<< imports >>
#@+node:peckj.20140923100049.4062: ** << imports >>
import csv
#@-<< imports >>
#@+<< declarations >>
#@+node:peckj.20140923100049.4063: ** << declarations >>
#@-<< declarations >>

#@+others
#@+node:peckj.20140923100049.4065: ** comment_stripper
def comment_stripper(iterator):
  for line in iterator:
    if line.startswith('#') or not line.strip():
      continue
    yield line
#@+node:peckj.20140923100049.4064: ** read_data
def read_data(data_file):
  ''' a generator function for reading csv files with # comments. '''
  with open(data_file, 'rb') as csv_data:
    reader = csv.reader(comment_stripper(csv_data))
    for row in reader:
      yield row
#@-others
#@-leo
