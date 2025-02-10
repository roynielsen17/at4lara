

class Crud(object):
    def __init__(self):
        """
        """
        pass
        
    def create(self):
        """
        """
        pass

    def read(self):
        """
        """
        pass

    def update(self):
        """
        """
        pass

    def delete(self):
        """
        """
        pass


class risCrud(Crud):

    def __init__(self, logger, credentials, location):
        """
        """
        if isinstance(logger, CyLogger):
            self.logger = logger
        else:
            self.logger = CyLogger(30)
            self.logger.initializeLogs()
        try:
            self.user = credentials[user]
            self.pass = credentials[pass]
        except:
            pass
        self.location = location

    def connect(self, instance: dict):
		"""
		instance: dict of location & credentials, if necessary- which
		          could include certificate, and/or username, password,
		          key, etc..  Could just be a file location for a text
		          only file, or a database with user and credential
		          protected instance.
		"""
		pass
 
    def create(self, instaciation: dict):
        """
        Use the imported RIS data structure to create the RIS table
        sftructures.
        instaciation: whatever is required to create the database, at least
                      a location, perhaps user and password/key/cert
                      credentials, etc.
        """
        pass

    def read(self, data_query: dict):
        """
        """
        pass

    def update(self, data: dict):
        """
        """
        pass

    def delete(self, data: dict):
        """
        """
        pass

    def log(self, data: dict, channel: dict):
        """
        """
        pass
