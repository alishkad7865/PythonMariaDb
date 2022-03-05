import mariadb 

conn = mariadb.connect(
    user="username",
    password="password123456",
    host="localhost",
    database="mydb")
cur = conn.cursor() 

#retrieving information 
some_name = "test" 
cur.execute("SELECT * FROM students where rowKey=1;") 
print(cur,"cur")
for student_row in cur: 
    print(f"student row: {student_row}")
    print(f"First name: {student_row[1]}")
    
#insert information 
try: 
    cur.execute("INSERT INTO students (firstName,lastName,rowKey, studentId, AccountCreated) VALUES (?, ?, ?, ?, ?);", ("Maria","DB","2","200874563","4702")) 
except mariadb.Error as e: 
    print(f"Error: {e}")

conn.commit() 
print(f"Last Inserted ID: {cur.lastrowid}")
    
conn.close()