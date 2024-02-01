import psycopg2
import os
from dotenv import load_dotenv
import random




def create_tables(dotenv_path):
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    
    try:
        with psycopg2.connect(host=os.getenv("db_host"),
                              user=os.getenv("db_user"), 
                              password=os.getenv("db_password"), 
                              dbname=os.getenv("db_name")) as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    create table if not exists production(
                        id serial primary key ,
                        production_name varchar(255) not null
                    );


                    create table if not exists user_admin(
                        id serial primary key ,
                        full_name varchar(255) not null,
                        user_role varchar(255) not null,
                        user_login varchar(255) not null unique,
                        user_password varchar(255) not null,
                        production_id serial references production on delete cascade
                    );

                    create table if not exists target_values(
                        id serial primary key ,
                        metric_type varchar(255) not null,
                        target_value varchar(255) not null,
                        production_id serial references production on delete cascade
                    );

                    create table if not exists production_total(
                        id serial primary key ,
                        production_id serial references production on delete cascade,
                        production_total_type varchar(255) not null,
                        production_total_value varchar(255) not null,
                        time_start timestamp not null,
                        time_end timestamp not null
                    );

                    create table if not exists report_models(
                        id serial primary key ,
                        report_model_name varchar(255) not null,
                        production_id serial references production on delete cascade
                    );

                    create table if not exists report_blocks(
                        id serial primary key ,
                        report_block_type varchar(255) not null,
                        report_block_name varchar(255) not null,
                        report_model_id serial references report_models on delete cascade,
                        report_block_source varchar(255) not null,
                        metric_type varchar(255) not null
                    );

                    create table if not exists generated_reports(
                        id serial primary key ,
                        report_name varchar(255) not null,
                        from_date timestamp not null,
                        to_date timestamp not null,
                        generated_report_model_id serial references report_models on delete cascade
                    );


                    create table if not exists shop(
                        id serial primary key ,
                        production_id serial references production on delete cascade,
                        shop_name varchar(255) not null  
                    );


                    create table if not exists shop_total(
                        id serial primary key ,
                        shop_id serial references shop on delete cascade,
                        shop_total_type varchar(255) not null,  
                        production_id serial references production on delete cascade,
                        shop_name varchar(255) not null 
                    );

                    create table if not exists worker(
                        id serial primary key,
                        full_name varchar(255) not null,
                        phone_number varchar(255) not null, 
                        position varchar(255) not null,
                        worker_login varchar(255) not null,
                        worker_password varchar(255) not null
                    );

                    create table if not exists worker_actions(
                        id serial primary key,
                        worker_id serial references worker,
                        action_class varchar(255) not null,
                        action_status varchar(255) not null,
                        action_time timestamp not null
                    );

                    create table if not exists worker_metrics(
                        id serial primary key,
                        worker_id serial references worker,
                        worker_metric_name varchar(255) not null,
                        worker_units_of_measurment varchar(255) not null,
                        worker_metric_value varchar(255) not null,
                        time_start timestamp not null,
                        time_end timestamp not null
                    );

                    create table if not exists machine_types (
                        id serial primary key,
                        type_name varchar(255) not null
                    );

                    create table if not exists sensors_by_types (
                        id serial primary key,
                        machine_type_id serial references machine_types,
                        units_of_measurment varchar(255) not null,
                        position integer not null
                    );

                    create table if not exists machines(
                        id serial primary key,
                        machine_name varchar(255) not null,
                        machine_type_id serial references machine_types,
                        machine_state varchar(255) not null,
                        tablet_id varchar(255) not null
                    );

                    create table if not exists sensors(
                        id serial primary key,
                        machine_id serial references machines,
                        sensor_name varchar(255) not null,
                        position integer not null,
                        sensor_value varchar(255) not null,
                        sensor_type_name varchar(255) not null
                    );

                    create table if not exists worker_to_machine(
                        id serial primary key,
                        shop_id serial references shop,
                        worker_id serial references worker,
                        machine_id serial references machines 
                    );

                    create table if not exists machine_actions(
                        id serial primary key,
                        machine_id serial references worker,
                        action_class varchar(255) not null,
                        action_status varchar(255) not null,
                        action_time timestamp not null
                    );

                    create table if not exists machine_metrics(
                        id serial primary key,
                        machine_id serial references worker,
                        machine_metric_name varchar(255) not null,
                        machine_metric_type varchar(255) not null,
                        machine_units_of_measurment varchar(255) not null,
                        machine_metric_value varchar(255) not null,
                        time_start timestamp not null,
                        time_end timestamp not null
                    );

                    create table if not exists alerts(
                        id serial primary key,
                        alert_message varchar(255) not null,
                        production_id serial references production,
                        machine_id serial references machines,
                        machine_action_id serial references machine_actions,
                        is_closed boolean not null,
                        is_read boolean not null

                    );
                """)
            print("db created")
            
                
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
