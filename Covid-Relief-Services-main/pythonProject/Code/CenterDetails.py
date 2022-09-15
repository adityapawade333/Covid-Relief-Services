import mysql.connector as connector

class CenterDetails:
    def __init__(self):
        self.con = connector.connect(host='localhost', port='3306', user='root', password='password', database='covidrelief', auth_plugin='mysql_native_password')

        query='create table if not exists centers(center VARCHAR(50) PRIMARY KEY, mobile VARCHAR(20), address VARCHAR(500), type VARCHAR(20) )'
        self.cur=self.con.cursor()
        self.cur.execute(query)

    def insert_center(self, center, mobile, address, type):
        query= "INSERT INTO centers values('{}', '{}', '{}', '{}')".format(center, mobile, address, type)
        self.cur.execute(query)
        self.con.commit()

    def delete_center(self, center):
        query= "DELETE FROM centers WHERE center = '{}'".format(center)
        self.cur.execute(query)
        self.con.commit()
        
    def update_center(self, center, mobile, address, type):
        query= "Update centers SET mobile='{}' , address='{}', type='{}' WHERE center='{}'".format(mobile, address, type, center)
        self.cur.execute(query)
        self.con.commit()

# cd = CenterDetails()
# cd.insert_center("Kasturba Specility Hospital", "77 22 091 200", "A/99, Kasturba Society Off Lohegaon Airport Road, Near St.Francis (Janta) School, Vishrantwadi, Pune - 411015, Maharashtra, India", "beds and oxygen")