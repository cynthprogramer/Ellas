from sqlalchemy import create_engine

#uma forma mais simples e pra algo que ja esta no disco do pc
#engine = create_engine("sqlite://bancoEllas",echo = True) 

#substituir de acordo com o computador e conta que estive usando
username = 'root'
password = 'labinfo'
host = '127.0.0.1'
port = 3306
database = 'ellasbanco'

engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')

connection = engine.connect()
print("deu certooo")
connection.close()




