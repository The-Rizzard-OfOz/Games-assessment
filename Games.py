# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'Game_Assessment.db'

def print_query(view_name:str):
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    # Get the results from the view
    sql = "SELECT * FROM '" + view_name + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Get the field names to use as headings
    field_names = "SELECT name from pragma_table_info('" + view_name + "') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    # Print the results in a table with the headings
    print(tabulate(results,headings))
    db.close()

TABLES = (' Games '
          ' LEFT JOIN Original_platforms ON Games.Platform_ID = Original_platforms.Platform_ID '
          ' LEFT JOIN Publisher ON Games.Publisher_ID = Publisher.Publisher_ID ')

def print_parameter_query(fields:str, where:str, parameter):
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    sql = ('SELECT ' + fields + ' FROM ' + TABLES + ' WHERE ' + where)
    cursor.execute(sql,(parameter,))
    results = cursor.fetchall()
    print(tabulate(results,fields.split(',')))
    db.close()

Original_platforms = input('What platform do you want to see: ')
print_parameter_query('Year, Game, Genre', 'Original_platforms = ? ORDER by Year DESC',Original_platforms)