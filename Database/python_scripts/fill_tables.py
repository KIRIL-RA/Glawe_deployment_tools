import psycopg2
import os
from dotenv import load_dotenv
from datetime import datetime

# User data

data = {
    'production_1' : {
        "table_name" : "production",
        "production_name" : "Производство 1"
    },

    "user_admin_1": {
        "table_name" : "user_admin",
        "full_name" : "Boris Borisovich Luvintain",
        "user_role" : "Admin",
        "user_login" : "luwa@mail.com",
        "user_password" : "$2b$04$uJ3nyBMpJQv5JIxm8buCQumeaxlAp8ebmqHMHVoxafyB9PFK1WDeu", # real password : borisboris123
        "production_id" : "1",
    },

    'worker_1' : {
        "table_name" : "worker",
        "full_name" : "Semen Semenovich Tartikov",
        "phone_number" : "88005553535",
        "position" : "Beginer Worker",
        "worker_login" : "sema@mail.com",
        "worker_password" : "$2b$04$Kuw37SPoNr0uqVzy/h7jsee8o/Hf.KGTQZivXZKjrY3RiFTWt5UTy", # real password : SemenSemen123
    },

    "shop" : {
        "table_name" : "shop",
        "production_id" : "1",
        "shop_name" : "Цех обработки фанеры",
    },

    "machine_types_1" : {
        "table_name" : "machine_types",
        "type_name": "Лазерный"
    },

    'sensors_by_types_11' : {
        "table_name" : "sensors_by_types",
        "machine_type_id" : "1",
        "units_of_measurment" : "вт/ч",
        "port" : "122",
        "sensor_type_name" : "consmp"
    },

    'sensors_by_types_12' : {
        "table_name" : "sensors_by_types",
        "machine_type_id" : "1",
        "units_of_measurment" : "_",
        "port" : "1",
        "sensor_type_name" : "lmpwork"
    },

    'sensors_by_types_13' : {
        "table_name" : "sensors_by_types",
        "machine_type_id" : "1",
        "units_of_measurment" : "вт/ч",
        "port" : "10",
        "sensor_type_name" : "tubeconsmp"
    },

    "machines_1" :{
        "table_name" : "machines",
        "machine_name" : "Laser machine",
        "machine_type_id" : "1",
        "machine_state" : "working...",
        "tablet_id" : "aScasjcnzxc",
    },

    "sensors_11" : {
        "table_name" : "sensors",
        "machine_id" : "1",
        "sensor_name" : "consmp",
        "sensor_port" : "122",
        "sensor_value" : "1223",
        "sensor_type_id" : "1",
    },

    "sensors_12" : {
        "table_name" : "sensors",
        "machine_id" : "1",
        "sensor_name" : "lmpwork",
        "sensor_port" : "1",
        "sensor_value" : "1",
        "sensor_type_id" : "2",
    },

    "sensors_13" : {
        "table_name" : "sensors",
        "machine_id" : "1",
        "sensor_name" : "tubeconsmp",
        "sensor_port" : "10",
        "sensor_value" : "12321",
        "sensor_type_id" : "3",
    },

    'machine_workplace_1' : {
        "table_name" : "machine_workplace",
        "machine_workplace_name" : "NoName",
        "machine_id" : "1",
    },

    "machine_metrics11" : {
        "table_name" : "machine_metrics",
        "machine_id" : "1",
        "machine_metric_name" : "Энергопотребление",
        "machine_metric_type" : "energy_consumption",
        "machine_units_of_measurment" : "квт/ч",
        "machine_metric_value" : "0",
        "time_start" : str(datetime.now()),
        "time_end" : str(datetime.now()),
    },

    "machine_metrics12" : {
        "table_name" : "machine_metrics",
        "machine_id" : "1",
        "machine_metric_name" : "OEE",
        "machine_metric_type" : "oee",
        "machine_units_of_measurment" : "%",
        "machine_metric_value" : "0",
        "time_start" : str(datetime.now()),
        "time_end" : str(datetime.now()),
    },


    "machine_metrics13" : {
        "table_name" : "machine_metrics",
        "machine_id" : "1",
        "machine_metric_name" : "КПЭ",
        "machine_metric_type" : "kpe",
        "machine_units_of_measurment" : "%",
        "machine_metric_value" : "0",
        "time_start" : str(datetime.now()),
        "time_end" : str(datetime.now()),
    },

    "machine_metrics14" : {
        "table_name" : "machine_metrics",
        "machine_id" : "1",
        "machine_metric_name" : "Время работы",
        "machine_metric_type" : "work_time",
        "machine_units_of_measurment" : "мин",
        "machine_metric_value" : "0",
        "time_start" : str(datetime.now()),
        "time_end" : str(datetime.now()),
    },

    "machine_metrics15" : {
        "table_name" : "machine_metrics",
        "machine_id" : "1",
        "machine_metric_name" : "Машинное время",
        "machine_metric_type" : "machine_time",
        "machine_units_of_measurment" : "мин",
        "machine_metric_value" : "0",
        "time_start" : str(datetime.now()),
        "time_end" : str(datetime.now()),
    },

    "machine_metrics16" : {
        "table_name" : "machine_metrics",
        "machine_id" : "1",
        "machine_metric_name" : "Причины простоя",
        "machine_metric_type" : "stay_",
        "machine_units_of_measurment" : "%",
        "machine_metric_value" : "0",
        "time_start" : str(datetime.now()),
        "time_end" : str(datetime.now()),
    },

    "machine_metrics17" : {
        "table_name" : "machine_metrics",
        "machine_id" : "1",
        "machine_metric_name" : "Среднее время обработки",
        "machine_metric_type" : "avg_processsing_time",
        "machine_units_of_measurment" : "мин",
        "machine_metric_value" : "0",
        "time_start" : str(datetime.now()),
        "time_end" : str(datetime.now()),
    },

    "machine_metrics18" : {
        "table_name" : "machine_metrics",
        "machine_id" : "1",
        "machine_metric_name" : "Среднее время между обработкой",
        "machine_metric_type" : "vg_time_between_processing",
        "machine_units_of_measurment" : "мин",
        "machine_metric_value" : "0",
        "time_start" : str(datetime.now()),
        "time_end" : str(datetime.now()),
    },


    "machine_metrics19" : {
        "table_name" : "machine_metrics",
        "machine_id" : "1",
        "machine_metric_name" : "Кол-во аварий",
        "machine_metric_type" : "accident_count",
        "machine_units_of_measurment" : "_",
        "machine_metric_value" : "0",
        "time_start" : str(datetime.now()),
        "time_end" : str(datetime.now()),
    },

    "machine_metrics110" : {
        "table_name" : "machine_metrics",
        "machine_id" : "1",
        "machine_metric_name" : "Время работы инструмента",
        "machine_metric_type" : "tool_operating_time ",
        "machine_units_of_measurment" : "мин",
        "machine_metric_value" : "0",
        "time_start" : str(datetime.now()),
        "time_end" : str(datetime.now()),
    },

    "worker_to_machine_1" : {
        "table_name" : "worker_to_machine",
        "machine_id" : "1",
        "shop_id" : "1",
        "worker_id" : "1",
    },

    "machine_types_2" : {
        "table_name" : "machine_types",
        "type_name": "Фрезерный"
    },

    'sensors_by_types_21 - 3' : {
        "table_name" : "sensors_by_types",
        "machine_type_id" : "2",
        "units_of_measurment" : "вт/ч",
        "port" : "1232",
        "sensor_type_name" : "consmp"
    },

    'sensors_by_types_22 - 4' : {
        "table_name" : "sensors_by_types",
        "machine_type_id" : "2",
        "units_of_measurment" : "об/мин",
        "port" : "133",
        "sensor_type_name" : "spo"
    },

    "machines_2" :{
        "table_name" : "machines",
        "machine_name" : "Freser",
        "machine_type_id" : "2",
        "machine_state" : "working...",
        "tablet_id" : "aScasjcnzxc",
    },

    "sensors_21" : {
        "table_name" : "sensors",
        "machine_id" : "2",
        "sensor_name" : "consmp",
        "sensor_port" : "1232",
        "sensor_value" : "123123123",
        "sensor_type_id" : "4",
    },

    "sensors_22" : {
        "table_name" : "sensors",
        "machine_id" : "2",
        "sensor_name" : "lmpwork",
        "sensor_port" : "133",
        "sensor_value" : "3333",
        "sensor_type_id" : "4",
    },

    'machine_workplace_2' : {
        "table_name" : "machine_workplace",
        "machine_workplace_name" : "SoName",
        "machine_id" : "2",
    },

    "machine_metrics21" : {
        "table_name" : "machine_metrics",
        "machine_id" : "2",
        "machine_metric_name" : "Энергопотребление",
        "machine_metric_type" : "energy_consumption",
        "machine_units_of_measurment" : "квт/ч",
        "machine_metric_value" : "0",
        "time_start" : str(datetime.now()),
        "time_end" : str(datetime.now()),
    },

    "machine_metrics22" : {
        "table_name" : "machine_metrics",
        "machine_id" : "2",
        "machine_metric_name" : "OEE",
        "machine_metric_type" : "oee",
        "machine_units_of_measurment" : "%",
        "machine_metric_value" : "0",
        "time_start" : str(datetime.now()),
        "time_end" : str(datetime.now()),
    },


    "machine_metrics23" : {
        "table_name" : "machine_metrics",
        "machine_id" : "2",
        "machine_metric_name" : "КПЭ",
        "machine_metric_type" : "kpe",
        "machine_units_of_measurment" : "%",
        "machine_metric_value" : "0",
        "time_start" : str(datetime.now()),
        "time_end" : str(datetime.now()),
    },

    "machine_metrics24" : {
        "table_name" : "machine_metrics",
        "machine_id" : "2",
        "machine_metric_name" : "Время работы",
        "machine_metric_type" : "work_time",
        "machine_units_of_measurment" : "мин",
        "machine_metric_value" : "0",
        "time_start" : str(datetime.now()),
        "time_end" : str(datetime.now()),
    },

    "machine_metrics25" : {
        "table_name" : "machine_metrics",
        "machine_id" : "2",
        "machine_metric_name" : "Машинное время",
        "machine_metric_type" : "machine_time",
        "machine_units_of_measurment" : "мин",
        "machine_metric_value" : "0",
        "time_start" : str(datetime.now()),
        "time_end" : str(datetime.now()),
    },

    "machine_metrics26" : {
        "table_name" : "machine_metrics",
        "machine_id" : "2",
        "machine_metric_name" : "Причины простоя",
        "machine_metric_type" : "stay_",
        "machine_units_of_measurment" : "%",
        "machine_metric_value" : "0",
        "time_start" : str(datetime.now()),
        "time_end" : str(datetime.now()),
    },

    "machine_metrics27" : {
        "table_name" : "machine_metrics",
        "machine_id" : "2",
        "machine_metric_name" : "Среднее время обработки",
        "machine_metric_type" : "avg_processsing_time",
        "machine_units_of_measurment" : "мин",
        "machine_metric_value" : "0",
        "time_start" : str(datetime.now()),
        "time_end" : str(datetime.now()),
    },

    "machine_metrics28" : {
        "table_name" : "machine_metrics",
        "machine_id" : "2",
        "machine_metric_name" : "Среднее время между обработкой",
        "machine_metric_type" : "vg_time_between_processing",
        "machine_units_of_measurment" : "мин",
        "machine_metric_value" : "0",
        "time_start" : str(datetime.now()),
        "time_end" : str(datetime.now()),
    },


    "machine_metrics29" : {
        "table_name" : "machine_metrics",
        "machine_id" : "2",
        "machine_metric_name" : "Кол-во аварий",
        "machine_metric_type" : "accident_count",
        "machine_units_of_measurment" : "_",
        "machine_metric_value" : "0",
        "time_start" : str(datetime.now()),
        "time_end" : str(datetime.now()),
    },

    "machine_metrics210" : {
        "table_name" : "machine_metrics",
        "machine_id" : "2",
        "machine_metric_name" : "Время работы инструмента",
        "machine_metric_type" : "tool_operating_time ",
        "machine_units_of_measurment" : "мин",
        "machine_metric_value" : "0",
        "time_start" : str(datetime.now()),
        "time_end" : str(datetime.now()),
    },



    "worker_to_machine_2" : {
        "table_name" : "worker_to_machine",
        "machine_id" : "2",
        "shop_id" : "1",
        "worker_id" : "1",
    },

}


# Function that addess workers then machines
def fill_tables(dotenv_path):

    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    try:
        # setting db connection data
        with psycopg2.connect(host=os.getenv("db_host"),
                              user=os.getenv("db_user"), 
                              password=os.getenv("db_password"), 
                              dbname=os.getenv("db_name")) as conn:
            # connecting to db
            with conn.cursor() as cursor:


                for table_tag in data:
                    print(f"table_tag : {table_tag}")

                    table_name = data[table_tag]["table_name"]
                    columns = [column_name  for column_name in data[table_tag] if column_name != "table_name"] 
                    column_values = [ "'" + data[table_tag][column_name] + "'" for column_name in data[table_tag] if column_name != "table_name"]

                    query = f"insert into {table_name} ({",".join(columns)}) values ({",".join(column_values)})"

                    print(query)
                    cursor.execute(query)
            
            
            
            print("db was filled)")

    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
