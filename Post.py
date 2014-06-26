import datetime
import json
import os

class Post:
    def __init__(self, post):
        self.author = str(os.environ.get('AUTHOR'))
        self.timestamp = str(datetime.datetime.utcnow())
        self.content = post

    def json(self):
        return json.dumps(self.__dict__)