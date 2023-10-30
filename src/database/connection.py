import psycopg2 as connector

def create_connection():
  connection = None
  try:
    connection = connector.connect(dbname='av-python', user='postgres', port='5432', host='localhost')
    return connection
  
  except connector.Error as err:
    print( "database error: ", err)

  return connection
