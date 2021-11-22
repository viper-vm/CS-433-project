import mysql.connector as mysql


class DbStreamer:
    def __init__(self, host, user, password, database):
        mysql.connect(host='localhost', user='root', password='0000')
        self.conn = mysql.connect(
            host=host, user=user, passwd=password, db=database)
        return

    def get_connection(self):
        return self.conn

    def close_connection(self):
        self.conn.commit()
        self.conn.close()
        return

    def run_my_query(self, command):
        _cursor = self.conn.cursor()
        _cursor.execute(command)
        results = _cursor.fetchall()
        return results

    def initialize_database(self):
        self.run_my_query("drop database if exists mydb;")
        self.run_my_query("create database mydb;")
        self.run_my_query("use mydb;")

    def connect_database(self):
        self.run_my_query("use mydb;")

    def insert_into_users(self, id, name, email, password):
        sql = "insert into Users (id, name, email, password) values (%s, %s, %s, %s);"
        val = (id, name, email, password)
        _cursor = self.conn.cursor()
        _cursor.execute(sql, (val))
        results = _cursor.fetchall()
        return results

    def insert_into_questions(self, title, description, user_id):
        sql = "insert into Questions (title, description, user_id) values ( %s, %s, %s);"
        val = (title, description, user_id)
        _cursor = self.conn.cursor()
        _cursor.execute(sql, (val))
        results = _cursor.fetchall()
        return results

    def insert_into_answers(self, description, question_id, user_id):
        sql = "insert into Answers (description, question_id, user_id) values ( %s, %s, %s);"
        val = (description, question_id, user_id)
        _cursor = self.conn.cursor()
        _cursor.execute(sql, (val))
        results = _cursor.fetchall()
        return results

    def insert_into_tags(self, name, question_id):
        sql = "insert into Tags (name, question_id) values (%s, %s);"
        val = (name, question_id)
        _cursor = self.conn.cursor()
        _cursor.execute(sql, (val))
        results = _cursor.fetchall()
        return results

    def update_question(self, id, description):
        sql = "update Questions set description = %s where id = %s;"
        val = (description, id)
        _cursor = self.conn.cursor()
        _cursor.execute(sql, (val))
        results = _cursor.fetchall()
        return results

    def delete_question(self, id):
        res = self.run_my_query(
            "select id from Answers where question_id = "+str(id)+";")
        for i in res:
            self.delete_answer(i[0])

        sql1 = "delete from QuestionVotes where question_id = %s;"
        sql2 = "delete from Tags where question_id = %s;"
        sql3 = "delete from Questions where id = %s;"
        val = (id)
        _cursor = self.conn.cursor()
        _cursor.execute(sql1, (val, ))
        _cursor.execute(sql2, (val, ))
        _cursor.execute(sql3, (val, ))
        results = _cursor.fetchall()
        return results

    def update_answer(self, id, description):
        sql = "update Answers set description = %s where id = %s;"
        val = (description, id)
        _cursor = self.conn.cursor()
        _cursor.execute(sql, (val))
        results = _cursor.fetchall()
        return results

    def delete_answer(self, id):
        sql1 = "delete from AnswerVotes where answer_id = %s;"
        sql2 = "delete from Answers where id = %s;"
        val = (id)
        _cursor = self.conn.cursor()
        _cursor.execute(sql1, (val, ))
        _cursor.execute(sql2, (val, ))
        results = _cursor.fetchall()
        return results

    def get_tables(self):
        sql = "SHOW TABLES;"
        _cursor = self.conn.cursor()
        _cursor.execute(sql)
        data = _cursor.fetchall()
        for i in data:
            print(i[0])
            res = self.run_my_query("select * from "+i[0])
            for j in res:
                print(j)
            print()
