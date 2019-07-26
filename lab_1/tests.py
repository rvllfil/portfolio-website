from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index, mhs_name, calculate_age
from django.http import HttpRequest
from datetime import date
import unittest


# Create your tests here.

class Lab1UnitTest(TestCase):

    def test_hello_name_is_exist(self):
        response = Client().get('/lab-1/')
        self.assertEqual(response.status_code, 200)

    def test_using_index_func(self):
        found = resolve('/lab-1/')
        self.assertEqual(found.func, index)
