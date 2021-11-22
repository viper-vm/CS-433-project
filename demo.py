from DbStreamer.main import DbStreamer

obj = DbStreamer("localhost", "root", "0000", "mydb")
obj.connect_database()

obj.insert_into_users("a", "A", "a@iitgn.ac.in", "abcd")
obj.insert_into_users("b", "B", "b@iitgn.ac.in", "abcd")
obj.insert_into_users("C", "C", "c@iitgn.ac.in", "abcd")

obj.insert_into_questions('dummy title', 'dummy description', "a",)
obj.insert_into_questions('dummy title1', 'dummy description', "b",)
obj.insert_into_questions('dummy title2', 'dummy description', "c",)

obj.insert_into_answers("try restarting bro", 1, "a")
obj.insert_into_answers("try restarting bro", 1, "a")
obj.insert_into_answers("try restarting bro", 1, "a")
obj.insert_into_answers("try restarting bro", 2, "a")
obj.insert_into_answers("try restarting bro", 2, "a")
obj.insert_into_answers("try restarting bro", 2, "a")

obj.insert_into_tags("c++", 1)
obj.insert_into_tags("py", 2)
obj.insert_into_tags("java", 3)

obj.update_question(1, "okay bro")
obj.update_answer(1, "okay bro")

obj.delete_question(1)
obj.delete_answer(6)

obj.close_connection()
