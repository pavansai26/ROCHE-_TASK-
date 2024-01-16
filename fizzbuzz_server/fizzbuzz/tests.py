from django.test import TestCase

# Create your tests here.
import unittest
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from fizzbuzz.models import FizzBuzzRequest
from fizzbuzz.serializers import FizzBuzzSerializer

class FizzBuzzSerializerTestCase(TestCase):

    def test_valid_data(self):
        data = {'int1': 3, 'int2': 5, 'limit': 16, 'str1': 'fizz', 'str2': 'buzz'}
        serializer = FizzBuzzSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.data['result'], '1,2,fizz,4,buzz,fizz,7,8,fizz,buzz,11,fizz,13,14,fizzbuzz,16')

    

class FizzBuzzViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_valid_post_request(self):
        data = {'int1': 3, 'int2': 5, 'limit': 16, 'str1': 'fizz', 'str2': 'buzz'}
        response = self.client.post(reverse('fizzbuzz'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(FizzBuzzRequest.objects.count(), 1)
        self.assertEqual(FizzBuzzRequest.objects.first().result, '1,2,fizz,4,buzz,fizz,7,8,fizz,buzz,11,fizz,13,14,fizzbuzz,16')

    

class StatsViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        FizzBuzzRequest.objects.create(int1=3, int2=5, limit=16, str1='fizz', str2='buzz', hits=2)
        FizzBuzzRequest.objects.create(int1=7, int2=11, limit=20, str1='foo', str2='bar', hits=1)

    def test_get_most_frequent_request(self):
        response = self.client.get(reverse('stats'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'most_frequent_params': {'int1': 3, 'int2': 5, 'limit': 16, 'str1': 'fizz', 'str2': 'buzz'}, 'hits': 2})

    
