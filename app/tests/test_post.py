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
        delete the test
        '''
        User.query.delete()
        Post.query.delete()

    def test_check_instance_variables(self):
        '''
        test 
        '''
        self.assertEquals(self.newpost.title,'read')
        self.assertEquals(self.newpost.category.'read')
        self.assertEquals(self.newpost.user_id,self.user_admin)

    def test_save(self):
        '''
        saving
        '''
        self.newpost.save_u()
        got_post=Post.query.get(1)
        self.assertEquals(le(got_post)==1)
