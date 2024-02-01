import psycopg2
import os
from dotenv import load_dotenv
import random


data = {
    'production' : {
        "amount" : 4,
        "production_name" : {
            "values": ["simon","Derirmont","witirement"]
        }
    }
}



def delete_all_tables(dotenv_path):

    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    try:
        with psycopg2.connect(host=os.getenv("db_host"),
                              user=os.getenv("db_user"), 
                              password=os.getenv("db_password"), 
                              dbname=os.getenv("db_name")) as conn:
            with conn.cursor() as cursor:
                for table in data:
                    table_name = table
                    
                    table_rows_data = data[table_name]

                    table_rows = [row for row in table_rows_data if table_rows_data[row] != "amount"]
                    print(table_rows_data)

                    random_values = [table_rows_data[row]["values"] for row in table_rows]

                    for row in range(len(table_rows)):
                        print(table_rows[row],random_values[row][(int(random.random()*100)%len(random_values[row]))])
            
            print("db cleared)")

    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

delete_all_tables("../../.env")