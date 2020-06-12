from django.test import TestCase
from inventory.models import TeaStallProducts
from django.urls import reverse

from django.apps import apps
from inventory.apps import InventoryConfig


class InventoryConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(InventoryConfig.name, 'inventory')
        self.assertEqual(apps.get_app_config('inventory').name, 'inventory')


class TeaStallProductTestCase(TestCase):
    def setUp(self):
        TeaStallProducts.objects.create(item_name="test1", item_description="testing", item_price=22.0,
                                        item_image='green.jpg')
        TeaStallProducts.objects.create(item_name="test3", item_description="testing3", item_price=20.0)

    def create_tea(self, item_name="tea 1", item_description="testing1", item_price=24.0):
        return TeaStallProducts.objects.create(item_name=item_name, item_description=item_description,
                                               item_price=item_price)

    def test_TeaStallProduct_Test(self):
        name = TeaStallProducts.objects.get(item_name="test1")

        self.assertEqual(name.item_name, 'test1')
        desc = TeaStallProducts.objects.get(item_description="testing")

        self.assertEqual(desc.item_description, 'testing')
        price = TeaStallProducts.objects.get(item_price=22.0)

        self.assertEqual(price.item_price, 22.0)

    def test_tea_shop_created(self):
        item_name = "test2"
        item_description = "testing2"
        item_price = 32.0
        tea1 = self.create_tea(item_name=item_name, item_description=item_description, item_price=item_price)
        tea2 = self.create_tea(item_name=item_name, item_description=item_description, item_price=item_price)
        tea3 = self.create_tea(item_name=item_name, item_description=item_description, item_price=item_price)
        qs = TeaStallProducts.objects.filter(item_name=item_name, item_description=item_description,
                                             item_price=item_price)
        self.assertEqual(qs.count(), 3)

    def test_price_inr(self):
        price = TeaStallProducts.objects.get(item_price=22.0)
        self.assertEqual(price.price_value(), 'INR 22.0')

    def test_url(self):
        image = TeaStallProducts.objects.get(item_image='green.jpg')
        self.assertEqual(image.url(), '/media/green.jpg')

    def test_image_tag(self):
        image = TeaStallProducts.objects.get(item_image='green.jpg')
        self.assertEqual(image.image_tag(), '<img src="/media/green.jpg" style="width: 95px; height:55px;" />')

    def test_image_tag_null(self):
        image = TeaStallProducts.objects.get(item_name="test3")
        self.assertEqual(image.image_tag(), 'No Image Found')

    def test_str(self):
        tea = TeaStallProducts.objects.get(item_name="test1", item_description="testing",
                                           item_price=22.0, item_image='green.jpg')
        self.assertEqual(str(tea), 'Name:{0} ,Price:INR{1},Description:{2},Image:{3}'.format(tea.item_name,
                                                                                             tea.item_price,
                                                                                             tea.item_description,
                                                                                             tea.item_image))
