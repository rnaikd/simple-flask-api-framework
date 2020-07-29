class Info:
    version = 1
    author = 'Rahul N'
    email = 'naikrahulda@gmail.com'


    def get(self):
        return {
            'version': self.version,
            'author': self.author,
            'author_email': self.email
        }
