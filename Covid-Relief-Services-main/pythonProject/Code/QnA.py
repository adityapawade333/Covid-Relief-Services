import mysql.connector as connector

class QnA:
    def __init__(self):
        self.con = connector.connect(host='localhost', port='3306', user='root', password='password', database='covidrelief', auth_plugin='mysql_native_password')

        query='create table if not exists qna(question VARCHAR(100) PRIMARY KEY, answer VARCHAR(500))'
        self.cur=self.con.cursor()
        self.cur.execute(query)

    def insert_question(self, question, answer):
        query= "INSERT INTO qna values('{}', '{}')".format(question, answer)
        self.cur.execute(query)
        self.con.commit()
        
    def update_question(self, question, answer):
        query= "Update qna SET answer='{}' WHERE question='{}'".format(answer, question)
        self.cur.execute(query)
        self.con.commit()

    def delete_question(self, question):
        query= "DELETE FROM qna WHERE question = '{}'".format(question)
        self.cur.execute(query)
        self.con.commit()

    def getdata(self):
        query= "SELECT * FROM qna"
        self.cur.execute(query)
        
        data = list()
        for row in self.cur:
            data.append(row)

        return data