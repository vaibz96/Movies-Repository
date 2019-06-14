import unittest
from Final_code import *


class Test_Movie_Tickets(unittest.TestCase):
    def test_movie_Tickets(self):
        DB_file = r"C:\Users\shanb\Final_database\final.db"

        db = sqlite3.connect(DB_file)

        query1 = """select DISTINCT Movie, Time, SUM(seats) Tickets from ticket_sales1_1
                GROUP BY Movie, Time
                ORDER BY Movie, Time;"""

        table = []

        for c in db.execute(query1):
            table.append(c)

        expected = [('Avengers: PythonGame', '21:00', 3),
                    ('Avengers: PythonGame', '22:00', 6),
                    ('Java Halloween Massacre', '14:00', 2),
                    ('Java Jokes', '14:00', 8),
                    ('Java Jokes', '20:00', 2),
                    ('Python Wars: the last Jedi', '22:00', 4),
                    ('The Last Pythonista', '21:00', 5),
                    ('The Last Pythonista', '22:00', 6)]

        self.assertEqual(table, expected)

class Test_Movies(unittest.TestCase):
    def test_movies(self):
        DB_file = r"C:\Users\shanb\Final_database\final.db"

        db = sqlite3.connect(DB_file)

        query2 = """select distinct Movie, sum(Seats) Tickets from ticket_sales1_1
                group by  movie
                order by movie;"""

        table = []

        for c in db.execute(query2):
            table.append(c)

        expected = [('Avengers: PythonGame', 9), 
                    ('Java Halloween Massacre', 2),
                    ('Java Jokes', 10 ),
                    ('Python Wars: the last Jedi', 4),
                    ('The Last Pythonista', 11)]

        self.assertEqual(table, expected)

class Test_Show_Time(unittest.TestCase):
    def test_show_time(self):
        DB_file = r"C:\Users\shanb\Final_database\final.db"

        db = sqlite3.connect(DB_file)

        query3 = """select distinct time 'Show Time' , sum(Seats) Tickets from ticket_sales1_1
                group by  time
                order by time;"""

        table = []

        for c in db.execute(query3):
            table.append(c)

        expected = [('14:00', 10),
                    ('20:00', 2),
                    ('21:00', 8),
                    ('22:00', 16)]

        self.assertEqual(table, expected)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
    