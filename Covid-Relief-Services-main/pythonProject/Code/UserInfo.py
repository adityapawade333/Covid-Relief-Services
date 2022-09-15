import mysql.connector as connector

class UserInfo:
    def __init__(self):
        self.con = connector.connect(host='localhost', port='3306', user='root', password='password', database='covidrelief', auth_plugin='mysql_native_password')

        query='create table if not exists user(name VARCHAR(20), age INT, mobile VARCHAR(12), address VARCHAR(100), username VARCHAR(20) PRIMARY KEY, password VARCHAR(20) )'
        self.cur=self.con.cursor()
        self.cur.execute(query)

    #Insert
    def insert_user(self, name, age, mobile, address, username, password):
        query= "INSERT INTO user values('{}', {}, '{}', '{}', '{}', '{}')".format(name, age, mobile, address, username, password)
        self.cur.execute(query)
        self.con.commit()
    
    #Checking username and password
    def checkUsername(self, username, password):
        query= "SELECT * FROM user WHERE username='{}' AND password='{}'".format(username, password)
        self.cur.execute(query)
        rows = self.cur.fetchall()
        if not rows:
            return 0
        else: return 1

    def getdata(self):
        query= "SELECT * FROM user"
        self.cur.execute(query)

        data = list()
        for row in self.cur:
            data.append(row)

        return data

# user = UserInfo()
# user.insert_user("Shaunak Kayande", 20, "8446391068", "Gaddam Plots, Akola", "shaun", "shaun")
#print(user.checkUsername("shaun", "shaun"))