import cx_Oracle

def DataBaseConnection():
    dsn = cx_Oracle.makedsn(host='oracle.fiap.com.br', port=1521, sid='ORCL')
    conn = cx_Oracle.connect(user='rm552605', password='020904', dsn=dsn)
    cursor = conn.cursor()
    return conn, cursor
