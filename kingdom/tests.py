from django.urls import resolve
from django.test import TestCase
from kingdom.views import home_page

class SmokeTest(TestCase):

    def test_home_page_resolving(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
