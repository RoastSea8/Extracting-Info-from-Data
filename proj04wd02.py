import csv

# 4
file = open('airlines.csv')
csvreader = csv.reader(file)
header = []
header = next(csvreader)
print("Header: ")
print(header)
 
# 5
callOne = []
callOne = next(csvreader)
callTwo = []
callTwo = next(csvreader)
callThree = []
callThree = next(csvreader)
print("\n\nNext call one:\n", callOne, "\n\nNext call two:\n", callTwo, "\n\nNext call three:\n", callThree)
 
# 7 a.)
def headingsOfTable(sheet):
   file = open(sheet)
   csvreader = csv.reader(file)
   return next(csvreader)
 
# 7 b.)
def dataOfTable(sheet):
   with open(sheet, newline='') as f:
      reader = csv.reader(f)
      data = []
      header = next(reader)
      for row in reader:
         if (row != header):
            data.append(row)
   return data