from django.test import TestCase

from . import models


class TestPerson(TestCase):

    def test_read_write(self):
        """Make sure we can read/write to the person table"""
        person = models.Person.objects.create(name='Lisa')

        self.assertTrue(models.Person.objects.filter(name=person.name).exists())
