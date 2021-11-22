from DbStreamer.main import DbStreamer

obj = DbStreamer("localhost", "root", "0000", "mydb")
obj.connect_database()

obj.insert_into_users("a", "A", "a@iitgn.ac.in", "abcd")
obj.insert_into_users("b", "B", "b@iitgn.ac.in", "abcd")
obj.insert_into_users("c", "C", "c@iitgn.ac.in", "abcd")
obj.insert_into_users("d", "D", "d@iitgn.ac.in", "abcd")
obj.insert_into_users("e", "D", "e@iitgn.ac.in", "abcd")
obj.insert_into_users("f", "D", "f@iitgn.ac.in", "abcd")
obj.insert_into_users("g", "D", "g@iitgn.ac.in", "abcd")
obj.insert_into_users("h", "D", "h@iitgn.ac.in", "abcd")

obj.insert_into_questions('dummy title', 'dummy description', "a",)
obj.insert_into_questions('dummy title1', 'dummy description', "b",)
obj.insert_into_questions('dummy title2', 'dummy description', "c",)

obj.insert_into_answers("try restarting bro", 1, "a")
obj.insert_into_answers("try restarting bro", 1, "a")
obj.insert_into_answers("try restarting bro", 1, "a")
obj.insert_into_answers("throw the computer", 2, "b")
obj.insert_into_answers("change the OS", 2, "a")
obj.insert_into_answers("reinstall audio drivers", 2, "c")

obj.insert_into_tags("c++", 1)
obj.insert_into_tags("py", 2)
obj.insert_into_tags("java", 3)

obj.upvote_question("a", 1)
obj.upvote_question("b", 2)
obj.upvote_question("b", 3)

obj.upvote_answer("a", 4)
obj.upvote_answer("a", 5)
obj.upvote_answer("a", 6)
obj.upvote_answer("b", 4)
obj.upvote_answer("b", 5)
obj.upvote_answer("b", 6)
obj.upvote_answer("c", 4)
obj.upvote_answer("c", 5)
obj.upvote_answer("c", 6)
obj.upvote_answer("d", 4)
obj.upvote_answer("d", 5)
obj.upvote_answer("d", 6)
obj.upvote_answer("e", 5)
obj.upvote_answer("e", 6)
obj.upvote_answer("f", 6)

obj.update_question(1, "okay bro")
obj.update_answer(1, "okay bro")

obj.delete_question(1)
obj.delete_answer(1)

print(obj.search_question("dummy"))

print(obj.search_answers(2))

print(obj.search_by_tag("py"))

print(obj.search_question_by_id(2))

obj.close_connection()
