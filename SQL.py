import psycopg
from functions import json_to_list, get_list_of_ids

connstring = "postgresql://postgres:1234@localhost:5432/cli_tracker"
with psycopg.connect(connstring) as conn:
    cur = conn.cursor()
    create_table = ("""CREATE TABLE IF NOT EXISTS tarefas (
            id INT PRIMARY KEY NOT NULL,
            descricao VARCHAR(80) NOT NULL,
            status VARCHAR(11) DEFAULT 'todo' NOT NULL,
            criadoEm TIMESTAMPTZ(0) DEFAULT CURRENT_TIMESTAMP NOT NULL,
            atualizadoEm TIMESTAMPTZ(0) DEFAULT CURRENT_TIMESTAMP NOT NULL
    )""")
    def sql_add_task(json_id, descricao):
        create_task_query = """INSERT INTO tarefas (id, descricao)
        VALUES (%s, '%s')
        """ % (json_id, descricao)
        cur.execute(create_task_query)

    def sql_update_task(json_id, descricao):
        update_task_query = """UPDATE tarefas
        SET descricao = '%s'
        WHERE id = %s
        """ % (descricao, id)
        cur.execute(update_task_query)
    def sql_delete_task(json_id):
        delete_task_query = """DELETE FROM tarefas
        WHERE id = %s
        """ % (id)
        cur.execute(delete_task_query)


    cur.execute(create_table)
    try:
        ## Updates SQL to the JSON File
        ## Get IDs that are into the JSON file, get ids that are in the SQL database
        ## If the id is in JSON File, but not SQL database, add the task to the sql database
        lista_ids_json = get_list_of_ids()
        query = """SELECT id FROM tarefas"""
        ids_in_sql_not_in_json = [id_in_json for id_in_json in lista_ids_json if id_in_json not in [item[0] for item in cur.execute(query).fetchall()]]
        # ^^ create list of ids that are in json but not sql
        print(ids_in_sql_not_in_json)
        for id in ids_in_sql_not_in_json:
            task = json_to_list()[id] # get task by id
            sql_add_task(id, task.get("desc"))
    except IndexError:
        pass
    except TypeError:
        pass
    conn.commit()
