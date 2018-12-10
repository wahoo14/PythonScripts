import sqlite3

sqlite_file = r'C:\Users\dyu\Documents\Other_Scripts\PythonScripts\Data Files\testDb.sqlite'
table_name1 = 'my_table_'
new_field = 'my_1st_column' # name of the column
field_type = 'INTEGER'  # column data type


# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

data = c.execute('SELECT * FROM my_table_;')
print(data.fetchall())

conn.commit()
conn.close()