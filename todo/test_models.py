from django.test import TestCase
from .models import Item

# Create your tests here.
class TestModels(TestCase):

    def test_done_default_to_false(self):
        item = Item.objects.create(name='Test todo Model')
        self.assertFalse(item.done)