import psycopg2
import os
from dotenv import load_dotenv
import random


data = {
    'production' : {
        "amount" : 4,
        "production_name" : {
            "type" : "normal",
            "values": ["simon","Derirmont","witirement"]
        }
    },

    'user_admin' : {
        "amount" : 4,
        "full_name" : {
            "type" : "normal",
            "values" : ["Sergeev Dmitry Urievich", "Somonkov Andrey Petrovich" ,"Solomankov Igor Dmitrievich"]
        },
        "user_role" : {
            "type" : "normal",
            "values" : ["admin", "plumber"]
        },
        "user_login" : {
            "type" : "normal",
            "values" : ["safsdfaf", "pluasfsadfdsmber","dfasfadsf"]
        },
        "user_password" : {
            "type" : "normal",
            "values" : ["admasdfasdfin", "asdfsdf","afsdfsadf"]
        },
        "production_id" : {
            "type" : "id",
            "values" : ["admin", "plumber"]
        },
    },

    'shop' : {
        "amount" : 4,
        "production_id" : {
            "type" : "id",
            "values" : ["none"]
        },
        "shop_name" : {
            "type" : "normal",
            "values" : ["big shop","small shop", "smth shop"]
        },
    },

    'worker' : {
        "amount" : 4,
        "full_name" : {
            "type" : "normal",
            "values" : ["big shop","small shop", "smth shop"]
        },
        "phone_number" : {
            "type" : "normal",
            "values" : ["big shop","small shop", "smth shop"]
        },
        "position" : {
            "type" : "normal",
            "values" : ["big shop","small shop", "smth shop"]
        },
        "worker_login" : {
            "type" : "normal",
            "values" : ["big shop","small shop", "smth shop"]
        },
        "worker_password" : {
            "type" : "normal",
            "values" : ["big shop","small shop", "smth shop"]
        },
    },

    'machine_types' : {
        "amount" : 4,
        "type_name" : {
            "type" : "normal",
            "values" : ["laser","fraser", ]
        },
    },

    'machines' :{
        "amount" : 4,
        "machine_name" : {
            "type" : "normal",
            "values" : ["big shop","small shop", "smth shop"]
        },
        "machine_type_id" : {
            "type" : "id",
            "values" : ["big shop","small shop", "smth shop"]
        },
        "machine_state" : {
            "type" : "normal",
            "values" : ["big shop","small shop", "smth shop"]
        },
        "tablet_id" : {
            "type" : "normal",
            "values" : ["big shop","small shop", "smth shop"]
        },

    },

    'worker_to_machine' : {
        "amount" : 4,
        "shop_id" : {
            "type" : "id",
            "values" : ["big shop","small shop", "smth shop"]
        },
        "worker_id" : {
            "type" : "id",
            "values" : ["big shop","small shop", "smth shop"]
        },

        "machine_id" : {
            "type" : "id",
            "values" : ["big shop","small shop", "smth shop"]
        },
    },

    'machine_workplace' : {
        "amount" : 4,
        "machine_workplace_name" : {
            "type" : "normal",
            "values" : ["big shop","small shop", "smth shop"]
        },
        "machine_id" : {
            "type" : "id",
            "values" : ["big shop","small shop", "smth shop"]
        },
    },

    'sensors' : {
        "amount" : 4,
        "machine_id" : {
            "type" : "id",
            "values" : ["big shop","small shop", "smth shop"]
        },
        "sensor_name" : {
            "type" : "normal",
            "values" : ["wonk","comsmp", "ddt"]
        },
        "position" : {
            "type" : "normal",
            "values" : [list(map(str,range(0,1000)))]
        },
        "sensor_value" : {
            "type" : "id",
            "values" : ["big shop","small shop", "smth shop"]
        },
        "sensor_type_name" : {
            "type" : "normal",
            "values" : ["wonk","small shop", ""]
        },
    },

    
    
    'sensors_by_types' : {
        "amount" : 4,
        "machine_type_id" : {
            "type" : "id",
            "values" : ["big shop","small shop", "smth shop"]
        },
        "units_of_measurment" : {
            "type" : "normal",
            "values" : ["big shop","small shop", "smth shop"]
        },
        "position" : {
            "type" : "id",
            "values" : ["big shop","small shop", "smth shop"]
        },
    }


}




def fill_db_with_data(dotenv_path):

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
                    
                    table_columns_data = data[table_name]

                    amount_of_times = table_columns_data["amount"]

                    table_columns = [column for column in table_columns_data if column != 'amount']

                    
 
                    random_values = [table_columns_data[column]["values"] for column in table_columns]
                    ones_that_must_be_incremented = [ False if table_columns_data[column]["type"] != "id" else True for column in table_columns ]

                    #  amount_of_times - amount of times to add to table
                    # table_columns[column] - names of columns
                    # random_values[column][(int(random.random()*100)%len(random_values[column]))] - random column value

                    names  = ",".join([table_columns[column] for column in range(len(table_columns))])

                    values = ""

                    
                
                    

                    def get_values():
                        
                        i = 0

                        return_mas = [] 

                        for column in range(len(table_columns)):
                            if not ones_that_must_be_incremented[column]:
                                return_mas.append("'" + random_values[column][(int(random.random()*100)%len(random_values[column]))]  + "'")
                            else:
                                i += 1
                                return_mas.append(str(i))

                        return return_mas

                    
                    for _ in range(amount_of_times):

                        values = ",".join(get_values())
                        print(f"insert into {table_name} ({names}) values ({values})")
                        cursor.execute(f"insert into {table_name} ({names}) values ({values})")
            
            print("db filled)")

    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

