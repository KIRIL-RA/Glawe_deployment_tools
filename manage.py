import sys

arguments = sys.argv

if (len(arguments) > 2):
    print("too many arguments")
    print("try : manage.py help")
    sys.exit(0)


dotenv_path = '.env'

if (len(arguments) < 2):
    print("not enough arguments")
    print("try : manage.py help")
    sys.exit(0)


if (arguments[1] == "help"):
    print(" commands : ")
    print("           createdb")
    print("           cleardb")
    print("           filldb")
elif (arguments[1] == "createdb"):
    from Database.python_scripts.create_tables import create_tables
    create_tables(dotenv_path)
elif (arguments[1] == "cleardb"):
    from Database.python_scripts.delete_all_tables import delete_all_tables
    delete_all_tables(dotenv_path)
elif (arguments[1] == "filldb"):
    from Database.python_scripts.fill_db_with_users import fill_db_with_data
    from Database.python_scripts.fill_db_with_machines import fill_db_with_machines
    fill_db_with_data(dotenv_path)
    fill_db_with_machines(dotenv_path)
else:
    print("argument doesn't exist")
    print("try : manage.py help")