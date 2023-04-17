import psycopg2

#configurações

# sslnode = 'require'
class db_connect():
    
    # cur.execute(" CREATE TABLE test2 ( id SERIAL PRIMARY KEY ," + 
    #             "questionNumber INT ," +
    #             "area VARCHAR(100)," +
    #             "body TEXT, " + 
    #             "answer varchar(1), " + 
    #             "year INT );")
    def save_question(label, area, text, year):
        host = 'localhost'
        dbname = 'tcc'
        user = 'postgres'
        password = 'postgres'
        #conexão

        conn_string = 'host={0} user={1} dbname={2} password={3}'.format(host, user, dbname, password)
        conn = psycopg2.connect(conn_string)
        print('connected')
        cur = conn.cursor()
        cur.execute("INSERT INTO test2 (questionNumber, area, body, year) values (%s, %s, %s, %s)", (label, area, text, year))
    
        conn.commit()
        cur.close()
