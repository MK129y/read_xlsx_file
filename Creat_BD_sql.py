import psycopg2
import openpyxl
#import pandas
import numpy as np

book = openpyxl.open('razb_uch.xlsx',read_only=True)

sheet = book.active

con = psycopg2.connect(
  database="Task",
  user="postgres",
  password="1",
  host="localhost",
  port="5432"
)
cur = con.cursor()
pkr =cur.execute('''CREATE TABLE TABLE1234(
    UCH_OST_POL INTeger,
    NAME_BEGIN_VOST_UCH CHAR(50));
    ''')
for row in range(1,sheet.max_row + 1):

    ID_UCH_VOST_POL = sheet[row][0].value
    NAME_BEGIN_VOST_UCH = sheet[row][1].value
    ESR_BEGIN_VOST_UCH = sheet[row][2].value
    DOR_BEGIN_VOST_UCH = sheet[row][3].value
    
con.commit()
con.close()
