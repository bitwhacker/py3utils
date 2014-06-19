"""Database helper methods"""
from .config import Config

class ModelHelper:
    """Database helper methods"""

    def getenginestring(self, config_section):
        config = Config()
        dbtype = config.get(config_section, 'dbtype')
        dbname = config.get(config_section, 'dbname')

        if dbname == None:
            raise NameError('Database name not defined')

        if dbtype == None:
            raise NameError('Database type not defined')

        if dbtype.lower() == 'sqlite':
            return 'sqlite:///' + dbname + '.db'
        elif dbtype.lower() == 'mysql':
            dbuser = config.get(config_section, 'user')
            if dbuser == None:
                raise NameError('Database user not defined')
            dbpass = config.get(config_section, 'password')
            if dbpass == None:
                raise NameError('Database poassword not defined')
            dbhost = config.get(config_section, 'hostname')
            if dbhost == None:
                raise NameError('Database hostname not defined')
            dbport = config.get(config_section, 'port')
            if dbport == None:
                raise NameError('Database port not defined')

            return 'mysql://' + dbuser + ':' + dbpass + '@' + \
                dbhost + ':' + dbport + '/' + dbname
        else:
            raise NameError('Invalid database type')
