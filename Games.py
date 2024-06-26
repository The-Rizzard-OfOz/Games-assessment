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

menu_choice = ''
while menu_choice != 'Z':
    menu_choice = input('Welcome to the Games database\n\n'
                        'Type the letter for the information you want:\n'
                        'A: List all games made for PC\n'
                        'B: List all games made by Konami\n'
                        'C: List all games released before 1999\n'
                        'D: List all games made after 1999\n'
                        'E: List all games that are action\n'
                        "F: List all games that are shoot 'em up\n"
                        'Z: Exit \n\nType option here: ')
    menu_choice = menu_choice.upper()
    if menu_choice == 'A':
        print_query('All games made for PC')
    elif menu_choice == 'B':
        print_query('All games made by Konami')
    elif menu_choice == 'C':
        print_query('All games released before 1999')
    elif menu_choice == 'D':
        print_query('All games made after 1999')
    elif menu_choice == 'E':
        print_query('All games that are action')
    elif menu_choice == 'F':
        print_query("All games that are shoot 'em up")