import csv
from functools import reduce
from proj04wd03 import columnOfTable
 
def column_nh(sheet, colPos):
   column = columnOfTable(sheet, colPos)
   return column[1:]
 
def column_int(column):
   return list(map(lambda x: int(x), column))
 
def min_minutes(sheet):
   column = column_nh(sheet, 18)
   column = column_int(column)
   return reduce(lambda x, y: min(x, y), column)
 
def avg_carriers(sheet):
   column = column_nh(sheet, 12)
   column = column_int(column)
   sum = reduce(lambda x, y: x + y, column)
   return sum / len(column)
 
def total_airlines(sheet):
   column = column_nh(sheet, 7)
   column = column_int(column)
   airlines = list(filter(lambda x: x <= 300, column))
   return len(airlines)