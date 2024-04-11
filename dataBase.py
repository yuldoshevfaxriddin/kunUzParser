import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
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
    # mycursor.execute("CREATE TABLE region (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100))")
    # mycursor.execute("CREATE TABLE category (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100))")
    mycursor.execute("""CREATE TABLE news (
                     id INT AUTO_INCREMENT PRIMARY KEY,
                     image VARCHAR(100),
                     meta_data VARCHAR(100),
                     original_url varchar(150),
                     title varchar(250),
                     content text
                     )""")
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

def showTables():
    mycursor.execute("SHOW TABLES")
    table_list = []
    for x in mycursor:
        table_list.append(x[0])
    print('tables',table_list)

def showData():
    mycursor.execute("SELECT * FROM news")
    myresult = mycursor.fetchall()
    for x in myresult:
          print(x)
   
      
def insertNews(news_list):
    for news in news_list:
        sql = f"""INSERT INTO `news`( `image`, `meta_data`, `original_url`, `title`, `content`) 
        VALUES ('{news['image']}','{news['meta-data']}','{news['original-url']}','{news['title']}','{news['content']}')"""
        mycursor.execute(sql)
        mydb.commit()
    print('inserting succes !')

def insertNewsTest():
    sql = f"""INSERT INTO `news`( `image`, `meta_data`, `original_url`, `title`, `content`) 
    VALUES ('asdas','wqeqw','qweqwe','qweqw','qweqwe')"""
    print(sql)
    mycursor.execute(sql)
    mydb.commit()
    print('inserting succes !')

def runningDB():
    # createDB()
    createTables()

if __name__=='__main__':

    # runningDB()
    # dropTables()
    # insertNewsTest()
    showTables()
    showData()


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
