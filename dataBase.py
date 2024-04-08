import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    # database="uzbgram"
    database="kunUzParser"
    )
mycursor = mydb.cursor()
    

def createDB():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE kunUzParser")
# createDB()
def createTables():
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE region (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100))")
    mycursor.execute("CREATE TABLE category (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100))")
    print('tables created !')

def dropTables():
    mycursor.execute("SHOW TABLES")
    table_list = []
    for x in mycursor:
        table_list.append(x[0])
    print('tables',table_list)
    for i in table_list:
        mycursor.execute(f"DROP TABLE {i}")
        # mycursor.execute(f"DROP TABLE region")

    print('dropping succes !')
    

def runningDB():
    # createDB()
    createTables()

if __name__=='__main__':

    runningDB()
    # dropTables()


# news
    # image
    # title
    # short_content
    # created_at
    # full_content
    # original_url 
    # region_id
    # category_id
    # author
    # korishlar soni
