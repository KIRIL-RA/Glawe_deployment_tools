import os
import random

import psycopg2
from dotenv import load_dotenv

machines = {
    "laser_machine_type_1" : {
        'machine_types' : {
            "amount" : 1,
            "type_name" : {
                "type" : "normal",
                "values" : ["laser"]
            },
        },

        'machines' :{
            "amount" : 1,
            "machine_name" : {
                "type" : "normal",
                "values" : ["Laser"]
            },
            "machine_type_id" : {
                "type" : "normal",
                "values" : ["1"]
            },
            "machine_state" : {
                "type" : "normal",
                "values" : ["working..."]
            },
            "tablet_id" : {
                "type" : "normal",
                "values" : ["Coinsdciwcs","dsfuvoioaj","casc"]
            },

        },

        'worker_to_machine' : {
            "amount" : 1,
            "shop_id" : {
                "type" : "normal",
                "values" : [1,2]
            },
            "worker_id" : {
                "type" : "normal",
                "values" : [1,2]
            },

            "machine_id" : {
                "type" : "normal",
                "values" : [1,2]
            },
        },

        'machine_workplace' : {
            "amount" : 1,
            "machine_workplace_name" : {
                "type" : "normal",
                "values" : ["Intel","Lenovo","Apple"]
            },
            "machine_id" : {
                "type" : "id",
                "values" : ["big shop","small shop", "smth shop"]
            },
        },

        'sensors' : {
            "amount" : 1,
            "machine_id" : {
                "type" : "id",
                "values" : []
            },
            "sensor_name" : {
                "type" : "normal",
                "values" : ["Consump"]
            },
            "position" : {
                "type" : "normal",
                "values" : list(map(int,range(0,1000)))
            },
            "sensor_value" : {
                "type" : "normal",
                "values" : list(map(int,range(0,1000)))
            },
            "sensor_type_name" : {
                "type" : "normal",
                "values" : ["Consumption of energy"]
            },
        },

         'sensors' : {
            "amount" : 1,
            "machine_id" : {
                "type" : "id",
                "values" : []
            },
            "sensor_name" : {
                "type" : "normal",
                "values" : ["Lamp_time"]
            },
            "position" : {
                "type" : "normal",
                "values" : list(map(int,range(0,1000)))
            },
            "sensor_value" : {
                "type" : "normal",
                "values" : list(map(int,range(0,1000)))
            },
            "sensor_type_name" : {
                "type" : "normal",
                "values" : ["lamp time working"]
            },
        },

         'sensors' : {
            "amount" : 1,
            "machine_id" : {
                "type" : "id",
                "values" : []
            },
            "sensor_name" : {
                "type" : "normal",
                "values" : ["laset_mp"]
            },
            "position" : {
                "type" : "normal",
                "values" : list(map(int,range(0,1000)))
            },
            "sensor_value" : {
                "type" : "normal",
                "values" : list(map(int,range(0,1000)))
            },
            "sensor_type_name" : {
                "type" : "normal",
                "values" : ["laser mp"]
            },
        },


        'sensors_by_types' : {
            "amount" : 1,
            "machine_type_id" : {
                "type" : "id",
                "values" : []
            },
            "units_of_measurment" : {
                "type" : "normal",
                "values" : ["Lamp","consomp", "laset mt"]
            },
            "position" : {
                "type" : "id",
                "values" : []
            },
        },
        
    },

    "laser_machine_type_2" : {
        'machine_types' : {
            "amount" : 1,
            "type_name" : {
                "type" : "normal",
                "values" : ["laser"]
            },
        },

        'machines' :{
            "amount" : 1,
            "machine_name" : {
                "type" : "normal",
                "values" : ["Laser"]
            },
            "machine_type_id" : {
                "type" : "normal",
                "values" : ["1"]
            },
            "machine_state" : {
                "type" : "normal",
                "values" : ["working..."]
            },
            "tablet_id" : {
                "type" : "normal",
                "values" : ["Coinsdciwcs","dsfuvoioaj","casc"]
            },

        },

        'worker_to_machine' : {
            "amount" : 1,
            "shop_id" : {
                "type" : "normal",
                "values" : [1,2]
            },
            "worker_id" : {
                "type" : "normal",
                "values" : [1,2]
            },

            "machine_id" : {
                "type" : "normal",
                "values" : [1,2]
            },
        },

        'machine_workplace' : {
            "amount" : 1,
            "machine_workplace_name" : {
                "type" : "normal",
                "values" : ["Intel","Lenovo","Apple"]
            },
            "machine_id" : {
                "type" : "id",
                "values" : ["big shop","small shop", "smth shop"]
            },
        },

        'sensors' : {
            "amount" : 1,
            "machine_id" : {
                "type" : "id",
                "values" : []
            },
            "sensor_name" : {
                "type" : "normal",
                "values" : ["consump"]
            },
            "position" : {
                "type" : "normal",
                "values" : list(map(int,range(0,1000)))
            },
            "sensor_value" : {
                "type" : "normal",
                "values" : list(map(int,range(0,1000)))
            },
            "sensor_type_name" : {
                "type" : "normal",
                "values" : ["Consumption of energy"]
            },
        },

         'sensors' : {
            "amount" : 1,
            "machine_id" : {
                "type" : "id",
                "values" : []
            },
            "sensor_name" : {
                "type" : "normal",
                "values" : ["sp0"]
            },
            "position" : {
                "type" : "normal",
                "values" : list(map(int,range(0,1000)))
            },
            "sensor_value" : {
                "type" : "normal",
                "values" : list(map(int,range(0,1000)))
            },
            "sensor_type_name" : {
                "type" : "normal",
                "values" : ["Speed of spa"]
            },
        },

        


        'sensors_by_types' : {
            "amount" : 1,
            "machine_type_id" : {
                "type" : "id",
                "values" : []
            },
            "units_of_measurment" : {
                "type" : "normal",
                "values" : ["consump","sp0"]
            },
            "position" : {
                "type" : "id",
                "values" : []
            },
        },

    }
    


}




def fill_db_with_machines(dotenv_path):

    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    try:
        with psycopg2.connect(host=os.getenv("db_host"),
                              user=os.getenv("db_user"), 
                              password=os.getenv("db_password"), 
                              dbname=os.getenv("db_name")) as conn:
            with conn.cursor() as cursor:
                for data in machines:
                    for table in machines[data]:
                        table_name = table

                        table_columns_data = machines[data][table_name]

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
                                    return_mas.append("'" + str(random_values[column][(int(random.random()*100)%len(random_values[column]))])  + "'")
                                else:
                                    i += 1
                                    return_mas.append(str(i))

                            return return_mas

                        
                        for _ in range(amount_of_times):

                            values = ",".join(get_values())
                            print(f"insert into {table_name} ({names}) values ({values})")
                            cursor.execute(f"insert into {table_name} ({names}) values ({values})")
                            conn.commit()
            print("added machines )")

    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

