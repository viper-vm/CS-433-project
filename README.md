# cs-432-databases-assignment-4

[**Statement**](https://docs.google.com/document/d/1A71z9YLwowCPuedxv1cTsyJdlE8_b1TQbj0tJgXL3rM/edit?usp=sharing)

## How to run?

- Run the schema.py(`make schema`) first which will
  - initialize the database
  - create required schemas
- `make ques`: to perform each query
- `make all`: Doing both of the above steps

## Helper docs:

- https://pypi.org/project/mysql-connector-python/
- https://dev.mysql.com/downloads/connector/python/

## Respective output:
   
<pre>python3 schema.py
python3 Q1.py

python3 Q2.py
[]

python3 Q3.py
[(&apos;Book1&apos;, 220), (&apos;Book2&apos;, 220), (&apos;Book3&apos;, 200), (&apos;Book4mi&apos;, 200), (&apos;Book5&apos;, 200), (&apos;Cloth1&apos;, 700), (&apos;Cloth2&apos;, 700), (&apos;Cloth3&apos;, 700), (&apos;Cloth4mi&apos;, 700), (&apos;Cloth5&apos;, 700), (&apos;Book1&apos;, 200), (&apos;Book2&apos;, 200), (&apos;Book3&apos;, 200), (&apos;Book4&apos;, 200), (&apos;Book5&apos;, 200), (&apos;nextGenLeptop1&apos;, 7000), (&apos;nextGenLeptop2&apos;, 7000), (&apos;nextGenLeptop3&apos;, 12000), (&apos;nextGenLeptop4&apos;, 15000), (&apos;-dark-product-&apos;, 23000), (&apos;Deep inside Mysql Part 1&apos;, 7000), (&apos;Deep inside Mysql Part 2&apos;, 7000), (&apos;Deep inside Mysql Part 3&apos;, 7000), (&apos;Dell Super 009&apos;, 50000), (&apos;HP Bro 669&apos;, 60000), (&apos;Google XX 0&apos;, 70000)]

python3 Q5.py
[(&apos;9191919191&apos;, &apos;myemail1@gmail.com&apos;)]

python3 Q6.py
[(4, &apos;Book4mi&apos;, &apos;Novels&apos;, &apos;new&apos;, 1, &apos;best book&apos;, datetime.date(2020, 1, 1), datetime.datetime(2021, 2, 2, 0, 0), 200, None, &apos;Dan Dany&apos;), (9, &apos;Cloth4mi&apos;, &apos;Clothes&apos;, &apos;new&apos;, 2, &apos;shiny cloth&apos;, datetime.date(2020, 2, 9), datetime.datetime(2021, 2, 2, 0, 0), 700, None, &apos;Dan Dany&apos;)]
[(1,)]

python3 Q13.py
[(24, &apos;Dell Super 009&apos;, &apos;Electronics&apos;, &apos;Laptop&apos;, 1, &apos;old laptop&apos;, datetime.date(2020, 1, 1), datetime.datetime(2021, 2, 2, 0, 0), 50000, None, &apos;mark marko&apos;), (25, &apos;HP Bro 669&apos;, &apos;Electronics&apos;, &apos;Laptop&apos;, 2, &apos;light laptop&apos;, datetime.date(2020, 1, 1), datetime.datetime(2021, 2, 2, 0, 0), 60000, None, &apos;mark marko&apos;), (26, &apos;Google XX 0&apos;, &apos;Electronics&apos;, &apos;Laptop&apos;, 3, &apos;beta version&apos;, datetime.date(2020, 1, 1), datetime.datetime(2021, 2, 2, 0, 0), 70000, None, &apos;mark marko&apos;)]

python3 Q16.py
[(1, &apos;9191919191&apos;, &apos;myemail1@gmail.com&apos;), (3, &apos;9191919191&apos;, &apos;myemail3@gmail.com&apos;)]

python3 Q19.py
[(1,), (2,)]

python3 Q20.py
[(1, &apos;Book1&apos;, &apos;Novels&apos;, &apos;new&apos;, 1, &apos;best book&apos;, datetime.date(2020, 1, 1), datetime.datetime(2021, 2, 2, 0, 0), 220, 15, &apos;Dan Dany&apos;), (2, &apos;Book2&apos;, &apos;Novels&apos;, &apos;new&apos;, 1, &apos;best book&apos;, datetime.date(2020, 1, 1), datetime.datetime(2021, 2, 2, 0, 0), 220, 15, &apos;Dan Dany&apos;), (3, &apos;Book3&apos;, &apos;Novels&apos;, &apos;new&apos;, 1, &apos;best book&apos;, datetime.date(2020, 1, 1), datetime.datetime(2021, 2, 2, 0, 0), 200, 15, &apos;Dan Dany&apos;), (4, &apos;Book4mi&apos;, &apos;Novels&apos;, &apos;new&apos;, 1, &apos;best book&apos;, datetime.date(2020, 1, 1), datetime.datetime(2021, 2, 2, 0, 0), 200, 15, &apos;Dan Dany&apos;), (5, &apos;Book5&apos;, &apos;Novels&apos;, &apos;new&apos;, 1, &apos;best book&apos;, datetime.date(2020, 1, 1), datetime.datetime(2021, 2, 2, 0, 0), 200, 15, &apos;Dan Dany&apos;), (6, &apos;Cloth1&apos;, &apos;Clothes&apos;, &apos;new&apos;, 2, &apos;shiny cloth&apos;, datetime.date(2020, 2, 9), datetime.datetime(2021, 2, 2, 0, 0), 700, 15, &apos;Dan Dany&apos;), (7, &apos;Cloth2&apos;, &apos;Clothes&apos;, &apos;new&apos;, 2, &apos;shiny cloth&apos;, datetime.date(2020, 2, 9), datetime.datetime(2021, 2, 2, 0, 0), 700, 15, &apos;Dan Dany&apos;), (8, &apos;Cloth3&apos;, &apos;Clothes&apos;, &apos;new&apos;, 2, &apos;shiny cloth&apos;, datetime.date(2020, 2, 9), datetime.datetime(2021, 2, 2, 0, 0), 700, 15, &apos;Dan Dany&apos;), (9, &apos;Cloth4mi&apos;, &apos;Clothes&apos;, &apos;new&apos;, 2, &apos;shiny cloth&apos;, datetime.date(2020, 2, 9), datetime.datetime(2021, 2, 2, 0, 0), 700, 15, &apos;Dan Dany&apos;), (24, &apos;Dell Super 009&apos;, &apos;Electronics&apos;, &apos;Laptop&apos;, 1, &apos;old laptop&apos;, datetime.date(2020, 1, 1), datetime.datetime(2021, 2, 2, 0, 0), 50000, 15, &apos;mark marko&apos;), (25, &apos;HP Bro 669&apos;, &apos;Electronics&apos;, &apos;Laptop&apos;, 2, &apos;light laptop&apos;, datetime.date(2020, 1, 1), datetime.datetime(2021, 2, 2, 0, 0), 60000, 15, &apos;mark marko&apos;), (26, &apos;Google XX 0&apos;, &apos;Electronics&apos;, &apos;Laptop&apos;, 3, &apos;beta version&apos;, datetime.date(2020, 1, 1), datetime.datetime(2021, 2, 2, 0, 0), 70000, 15, &apos;mark marko&apos;)]

python3 Q21.py
[(&apos;Book1&apos;,), (&apos;Book2&apos;,), (&apos;Book3&apos;,), (&apos;Book4mi&apos;,), (&apos;Book5&apos;,), (&apos;Book1&apos;,), (&apos;Book2&apos;,), (&apos;Book3&apos;,), (&apos;Book4&apos;,), (&apos;Book5&apos;,)]
</pre>
