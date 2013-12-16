"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest() #this is an HttpReqiest object which is what Django will see when a user's browser asks for a page.
        response = home_page(request) #we pass it to our home page view which gives us a response
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html) #we use the decode to covert the response. content bytes into a Python unicode string, which allows us to comapre strings with strings.
        