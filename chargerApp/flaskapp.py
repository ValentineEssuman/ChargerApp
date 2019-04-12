import sqlite3
if not os.path.isfile('powerdata.db'):
    conn = sqlite3.connect('powerdata.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE powerdata(
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        API_key text,
        date_time text,
        mac text,
        field1 integer,
        sdata real,
        field2 integer,
        gdata real,
        field3 integer,
        bdata real
        )""")
    conn.commit()

app = Flask(__name__)

@app.route("/")
def update(api_key, mac, field1, field2, field3, sdata, gdata, bdata):
      if(api_key == API_key and mac == MAC):
            print('Confiuration checks')
            fields = [field1, field2, field3]
            print("fields: ", fields)
            data = [sdata, gdata, bdata]
            print("data:", data)
            print("Connecting to database")
            conn = sqlite3.connect('powerdata.db')
            c = conn.cursor()
            time = datetime.datetime.now(tz=pytz.timezone('Africa/Accra'))
            date_time_str = time.isoformat()

            c.execute("INSERT INTO powerdata VALUES(:Id, :API_key, :datetim$
            conn.commit()
            c.close()
            conn.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
