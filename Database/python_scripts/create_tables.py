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
SELECT 1+1 AS result;


SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_name = 'production';


CREATE TABLE IF NOT EXISTS "production" ("id"  SERIAL , "production_name" VARCHAR(255), PRIMARY KEY ("id"));;


SELECT i.relname AS name, ix.indisprimary AS primary, ix.indisunique AS unique, ix.indkey AS indkey, array_agg(a.attnum) as column_indexes, array_agg(a.attname) AS column_names, pg_get_indexdef(ix.indexrelid) AS definition FROM pg_class t, pg_class i, pg_index ix, pg_attribute a WHERE t.oid = ix.indrelid AND i.oid = ix.indexrelid AND a.attrelid = t.oid AND t.relkind = 'r' and t.relname = 'production' GROUP BY i.relname, ix.indexrelid, ix.indisprimary, ix.indisunique, ix.indkey ORDER BY i.relname;;


SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_name = 'user_admin';


CREATE TABLE IF NOT EXISTS "user_admin" ("id"  SERIAL , "full_name" VARCHAR(255), "user_role" VARCHAR(255), "user_login" VARCHAR(255), "user_password" VARCHAR(255), "production_id" INTEGER REFERENCES "production" ("id"), PRIMARY KEY ("id"));;


SELECT i.relname AS name, ix.indisprimary AS primary, ix.indisunique AS unique, ix.indkey AS indkey, array_agg(a.attnum) as column_indexes, array_agg(a.attname) AS column_names, pg_get_indexdef(ix.indexrelid) AS definition FROM pg_class t, pg_class i, pg_index ix, pg_attribute a WHERE t.oid = ix.indrelid AND i.oid = ix.indexrelid AND a.attrelid = t.oid AND t.relkind = 'r' and t.relname = 'user_admin' GROUP BY i.relname, ix.indexrelid, ix.indisprimary, ix.indisunique, ix.indkey ORDER BY i.relname;;





SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_name = 'production_total';CREATE TABLE IF NOT EXISTS "production_total" ("id"  SERIAL , "production_total_type" VARCHAR(255), "production_total_value" VARCHAR(255), "time_start" TIMESTAMP WITH TIME ZONE, "time_end" TIMESTAMP WITH TIME ZONE, "production_id" INTEGER REFERENCES "production" ("id"), PRIMARY KEY ("id"));;


SELECT i.relname AS name, ix.indisprimary AS primary, ix.indisunique AS unique, ix.indkey AS indkey, array_agg(a.attnum) as column_indexes, array_agg(a.attname) AS column_names, pg_get_indexdef(ix.indexrelid) AS definition FROM pg_class t, pg_class i, pg_index ix, pg_attribute a WHERE t.oid = ix.indrelid AND i.oid = ix.indexrelid AND a.attrelid = t.oid AND t.relkind = 'r' and t.relname = 'production_total' GROUP BY i.relname, ix.indexrelid, ix.indisprimary, ix.indisunique, ix.indkey ORDER BY i.relname;;


SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_name = 'report_models';


CREATE TABLE IF NOT EXISTS "report_models" ("id"  SERIAL , "report_model_name" VARCHAR(255), "production_id" INTEGER REFERENCES "production" ("id"), PRIMARY KEY ("id"));;


SELECT i.relname AS name, ix.indisprimary AS primary, ix.indisunique AS unique, ix.indkey AS indkey, array_agg(a.attnum) as column_indexes, array_agg(a.attname) AS column_names, pg_get_indexdef(ix.indexrelid) AS definition FROM pg_class t, pg_class i, pg_index ix, pg_attribute a WHERE t.oid = ix.indrelid AND i.oid = ix.indexrelid AND a.attrelid = t.oid AND t.relkind = 'r' and t.relname = 'report_models' GROUP BY i.relname, ix.indexrelid, ix.indisprimary, ix.indisunique, ix.indkey ORDER BY i.relname;;


SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_name = 'report_blocks';


CREATE TABLE IF NOT EXISTS "report_blocks" ("id"  SERIAL , "report_block_type" VARCHAR(255), "report_block_name" VARCHAR(255), "report_block_source" VARCHAR(255), "metric_type" VARCHAR(255), "report_model_id" INTEGER REFERENCES "report_models" ("id"), PRIMARY KEY ("id"));;


SELECT i.relname AS name, ix.indisprimary AS primary, ix.indisunique AS unique, ix.indkey AS indkey, array_agg(a.attnum) as column_indexes, array_agg(a.attname) AS column_names, pg_get_indexdef(ix.indexrelid) AS definition FROM pg_class t, pg_class i, pg_index ix, pg_attribute a WHERE t.oid = ix.indrelid AND i.oid = ix.indexrelid AND a.attrelid = t.oid AND t.relkind = 'r' and t.relname = 'report_blocks' GROUP BY i.relname, ix.indexrelid, ix.indisprimary, ix.indisunique, ix.indkey ORDER BY i.relname;;


SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_name = 'generated_reports';


CREATE TABLE IF NOT EXISTS "generated_reports" ("id"  SERIAL , "report_name" VARCHAR(255), "from_date" TIMESTAMP WITH TIME ZONE, "to_date" TIMESTAMP WITH TIME ZONE, "generated_report_model_id" INTEGER REFERENCES "report_models" ("id"), PRIMARY KEY ("id"));;


SELECT i.relname AS name, ix.indisprimary AS primary, ix.indisunique AS unique, ix.indkey AS indkey, array_agg(a.attnum) as column_indexes, array_agg(a.attname) AS column_names, pg_get_indexdef(ix.indexrelid) AS definition FROM pg_class t, pg_class i, pg_index ix, pg_attribute a WHERE t.oid = ix.indrelid AND i.oid = ix.indexrelid AND a.attrelid = t.oid AND t.relkind = 'r' and t.relname = 'generated_reports' GROUP BY i.relname, ix.indexrelid, ix.indisprimary, ix.indisunique, ix.indkey ORDER BY i.relname;;


SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_name = 'shop';





CREATE TABLE IF NOT EXISTS "shop" ("id"  SERIAL , "shop_name" VARCHAR(255), "production_id" INTEGER REFERENCES "production" ("id"), PRIMARY KEY ("id"));;SELECT i.relname AS name, ix.indisprimary AS primary, ix.indisunique AS unique, ix.indkey AS indkey, array_agg(a.attnum) as column_indexes, array_agg(a.attname) AS column_names, pg_get_indexdef(ix.indexrelid) AS definition FROM pg_class t, pg_class i, pg_index ix, pg_attribute a WHERE t.oid = ix.indrelid AND i.oid = ix.indexrelid AND a.attrelid = t.oid AND t.relkind = 'r' and t.relname = 'shop' GROUP BY i.relname, ix.indexrelid, ix.indisprimary, ix.indisunique, ix.indkey ORDER BY i.relname;;


SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_name = 'shop_total';


CREATE TABLE IF NOT EXISTS "shop_total" ("id"  SERIAL , "shop_total_type" VARCHAR(255), "shop_name" VARCHAR(255), "shop_id" INTEGER REFERENCES "shop" ("id"), "production_id" INTEGER REFERENCES "production" ("id"), PRIMARY KEY ("id"));;


SELECT i.relname AS name, ix.indisprimary AS primary, ix.indisunique AS unique, ix.indkey AS indkey, array_agg(a.attnum) as column_indexes, array_agg(a.attname) AS column_names, pg_get_indexdef(ix.indexrelid) AS definition FROM pg_class t, pg_class i, pg_index ix, pg_attribute a WHERE t.oid = ix.indrelid AND i.oid = ix.indexrelid AND a.attrelid = t.oid AND t.relkind = 'r' and t.relname = 'shop_total' GROUP BY i.relname, ix.indexrelid, ix.indisprimary, ix.indisunique, ix.indkey ORDER BY i.relname;;


SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_name = 'worker';


CREATE TABLE IF NOT EXISTS "worker" ("id"  SERIAL , "full_name" VARCHAR(255), "phone_number" VARCHAR(255), "position" VARCHAR(255), "worker_login" VARCHAR(255), "worker_password" VARCHAR(255), PRIMARY KEY ("id"));;


SELECT i.relname AS name, ix.indisprimary AS primary, ix.indisunique AS unique, ix.indkey AS indkey, array_agg(a.attnum) as column_indexes, array_agg(a.attname) AS column_names, pg_get_indexdef(ix.indexrelid) AS definition FROM pg_class t, pg_class i, pg_index ix, pg_attribute a WHERE t.oid = ix.indrelid AND i.oid = ix.indexrelid AND a.attrelid = t.oid AND t.relkind = 'r' and t.relname = 'worker' GROUP BY i.relname, ix.indexrelid, ix.indisprimary, ix.indisunique, ix.indkey ORDER BY i.relname;;


SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_name = 'worker_actions';


CREATE TABLE IF NOT EXISTS "worker_actions" ("id"  SERIAL , "action_class" VARCHAR(255), "action_status" VARCHAR(255), "action_time" TIMESTAMP WITH TIME ZONE, "worker_id" INTEGER REFERENCES "worker" ("id"), PRIMARY KEY ("id"));;


SELECT i.relname AS name, ix.indisprimary AS primary, ix.indisunique AS unique, ix.indkey AS indkey, array_agg(a.attnum) as column_indexes, array_agg(a.attname) AS column_names, pg_get_indexdef(ix.indexrelid) AS definition FROM pg_class t, pg_class i, pg_index ix, pg_attribute a WHERE t.oid = ix.indrelid AND i.oid = ix.indexrelid AND a.attrelid = t.oid AND t.relkind = 'r' and t.relname = 'worker_actions' GROUP BY i.relname, ix.indexrelid, ix.indisprimary, ix.indisunique, ix.indkey ORDER BY i.relname;;


SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_name = 'worker_metrics';


CREATE TABLE IF NOT EXISTS "worker_metrics" ("id"  SERIAL , "worker_metric_name" VARCHAR(255), "worker_units_of_measurment" VARCHAR(255), "worker_metric_value" VARCHAR(255), "time_start" TIMESTAMP WITH TIME ZONE, "time_end" TIMESTAMP WITH TIME ZONE, "worker_id" INTEGER REFERENCES "worker" ("id"), PRIMARY KEY ("id"));;


SELECT i.relname AS name, ix.indisprimary AS primary, ix.indisunique AS unique, ix.indkey AS indkey, array_agg(a.attnum) as column_indexes, array_agg(a.attname) AS column_names, pg_get_indexdef(ix.indexrelid) AS definition FROM pg_class t, pg_class i, pg_index ix, pg_attribute a WHERE t.oid = ix.indrelid AND i.oid = ix.indexrelid AND a.attrelid = t.oid AND t.relkind = 'r' and t.relname = 'worker_metrics' GROUP BY i.relname, ix.indexrelid, ix.indisprimary, ix.indisunique, ix.indkey ORDER BY i.relname;;


SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_name = 'machine_types';


CREATE TABLE IF NOT EXISTS "machine_types" ("id"  SERIAL , "type_name" VARCHAR(255), PRIMARY KEY ("id"));;


SELECT i.relname AS name, ix.indisprimary AS primary, ix.indisunique AS unique, ix.indkey AS indkey, array_agg(a.attnum) as column_indexes, array_agg(a.attname) AS column_names, pg_get_indexdef(ix.indexrelid) AS definition FROM pg_class t, pg_class i, pg_index ix, pg_attribute a WHERE t.oid = ix.indrelid AND i.oid = ix.indexrelid AND a.attrelid = t.oid AND t.relkind = 'r' and t.relname = 'machine_types' GROUP BY i.relname, ix.indexrelid, ix.indisprimary, ix.indisunique, ix.indkey ORDER BY i.relname;;


SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_name = 'sensors_by_types';


CREATE TABLE IF NOT EXISTS "sensors_by_types" ("id"  SERIAL , "units_of_measurment" VARCHAR(255), "port" VARCHAR(255), "sensor_type_name" VARCHAR(255), "machine_type_id" INTEGER REFERENCES "machine_types" ("id"), PRIMARY KEY ("id"));;


SELECT i.relname AS name, ix.indisprimary AS primary, ix.indisunique AS unique, ix.indkey AS indkey, array_agg(a.attnum) as column_indexes, array_agg(a.attname) AS column_names, pg_get_indexdef(ix.indexrelid) AS definition FROM pg_class t, pg_class i, pg_index ix, pg_attribute a WHERE t.oid = ix.indrelid AND i.oid = ix.indexrelid AND a.attrelid = t.oid AND t.relkind = 'r' and t.relname = 'sensors_by_types' GROUP BY i.relname, ix.indexrelid, ix.indisprimary, ix.indisunique, ix.indkey ORDER BY i.relname;;


SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_name = 'machines';


CREATE TABLE IF NOT EXISTS "machines" ("id"  SERIAL , "machine_name" VARCHAR(255), "machine_state" VARCHAR(255), "tablet_id" VARCHAR(255), "machine_token" VARCHAR(255), "machine_type_id" INTEGER REFERENCES "machine_types" ("id"), PRIMARY KEY ("id"));;





SELECT i.relname AS name, ix.indisprimary AS primary, ix.indisunique AS unique, ix.indkey AS indkey, array_agg(a.attnum) as column_indexes, array_agg(a.attname) AS column_names, pg_get_indexdef(ix.indexrelid) AS definition FROM pg_class t, pg_class i, pg_index ix, pg_attribute a WHERE t.oid = ix.indrelid AND i.oid = ix.indexrelid AND a.attrelid = t.oid AND t.relkind = 'r' and t.relname = 'machines' GROUP BY i.relname, ix.indexrelid, ix.indisprimary, ix.indisunique, ix.indkey ORDER BY i.relname;;SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_name = 'sensors';


CREATE TABLE IF NOT EXISTS "sensors" ("id"  SERIAL , "sensor_name" VARCHAR(255), "sensor_port" VARCHAR(255), "sensor_value" VARCHAR(255), "machine_id" INTEGER REFERENCES "machines" ("id"), "sensor_type_id" INTEGER REFERENCES "sensors_by_types" ("id"), PRIMARY KEY ("id"));;


SELECT i.relname AS name, ix.indisprimary AS primary, ix.indisunique AS unique, ix.indkey AS indkey, array_agg(a.attnum) as column_indexes, array_agg(a.attname) AS column_names, pg_get_indexdef(ix.indexrelid) AS definition FROM pg_class t, pg_class i, pg_index ix, pg_attribute a WHERE t.oid = ix.indrelid AND i.oid = ix.indexrelid AND a.attrelid = t.oid AND t.relkind = 'r' and t.relname = 'sensors' GROUP BY i.relname, ix.indexrelid, ix.indisprimary, ix.indisunique, ix.indkey ORDER BY i.relname;;


SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_name = 'machine_workplace';


CREATE TABLE IF NOT EXISTS "machine_workplace" ("id"  SERIAL , "machine_workplace_name" VARCHAR(255), "machine_id" INTEGER REFERENCES "machines" ("id"), PRIMARY KEY ("id"));;


SELECT i.relname AS name, ix.indisprimary AS primary, ix.indisunique AS unique, ix.indkey AS indkey, array_agg(a.attnum) as column_indexes, array_agg(a.attname) AS column_names, pg_get_indexdef(ix.indexrelid) AS definition FROM pg_class t, pg_class i, pg_index ix, pg_attribute a WHERE t.oid = ix.indrelid AND i.oid = ix.indexrelid AND a.attrelid = t.oid AND t.relkind = 'r' and t.relname = 'machine_workplace' GROUP BY i.relname, ix.indexrelid, ix.indisprimary, ix.indisunique, ix.indkey ORDER BY i.relname;;


SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_name = 'worker_to_machine';


CREATE TABLE IF NOT EXISTS "worker_to_machine" ("id"  SERIAL , "shop_id" INTEGER REFERENCES "shop" ("id"), "worker_id" INTEGER REFERENCES "worker" ("id"), "machine_id" INTEGER REFERENCES "machines" ("id"), PRIMARY KEY ("id"));;


SELECT i.relname AS name, ix.indisprimary AS primary, ix.indisunique AS unique, ix.indkey AS indkey, array_agg(a.attnum) as column_indexes, array_agg(a.attname) AS column_names, pg_get_indexdef(ix.indexrelid) AS definition FROM pg_class t, pg_class i, pg_index ix, pg_attribute a WHERE t.oid = ix.indrelid AND i.oid = ix.indexrelid AND a.attrelid = t.oid AND t.relkind = 'r' and t.relname = 'worker_to_machine' GROUP BY i.relname, ix.indexrelid, ix.indisprimary, ix.indisunique, ix.indkey ORDER BY i.relname;;


SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_name = 'machine_actions';


CREATE TABLE IF NOT EXISTS "machine_actions" ("id"  SERIAL , "action_type" VARCHAR(255), "action_name" VARCHAR(255), "action_time" TIMESTAMP WITH TIME ZONE, "machine_id" INTEGER REFERENCES "machines" ("id"), PRIMARY KEY ("id"));;


SELECT i.relname AS name, ix.indisprimary AS primary, ix.indisunique AS unique, ix.indkey AS indkey, array_agg(a.attnum) as column_indexes, array_agg(a.attname) AS column_names, pg_get_indexdef(ix.indexrelid) AS definition FROM pg_class t, pg_class i, pg_index ix, pg_attribute a WHERE t.oid = ix.indrelid AND i.oid = ix.indexrelid AND a.attrelid = t.oid AND t.relkind = 'r' and t.relname = 'machine_actions' GROUP BY i.relname, ix.indexrelid, ix.indisprimary, ix.indisunique, ix.indkey ORDER BY i.relname;;


SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_name = 'machine_metrics';


CREATE TABLE IF NOT EXISTS "machine_metrics" ("id"  SERIAL , "machine_metric_name" VARCHAR(255), "machine_metric_type" VARCHAR(255), "machine_units_of_measurment" VARCHAR(255), "machine_metric_value" VARCHAR(255), "time_start" TIMESTAMP WITH TIME ZONE, "time_end" TIMESTAMP WITH TIME ZONE, "machine_id" INTEGER REFERENCES "machines" ("id"), PRIMARY KEY ("id"));;


SELECT i.relname AS name, ix.indisprimary AS primary, ix.indisunique AS unique, ix.indkey AS indkey, array_agg(a.attnum) as column_indexes, array_agg(a.attname) AS column_names, pg_get_indexdef(ix.indexrelid) AS definition FROM pg_class t, pg_class i, pg_index ix, pg_attribute a WHERE t.oid = ix.indrelid AND i.oid = ix.indexrelid AND a.attrelid = t.oid AND t.relkind = 'r' and t.relname = 'machine_metrics' GROUP BY i.relname, ix.indexrelid, ix.indisprimary, ix.indisunique, ix.indkey ORDER BY i.relname;;


SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_name = 'target_values';


CREATE TABLE IF NOT EXISTS "target_values" ("id"  SERIAL , "type_name" VARCHAR(255), "target_value" VARCHAR(255), PRIMARY KEY ("id"));;


SELECT i.relname AS name, ix.indisprimary AS primary, ix.indisunique AS unique, ix.indkey AS indkey, array_agg(a.attnum) as column_indexes, array_agg(a.attname) AS column_names, pg_get_indexdef(ix.indexrelid) AS definition FROM pg_class t, pg_class i, pg_index ix, pg_attribute a WHERE t.oid = ix.indrelid AND i.oid = ix.indexrelid AND a.attrelid = t.oid AND t.relkind = 'r' and t.relname = 'target_values' GROUP BY i.relname, ix.indexrelid, ix.indisprimary, ix.indisunique, ix.indkey ORDER BY i.relname;;


SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_name = 'alerts';


CREATE TABLE IF NOT EXISTS "alerts" ("id"  SERIAL , "alert_message" VARCHAR(255), "is_closed" VARCHAR(255), "is_read" VARCHAR(255), "production_id" INTEGER REFERENCES "production" ("id"), "machine_id" INTEGER REFERENCES "machines" ("id"), "machine_action_id" INTEGER REFERENCES "machine_actions" ("id"), PRIMARY KEY ("id"));;


SELECT i.relname AS name, ix.indisprimary AS primary, ix.indisunique AS unique, ix.indkey AS indkey, array_agg(a.attnum) as column_indexes, array_agg(a.attname) AS column_names, pg_get_indexdef(ix.indexrelid) AS definition FROM pg_class t, pg_class i, pg_index ix, pg_attribute a WHERE t.oid = ix.indrelid AND i.oid = ix.indexrelid AND a.attrelid = t.oid AND t.relkind = 'r' and t.relname = 'alerts' GROUP BY i.relname, ix.indexrelid, ix.indisprimary, ix.indisunique, ix.indkey ORDER BY i.relname;;


SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_name = 'admin_sessions';


SELECT i.relname AS name, ix.indisprimary AS primary, ix.indisunique AS unique, ix.indkey AS indkey, array_agg(a.attnum) as column_indexes, array_agg(a.attname) AS column_names, pg_get_indexdef(ix.indexrelid) AS definition FROM pg_class t, pg_class i, pg_index ix, pg_attribute a WHERE t.oid = ix.indrelid AND i.oid = ix.indexrelid AND a.attrelid = t.oid AND t.relkind = 'r' and t.relname = 'admin_sessions' GROUP BY i.relname, ix.indexrelid, ix.indisprimary, ix.indisunique, ix.indkey ORDER BY i.relname;;


SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' AND table_name = 'worker_sessions';


SELECT i.relname AS name, ix.indisprimary AS primary, ix.indisunique AS unique, ix.indkey AS indkey, array_agg(a.attnum) as column_indexes, array_agg(a.attname) AS column_names, pg_get_indexdef(ix.indexrelid) AS definition FROM pg_class t, pg_class i, pg_index ix, pg_attribute a WHERE t.oid = ix.indrelid AND i.oid = ix.indexrelid AND a.attrelid = t.oid AND t.relkind = 'r' and t.relname = 'worker_sessions' GROUP BY i.relname, ix.indexrelid, ix.indisprimary, ix.indisunique, ix.indkey ORDER BY i.relname;;



""")
            print("db created)")
            
                
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
