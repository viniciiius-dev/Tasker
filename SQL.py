import psycopg

connstring = "postgresql://postgres:1234@localhost:5432/cli_tracker"
with psycopg.connect(connstring) as conn:
    cur = conn.cursor()
    create_table = ("""CREATE TABLE IF NOT EXISTS tarefas (
            id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            descricao VARCHAR(80) NOT NULL,
            status VARCHAR(11) DEFAULT 'todo' NOT NULL,
            criadoEm TIMESTAMPTZ(0) DEFAULT CURRENT_TIMESTAMP NOT NULL,
            atualizadoEm TIMESTAMPTZ(0) DEFAULT CURRENT_TIMESTAMP NOT NULL
    )""")
    def sql_add_task(desc):
        create_task_query = """INSERT INTO tarefas (descricao)
        VALUES ('%s')
        """ % (desc)
        cur.execute(create_task_query)

    def sql_update_task(id, desc):
        update_task_query = """UPDATE tarefas
        SET descricao = '%s'
        WHERE id = %s
        """ % (desc, id)
        cur.execute(update_task_query)
    def sql_delete_task(id):
        delete_task_query = """DELETE FROM tarefas
        WHERE id = %s
        """ % (id)
        cur.execute(delete_task_query)


    cur.execute(create_table)
    conn.commit()
