import mysql.connector
from mysql.connector import Error

def DBconnection(hostname, uname, pwd, dbname):
    try:
        con = mysql.connector.connect(
            host = hostname,
            user = uname,
            password = pwd,
            database = dbname
         )
        print("Connection successfull")
    except Error as e:
        print("Connection Unsuccessful")
    return con

# Execute query funciton to read the rows from table
def execute_read_query(con, sql):
    mycursor = con.cursor(dictionary=True)
    rows = None
    try: #trying to capture the right result or not, may need to use the exception case
        mycursor.execute(sql)
        rows = mycursor.fetchall() #looking at the row variables
        return rows
    except Error as e:
        print("Errors is: ", e)

# Execute query Function to insert the rows into table
def execute_update_query(con, sql):
    mycursor = con.cursor()
    try:
        mycursor.execute(sql)
        con.commit()
        print("DB update successful")
    except Error as e:
        print("Error is:", e)

# everything from class notes week4