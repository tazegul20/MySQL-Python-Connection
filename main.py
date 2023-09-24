import pandas as pd
import mysql.connector as connection
conn= connection.connect(
    host='localhost',
    user='root',
    password='****',#This is the password you set before you create your database so please don't forget it
    database='sys'
)
query="""select*from gdp_csv
where Ulke_adi = "Turkey" and Year between 1990 and 2000;
"""
df=pd.read_sql(query,conn)

df.plot(df.columns[2],df.columns[3],marker='o', linestyle='-', color='b', label='GDP')
plt.title("Turkey's GDP")
plt.xlabel("year")
plt.ylabel("para")
plt.show()
