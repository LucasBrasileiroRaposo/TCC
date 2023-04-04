import psycopg2

#configurações
host = 'localhost'
dbname = 'tcc'
user = 'postgres'
password = 'postgres'
sslnode = 'require'

#conexão
conn_string = 'host={0} user={1} dbname={2} password={3} sslnode={4}'.format(host, user, dbname, password, sslnode);
conn = psycopg2.connect(conn_string);
print('connected')