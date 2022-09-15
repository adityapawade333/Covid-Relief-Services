import mysql.connector as connector

class TestingLabs:
    def __init__(self):
        self.con = connector.connect(host='localhost', port='3306', user='root', password='password', database='covidrelief', auth_plugin='mysql_native_password')

        query='create table if not exists testinglabs(center VARCHAR(50) PRIMARY KEY, available_tests VARCHAR(100), FOREIGN KEY(center) REFERENCES centers(center) ON DELETE CASCADE)'
        self.cur=self.con.cursor()
        self.cur.execute(query)

    def insert_tests(self, center, available_tests):
        query= "INSERT INTO testinglabs values('{}', '{}')".format(center, available_tests)
        self.cur.execute(query)
        self.con.commit()
        
    def update_tests(self, center, available_tests):
        query= "Update testinglabs SET available_tests='{}' WHERE center='{}'".format(available_tests, center)
        self.cur.execute(query)
        self.con.commit()

    def getdata(self):
        query= "SELECT testinglabs.*, centers.mobile, centers.address FROM testinglabs INNER JOIN centers ON testinglabs.center = centers.center"
        self.cur.execute(query)
        
        data = list()
        for row in self.cur:
            data.append(row)

        return data
# tl = TestingLabs()
# tl.insert_tests("Dr. Lal PathLabs", "RTPCR, Rapid Antigen")
