import psycopg2
import os
from dotenv import load_dotenv
import random




def delete_all_tables(dotenv_path):

    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    try:
        with psycopg2.connect(host=os.getenv("db_host"),
                              user=os.getenv("db_user"), 
                              password=os.getenv("db_password"), 
                              dbname=os.getenv("db_name")) as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    drop table if exists machines,
                                shop_total,
                                worker,
                                worker_actions,
                                worker_metrics,
                                machine_types,
                                sensors_by_types,
                                worker_to_machine,
                                sensors,
                                machine_actions,
                                production,
                                user_admin,
                                target_values,
                                production_total,
                                report_models,
                                report_blocks,
                                generated_reports,
                                shop,
                                machine_metrics,
                                alerts,
                               machine_workplace;
                """)
                print("db cleared)")

    except (psycopg2.DatabaseError, Exception) as error:
        print(error)