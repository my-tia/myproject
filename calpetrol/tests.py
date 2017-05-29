from django.core.urlresolvers import resolve
from django.test import TestCase
from django.shortcuts import render_to_response

from calpetrol.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)


    def test_home_page_returns_correct_html(self):
        request = render_to_response('calpetrol/homepage.html')  
        response = home_page(request)  
        self.assertTrue(response.content.startswith(b'<html>'))  
        self.assertIn(b'<title>calculate petrol for your car</title>', response.content)  
        self.assertTrue(response.content.endswith(b''))  
