from django.contrib.auth.models import User
from blog.models import Blog
from django.conf import settings
import os
from datetime import datetime

def create_users():
    """
    create user
    """
    super_user = User.objects.create_superuser(username='mog', email='mog@gmail.com', password='1234567890')
    user1 = User.objects.create_user(username='user1', email='user1@gmail.com', password='01234566789')
    user2 = User.objects.create_user(username='user2', email='user2@gmail.com', password='023456789')
    user3 = User.objects.create_user(username='user3', email='user3@gmail.com', password='345678980')
    return {
        'super_user': super_user,
        'user1': user1,
        'user2': user2,
        'user3': user3,
    }


def create_posts(**kwargs):
    """
    create model data for Blog
    """

    users = kwargs['users']

    sample_blogs_path = os.path.join(settings.BASE_DIR, 'blog', 'tests', 'data', 'blogs')
    file = os.path.join(sample_blogs_path, 'post1.md')
    with open(file, 'r') as post:
        content = post.read()
        post1 = Blog.objects.create(title='test blog 1 for user 1', author=users.get('user1'), publish=datetime.now(), content=content)
    file = os.path.join(sample_blogs_path, 'post2.md')
    with open(file, 'r') as post:
        content = post.read()
        post2 = Blog.objects.create(title='test blog 2 for user 1', author=users.get('user1'), publish=datetime.now(), content=content)
    file = os.path.join(sample_blogs_path, 'post3.md')
    with open(file, 'r') as post:
        content = post.read()
        post3 = Blog.objects.create(title='test blog 3 for user 1', author=users.get('user1'), publish=datetime.now(), content=content)
    file = os.path.join(sample_blogs_path, 'post2.md')
    with open(file, 'r') as post:
        content = post.read()
        post4 = Blog.objects.create(title='test blog 2 for user 2', author=users.get('user2'), publish=datetime.now(), content=content)
    file = os.path.join(sample_blogs_path, 'post3.md')
    with open(file, 'r') as post:
        content = post.read()
        post5 = Blog.objects.create(title='test blog 3 for user 2', author=users.get('user2'), publish=datetime.now(), content=content)
    file = os.path.join(sample_blogs_path, 'post2.md')
    with open(file, 'r') as post:
        content = post.read()
        post6 = Blog.objects.create(title='test blog 4 for user 2', author=users.get('user2'), publish=datetime.now(), content=content)

    return {
        'post1': post1, 
        'post2': post2,
        'post3': post3,
        'post4': post4, 
        'post5': post5,
        'post6': post6,
    }