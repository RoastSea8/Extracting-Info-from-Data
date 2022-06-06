import csv
 
def recordOfTable(sheet, rowPos):
   if (rowPos == 0):
       return "The header is not a record."
   with open(sheet, newline='') as f:
       reader = csv.reader(f)
       pos = 0
       for row in reader:
           if (pos == rowPos):
               return row
           pos += 1
       return "Please enter valid inputs."
 
def fieldOfRecord(sheet, rowPos, fieldPos):
   record = recordOfTable(sheet, rowPos)
   counter = 0
   for field in record:
       if (counter == fieldPos):
           return field
       counter += 1
   return "Please enter valid inputs."
 
def columnOfTable(sheet, colPos):
   with open(sheet, newline='') as f:
       reader = csv.reader(f)
       column = []
       for row in reader:
           pos = 0
           for field in row:
               if pos == colPos:
                   column.append(field)
               pos += 1
   return column