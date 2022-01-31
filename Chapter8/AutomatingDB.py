import pyodbc
import pandas as pd

connectionString = r'DRIVER={SQL Server};SERVER=.\SQLExpress;DATABASE=lab8;Trusted_Connection=yes'

# Part 1

sqlStr="""CREATE TABLE Student (
StudentID int NOT NULL,
FirstName nvarchar(40) NOT NULL,
Surname nvarchar(30) NULL,
Course nvarchar(30) NULL,
City nvarchar(15) NULL)"""

conn = pyodbc.connect(connectionString)
cur = conn.cursor() 
cur.execute(sqlStr)
conn.commit()
conn.close()

# part 2

# Inserting data manually:

# sqlStr = """INSERT INTO Student (StudentID, FirstName, Surname, Course, City)
# VALUES(123,'Umar','Rehman', 'Coding-Fundamentals', 'London')"""
# conn = pyodbc.connect(connectionString)
# cur = conn.cursor() 
# cur.execute(sqlStr)
# conn.commit()S
# conn.close()

# Inserting data from csv file:

conn = pyodbc.connect(connectionString)
cur = conn.cursor()
df = pd.read_csv("Chapter8//students.csv")

for index, row in df.iterrows():
    cur.execute("INSERT INTO Student (StudentID,FirstName,Surname,Course,City) values(?,?,?,?,?)", row.StudentID, row.FirstName, row.Surname, row.Course, row.City)

conn.commit()
conn.close()

# Part 3

sqlStr = """UPDATE Student
SET Course = 'SQL-Fundamentals'
WHERE StudentID = 123"""
conn = pyodbc.connect(connectionString)
cur = conn.cursor() 
cur.execute(sqlStr)
conn.commit()
conn.close()