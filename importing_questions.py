import numpy
import xlsxwriter
from pandas import read_excel
import xlrd
import pandas
data = read_excel('data/questions_and_choices.xlsx')
print(data.columns[2])

# print(data.head())
