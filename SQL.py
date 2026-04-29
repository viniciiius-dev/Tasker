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
        create_task_string = """INSERT INTO tarefas (descricao)
        VALUES ('%s')
        """ % (desc)
        cur.execute(create_task_string)

    def sql_update_task(id, desc):
        pass
    def sql_delete_task(id):
        pass

    # cur.execute(create_table)
    # cur.execute(sql_add_task("do laundry"))
    # conn.commit()
