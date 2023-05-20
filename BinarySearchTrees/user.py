class User:
    # Initializes a new User object.
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        #print('User Created')

    
    # Returns a string representation of the User object.
    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)
    
    def __str__(self):
        return self.__repr__()