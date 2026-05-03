import sql_connection

from functions import json_to_list, get_list_of_ids, create_json_file
from sql_connection import SQL_connected
if SQL_connected:
    from sql_connection import conn

if SQL_connected:
    create_table = ("""CREATE TABLE IF NOT EXISTS tarefas_db (
            id INT PRIMARY KEY NOT NULL,
            descricao VARCHAR(80) NOT NULL,
            status VARCHAR(11) DEFAULT 'todo' NOT NULL,
            criadoEm TIMESTAMP(0) DEFAULT CURRENT_TIMESTAMP NOT NULL,
            atualizadoEm TIMESTAMP(0) DEFAULT CURRENT_TIMESTAMP NOT NULL
)""")
    cur = sql_connection.conn.cursor()
    cur.execute(create_table)

def sql_add_task(json_id, descricao):
    if not SQL_connected:
        return None

    try:
        create_task_query = """INSERT INTO tarefas_db (id, descricao)
        VALUES (%s, %s)
        """
        cur.execute(create_task_query, (json_id, descricao))
        conn.commit()
    except Exception as e:
        print(f"não foi possível adicionar tarefa ao SQL. Erro: {e}")



def sql_add_existing_task(json_id, descricao, status, criadoEm, atualizadoEm):
    if not SQL_connected:
        return None
    create_task_query = """INSERT INTO tarefas_db (id, descricao, status, criadoEm, atualizadoEm)
    VALUES (%s, %s, %s, %s, %s)
    """
    cur.execute(create_task_query, (json_id, descricao, status, criadoEm, atualizadoEm))

def sql_update_task(json_id, descricao):
    if not SQL_connected:
        return None
    update_task_query = """UPDATE tarefas_db
    SET descricao = %s
    WHERE id = %s
    """
    cur.execute(update_task_query, (descricao, json_id))
    conn.commit()

def sql_mark_in_progress(json_id):
    if not SQL_connected:
        return None
    in_progress_query = """UPDATE tarefas_db
    SET status = 'in_progress'
    WHERE id = %s"""
    cur.execute(in_progress_query, (json_id,))
    conn.commit()

def sql_mark_done(json_id):
    if not SQL_connected:
        return None
    mark_done_query = """UPDATE tarefas_db
    SET status = 'done'
    WHERE id = %s"""
    cur.execute(mark_done_query, (json_id,))
    conn.commit()


def sql_delete_task(json_id):
    if not SQL_connected:
        return None
    delete_task_query = """DELETE FROM tarefas_db
    WHERE id = %s
    """
    cur.execute(delete_task_query, (json_id,))
    conn.commit()

def update_SQL_to_JSON():
    if not SQL_connected:
            return None
    ## Updates SQL to the JSON File
    ## Get IDs that are into the JSON file, get ids that are in the SQL database
    ## If the id is in JSON File, but not SQL database, add the task to the SQL database
    try:
        list_ids_json = get_list_of_ids()
    except TypeError:
        create_json_file()
        list_ids_json = get_list_of_ids()


    query = """SELECT id FROM tarefas_db"""
    cur.execute(query)
    ids_in_sql =  {row[0] for row in cur.fetchall()}
    ids_to_add = [id_json for id_json in list_ids_json if id_json not in ids_in_sql]
    # ^^ create list of ids that are in JSON but not SQL

    # add to SQL those tasks
    tasks = json_to_list()
    for id in ids_to_add:
        sql_add_existing_task(id,
            tasks[id].get("desc"),
            tasks[id].get("status"),
            tasks[id].get("createdAt"),
            tasks[id].get("updatedAt")
        )
    conn.commit()

update_SQL_to_JSON()