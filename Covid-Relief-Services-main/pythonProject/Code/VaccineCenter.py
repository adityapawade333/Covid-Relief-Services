import mysql.connector as connector

class VaccineCenter:
    def __init__(self):
        self.con = connector.connect(host='localhost', port='3306', user='root', password='password', database='covidrelief', auth_plugin='mysql_native_password')

        query='create table if not exists vaccinecenter(center VARCHAR(50) PRIMARY KEY, vaccine_name VARCHAR(15), cost VARCHAR(10), FOREIGN KEY(center) REFERENCES centers(center) ON DELETE CASCADE)'
        self.cur=self.con.cursor()
        self.cur.execute(query)

    def insert_center(self, center, vaccine_name, cost):
        query= "INSERT INTO vaccinecenter values('{}', '{}', '{}')".format(center, vaccine_name, cost)
        self.cur.execute(query)
        self.con.commit()
        
    def update_center(self, center, vaccine_name, cost):
        query= "Update vaccinecenter SET vaccine_name='{}', cost='{}' WHERE center='{}'".format(vaccine_name, cost, center)
        self.cur.execute(query)
        self.con.commit()

    def getdata(self):
        query= "SELECT vaccinecenter.*, centers.mobile, centers.address FROM vaccinecenter INNER JOIN centers ON vaccinecenter.center = centers.center"
        self.cur.execute(query)
        
        data = list()
        for row in self.cur:
            data.append(row)

        return data


# vc = VaccineCenter()
# vc.insert_center("Yerwada Late. Rajiv Gandhi Hospital", "Covishield", "600")
