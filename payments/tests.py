from django.test import TestCase

# Create your tests here.

from .models import *

# Create your tests here.
class SimpleTest(TestCase):
    def test_basic_addition(self):
    	print "hai"
        """
        Tests that 1 + 1 always equals 2.
        """
        self.failUnlessEqual(1 + 1, 2)

    def test(self):
    	print "testing"
    	self.failUnlessEqual(1+1,2)

'''
Run test case by using follwoing commands

python manage.py test

python manage.py test scrapcars.tests.CartradeTest.test_cartrade


'''

