import unittest
from app.models import User,Post
from app import db

class BlogTest(unittest.TestCase):
    def setUp(self):
        '''
        method to set all test
        '''
        self.user=User(username='usanase',pass_secure='havugima@2019'email='fusanasencoise@gmail.com')
        self.newpost=Post(title='read',category='read',user_id=self.id)
        
    def tearDown(self):
        '''