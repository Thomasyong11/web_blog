import uuid

from src.common.database import Database
import datetime

__author__="yong"

"""class Post(object): #giving out post properties
    def __init__(self):
        self.title = "this is my title"
        self.content = "this is some content"
        self.author = "yong" """


class Post(object):
    #  giving out post properties
    def __init__(self, blog_id, title, content, author, created_date= datetime.datetime.utcnow(), _id= None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = created_date
        self._id = uuid.uuid4().hex if _id is None else _id

    def save_to_mongo(self):
        Database.insert(collection='posts',
                        data=self.json())

    def json(self):
        return{
            '_id': self._id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date
        }
    """json code returns a json representation of the data created
    and the save to mongo inserts the json representation into the database"""
    @classmethod
    def from_mongo(cls, id):
        post_data = Database.find_one(collection='posts', query={'_id': id})
        return cls(**post_data)

    """   above class is a simplified method of what's below
     def from_mongo(cls, id):
        post_data = Database.find_one(collection='posts', query={'_id': id})
        return cls(blog_id=post_data['blog_id'],
                   title=post_data['title'],
                   content=post_data['content'],
                   author=post_data['author'],
                   created_date=post_data['created_date'],
                   _id=post_data['_id'])"""

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts', query={'blog_id': id})]
