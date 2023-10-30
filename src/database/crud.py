import psycopg2 as connector

class AppBD:
    
    def __init__(self):
        pass

    def abrirConexao(self):
        self.connection = None
        try:
            self.connection = connector.connect(dbname='av-python', user='postgres', port='5432', host='localhost')

        except connector.Error as err:
            print( "database error: ", err)

        return self.connection
