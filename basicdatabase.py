import sqlite3

conn = sqlite3.connect('lunch.db')
c = conn.cursor()

#delete table
#c.execute('''DROP TABLE meals''')

#create a table
c.execute('''CREATE TABLE meals(sandwich TEXT, fruit TEXT, tablenumber INT)''')

#data to insert
sandwich = 'chicken'
fruit = 'orange'
tablenum = 22

#insert and commit to database
c.execute('''INSERT INTO meals VALUES(?,?,?)''', (sandwich, fruit, tablenum))
conn.commit()

#select all data from table and print
c.execute('''SELECT * FROM meals''')
results = c.fetchall()
print(results)
