import mysql.connector as connector

class OxygenBed:
    def __init__(self):
        self.con = connector.connect(host='localhost', port='3306', user='root', password='password', database='covidrelief', auth_plugin='mysql_native_password')

        query='create table if not exists oxygenbed(center VARCHAR(50) PRIMARY KEY, normal_beds INT, oxygen_beds INT, total_beds INT, FOREIGN KEY(center) REFERENCES centers(center) ON DELETE CASCADE)'
        self.cur=self.con.cursor()
        self.cur.execute(query)

    def insert_beds(self, center, beds, oxygen_beds, total):
        query= "INSERT INTO oxygenbed values('{}', {}, {}, {})".format(center, beds, oxygen_beds, total)
        self.cur.execute(query)
        self.con.commit()
        
    def update_beds(self, center, beds, oxygen_beds, total):
        query= "Update oxygenbed SET normal_beds={} , oxygen_beds={}, total_beds={} WHERE center='{}'".format(beds, oxygen_beds, total, center)
        self.cur.execute(query)
        self.con.commit()

    def getdata(self):
        query= "SELECT oxygenbed.*, centers.mobile, centers.address FROM oxygenbed INNER JOIN centers ON oxygenbed.center = centers.center"
        self.cur.execute(query)
        
        data = list()
        for row in self.cur:
            data.append(row)

        return data

# ox = OxygenBed()
# ox.insert_beds("Kasturba Specility Hospital", 10, 3, 13)