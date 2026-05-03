try:
    import psycopg
except:
    print('Library "psycopg" was not found. Skipping SQL-dependent functions.')

try:
    connstring = "postgresql://postgres:1234@localhost:5432/cli_tracker"
    conn = psycopg.connect(connstring)
    SQL_connected = True
except:
    print("Couldn't connect to SQL Database. Skipping SQL-Dependent functions")
    SQL_connected = False





