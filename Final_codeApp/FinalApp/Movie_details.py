from flask import Flask, render_template
import sqlite3
app = Flask(__name__)

@app.route('/Movie_Tickets Summary')
def Movie_tickets_Summary():
    DB_file = r"C:\Users\shanb\Final_database\final.db"
    db = sqlite3.connect(DB_file)

    query1 = """select DISTINCT Movie, Time, SUM(seats) Tickets from ticket_sales1_1
                GROUP BY Movie, Time
                ORDER BY Movie, Time;"""

    results = db.execute(query1)

    data = [{'movie' : movie, 'time': time, 'tickets': tickets}\
            for movie, time, tickets in results]

    return render_template('tables.html',
                            title = 'Movie_summary',
                            table_header = 'Movies and Show times',
                            movies_summary = data)

@app.route('/Movie_Summary')
def Movies_Summary():

    DB_file = r"C:\Users\shanb\Final_database\final.db"

    db = sqlite3.connect(DB_file)

    query2 = """select distinct Movie, sum(Seats) Tickets from ticket_sales1_1
                group by  movie
                order by movie;"""

    results = db.execute(query2)

    data = [{'movie' : movie, 'tickets': tickets}\
            for movie, tickets in results]

    return render_template('movies_table.html',
                            title = 'Movie Summary',
                            table_header = 'Movies',
                            movies = data)

@app.route('/Show_Time Summary')
def Show_Time_Summary():
    DB_file = r"C:\Users\shanb\Final_database\final.db"

    db = sqlite3.connect(DB_file)

    query3 = """select distinct time 'Show Time' , sum(Seats) Tickets from ticket_sales1_1
                group by  time
                order by time;"""

    results = db.execute(query3)

    data = [{'time' : time, 'tickets': tickets}\
            for time, tickets in results]

    return render_template('show_time.html',
                            title = 'Movie Summary',
                            table_header = 'Show Times',
                            show_time = data)

app.run(debug=True)
    