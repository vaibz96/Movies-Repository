import os
from collections import defaultdict
from prettytable import PrettyTable
import csv
import sqlite3
import os

def field1():
    return ['Movie', 'Show Time', 'Tickets']

def field2():
    return ['Movie', 'Tickets']

def field3():
    return ['Show Time', 'Tickets']

def file_reader(path, num_field, sep, header=False):
    """ Open the file path safely """
    try:
        fp = open(path, 'r+', encoding="utf-8")
    except FileNotFoundError:
        raise ValueError("Cant' open, {} not found".format(path))
    else:
        with fp:
            lines = fp.readlines()
            for i, line in enumerate(lines):
                field = line.rstrip("\n").split(sep)
                if len(field) == num_field:
                    if header == True and i == 0:
                        """ The continue will continue to next line and skip the first line if its a header"""
                        continue
                    else:
                        yield field
                else:
                    raise ValueError("{} has {} fields but on line {} expected {}".format(path, len(field), i, num_field))

def text_file(db_file):
    """this function will create a new file as text for the analysis, I created this
       file because I wanted to store the data in the database into comma separated value
       and DataGrip by somewhat does not support pipe separated value in the "value separator" 
       section I tried a lot but could not implement it so chose to do it this way"""

    """ Please sepcify the the file path in which the text file is present and run it once 
       to create the alternative text file that can be read in datagrip
       should work for any file_read because the yield function stores the value in a list which is comma separated"""

    path = r'C:\Users\shanb\PycharmProjects\Old_810_SSW\ticket_sales.txt'
    num_field = 3
    sep = '|'
    table = file_reader(path, num_field, sep, header = True)
    with open(db_file, 'w') as output:
        writer = csv.writer(output, lineterminator = '\n')
        writer.writerows(table)

def Movie_Tickets(DB_file):
    
    db = sqlite3.connect(DB_file)

    query1 = """select DISTINCT Movie, Time, SUM(seats) Tickets from ticket_sales1_1
                GROUP BY Movie, Time
                ORDER BY Movie, Time;"""

    pt = PrettyTable(field_names=field1())
    for c in db.execute(query1):
        pt.add_row(c)
    print("Movies and Show Times")
    return pt

def Movies(DB_file):

    db = sqlite3.connect(DB_file)
    
    query2 = """select distinct Movie, sum(Seats) Tickets from ticket_sales1_1
                group by  movie
                order by movie;"""

    pt = PrettyTable(field_names=field2())
    for c in db.execute(query2):
        pt.add_row(c)
    print("Movies")
    return pt

def Show_time(DB_file):

    db = sqlite3.connect(DB_file)

    query3 = """select distinct time 'Show Time' , sum(Seats) Tickets from ticket_sales1_1
                group by  time
                order by time;"""

    pt = PrettyTable(field_names=field3())
    for c in db.execute(query3):
        pt.add_row(c)
    print("Show Times")
    return pt

def main():
    file_reader(r'C:\Users\shanb\PycharmProjects\Old_810_SSW\ticket_sales.txt', 3, '|', header = True)

    """ Specify the database file path, the db_file below will directly store the data in the database with the 
        the latest file type so that the data can be imported into the database file in DataGrip"""

    #db_file = r'C:\Users\shanb\Final_database\ticket_sales.txt'

    """ After running the text_file function please call it in the main function"""

    #text_file(db_file)
    DB_file = r"C:\Users\shanb\Final_database\final.db"
    return print(Movie_Tickets(DB_file)), print(Movies(DB_file)), print(Show_time(DB_file))

if __name__ == '__main__':
    main()

