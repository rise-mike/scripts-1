# Outputs a 1 layer JSON object to CSV, separating keys and values into different columns.
# Row 22 is configured for a specific object, may need to tweak

from sys import argv
import json
import csv

infile = input("In this directory, what's your JSON file called? > ")
outfile = input("What do you want the destination (with extension) to be? > ")
print()
input(f'So you want {infile} to wind up in {outfile}?')

with open(infile) as source:
  data = json.load(source)

destination = open(outfile, 'w')

writer = csv.writer(destination)

writer.writerow(["Name"] + ["Text"])

for k, v in data['TEXT'].items():
  this_row = k + ":" + v
  writer.writerow([k] + [v])