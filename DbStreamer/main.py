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

    def upvote_question(self, user_id, question_id):
        sql1 = "insert into QuestionVotes (user_id, question_id) values (%s, %s);"
        sql2 = "update Questions set upvotes = upvotes+1 where id = %s;"
        val1 = (user_id, question_id)
        val2 = (question_id)
        _cursor = self.conn.cursor()
        _cursor.execute(sql1, (val1))
        _cursor.execute(sql2, (val2, ))
        results = _cursor.fetchall()
        return results

    def upvote_answer(self, user_id, answer_id):
        sql1 = "insert into AnswerVotes (user_id, answer_id) values (%s, %s);"
        sql2 = "update Answers set upvotes = upvotes+1 where id = %s;"
        val1 = (user_id, answer_id)
        val2 = (answer_id)
        _cursor = self.conn.cursor()
        _cursor.execute(sql1, (val1))
        _cursor.execute(sql2, (val2, ))
        results = _cursor.fetchall()
        return results

    def search_question(self, title):
        sql = """
        select * from Questions
        where title like concat("%", %s, "%");
        """
        val = (title)
        _cursor = self.conn.cursor()
        _cursor.execute(sql, (val, ))
        results = _cursor.fetchall()
        return results

    def search_question_by_id(self, id):
        sql = "select * from Questions where id = %s;"
        val = (id)
        _cursor = self.conn.cursor()
        _cursor.execute(sql, (val, ))
        results = _cursor.fetchall()
        return results

    def search_answers(self, id):
        sql = "select * from Answers where question_id = %s order by upvotes DESC;"
        val = (id)
        _cursor = self.conn.cursor()
        _cursor.execute(sql, (val, ))
        results = _cursor.fetchall()
        return results

    def search_by_tag(self, tag):
        sql = "select * from Tags where name = %s;"
        val = (tag)
        _cursor = self.conn.cursor()
        _cursor.execute(sql, (val, ))
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
