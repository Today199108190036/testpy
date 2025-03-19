# -*- coding: UTF-8 -*-
import pymysql
from pymysql import connect
import pandas as pd

con = connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    passwd="zx6923531",
    database="test",
    charset="utf8"
)
cursor = con.cursor()
cursor.execute("select * from test.score")
rows = cursor.fetchall()
df = pd.DataFrame(rows, columns=["id", "stu_id", "c_name", "grade"])
print(df.values)
cursor.close()
con.close()

