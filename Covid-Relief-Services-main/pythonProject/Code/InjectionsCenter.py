import mysql.connector as connector

class InjectionsCenter:
    def __init__(self):
        self.con = connector.connect(host='localhost', port='3306', user='root', password='password', database='covidrelief', auth_plugin='mysql_native_password')

        query='create table if not exists injectionscenter(center VARCHAR(50) PRIMARY KEY, injection_name VARCHAR(15), cost VARCHAR(10), FOREIGN KEY(center) REFERENCES centers(center) ON DELETE CASCADE)'
        self.cur=self.con.cursor()
        self.cur.execute(query)

    def insert_center(self, center, injection_name, cost):
        query= "INSERT INTO injectionscenter values('{}', '{}', '{}')".format(center, injection_name, cost)
        self.cur.execute(query)
        self.con.commit()
        
    def update_center(self, center, injection_name, cost):
        query= "Update injectionscenter SET injection_name='{}', cost='{}' WHERE center='{}'".format(injection_name, cost, center)
        self.cur.execute(query)
        self.con.commit()

    def getdata(self):
        query= "SELECT injectionscenter.*, centers.mobile, centers.address FROM injectionscenter INNER JOIN centers ON injectionscenter.center = centers.center"
        self.cur.execute(query)
        
        data = list()
        for row in self.cur:
            data.append(row)

        return data

# ic = InjectionsCenter()
# ic.update_center("Datta Medical", "Remdesivir", "1100")
