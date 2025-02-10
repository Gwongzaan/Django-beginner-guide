from django.http import HttpRequest
from django.shortcuts import resolve_url
from django.test import TestCase
from django.urls import resolve

from blog.views import titles


class BlogPageTest(TestCase):
    def test_blog_url_resolves_to_blog_titles_view(self):
        found = resolve(resolve_url("blog:titles"))
        self.assertEqual(found.func, titles)

    def test_blog_url_resolves_to_blog_titles_view_another_method(self):
        response = self.client.get(resolve_url("blog:titles"))
        self.assertTemplateUsed(response, "blog/titles.html")

    def test_blog_titles_returns_correct_html(self):
        request = HttpRequest()
        response = titles(request)
        html = response.content.decode("utf8").strip()
        self.assertTrue(html.startswith("<!DOCTYPE html>"))
        self.assertIn("<title>Titles</title>", html)
        self.assertTrue(html.endswith("</html>"))

    def test_blog_titles_returns_correct_html_method_2(self):
        response = self.client.get(resolve_url("blog:titles"))
        html = response.content.decode("utf8")
        self.assertTrue(html.startswith("<!DOCTYPE html>"))
        self.assertIn("<title>Titles</title>", html)
        self.assertTrue(html.strip().endswith("</html>"))
        self.assertTemplateUsed(response, "blog/titles.html")
