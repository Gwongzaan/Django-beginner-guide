from django.test import TestCase
from django.urls import reverse
from django.http import Http404
from . import setup_model_data

class TitleViewTest(TestCase):
    def setUp(self):
       self.users =  setup_model_data.create_users()
       self.posts = setup_model_data.create_posts(users=self.users)

    def test_title_view_status_code(self):
        response = self.client.get(reverse('blog:titles'))
        self.assertEqual(response.status_code, 200)

    def test_title_view_template_used(self):
        response = self.client.get(reverse('blog:titles'))
        self.assertTemplateUsed(response, 'blog/titles.html')

    def test_title_view_context(self):
        response = self.client.get(reverse('blog:titles'))

        self.assertIn('title', response.context)
        self.assertEqual('My blogs', response.context['title'])

        self.assertIn('blogs', response.context)
        self.assertEqual(response.context['blogs'].count(), len(self.posts))
        

        
class DetailViewTest(TestCase):
    def setUp(self):
        self.users = setup_model_data.create_users()
        self.posts = setup_model_data.create_posts(users=self.users)

    def test_detail_view_status_code(self):
        response = self.client.get(reverse('blog:detail', kwargs={'id': 1}))
        self.assertEqual(response.status_code, 200)

    def test_detail_template_used(self):
        response = self.client.get(reverse('blog:detail', kwargs={'id': 1}))
        self.assertTemplateUsed(response, 'blog/detail.html')

    def test_detail_view_context(self):
        post = self.posts['post1']
        response = self.client.get(reverse('blog:detail', kwargs={"id": post.id}))
        self.assertIn('post', response.context)
        self.assertEqual(post.title, response.context['post'].title)