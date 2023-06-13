from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title='Water', price=0, inventory=100)
        Menu.objects.create(title='Boiled Rice', price=1.50, inventory=100)

    def test_getall(self):
        item1 = Menu.objects.get(name='Water')
        item2 = Menu.object.get(name="Boiled Rice")
        self.assertEqual(item1, 'Water : 0')
        self.assertEqual(item2, 'Boiled Rice : 1.50')