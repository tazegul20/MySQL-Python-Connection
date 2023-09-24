conn= connection.connect(
    host='localhost',
    user='root',
    password='22102001',
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
