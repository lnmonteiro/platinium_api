import pyodbc
import os
import logging

def get_db_connection():
    """Retorna uma conexão com o banco de dados"""
    try:
        conn_string = os.environ["DB_CONNECTION_STRING"]
        return pyodbc.connect(conn_string)
    except Exception as e:
        logging.error(f"Erro ao conectar ao banco: {str(e)}")
        raise

def execute_query(query, params=None):
    """Executa uma query e retorna os resultados"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        
        columns = [column[0] for column in cursor.description]
        results = []
        
        for row in cursor.fetchall():
            results.append(dict(zip(columns, row)))
        
        return results
    finally:
        cursor.close()
        conn.close()