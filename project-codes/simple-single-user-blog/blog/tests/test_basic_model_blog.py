from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Blog
from . import setup_model_data

class BlogModelTest(TestCase):
    def setUp(self):
       self.users = setup_model_data.create_users()
       self.posts = setup_model_data.create_posts(users=self.users) 
    
    def test_post_creation(self):
        self.assertEqual(self.posts.get('post1').title, 'test blog 1 for user 1')
        self.assertEqual(self.posts.get('post1').author, self.users.get('user1'))

    def test_delete_user_cascade(self):
        posts = Blog.objects.filter(author=self.users.get('user1'))
        self.assertEqual(posts.count(), 3)
        
        users = User.objects.all()
        self.assertEqual(users.count(), 4)

        User.objects.filter(username=self.users.get('user1').username).delete()
        users = User.objects.all()
        self.assertEqual(users.count(), 3)

        posts = Blog.objects.filter(author=self.users.get('user1'))
        self.assertEqual(posts.count(), 0)

    # TODO
    def test_missing_required_field(self):
        pass

    def test_invalid_data_format(self):
        pass

    def test_constraint(self):
        pass

