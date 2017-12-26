from django.test import TestCase

from example.models import Purchase, PurchaseItem


class ManagersTestCase(TestCase):

    def setUp(self):
        purchase = self.purchase2k14 = Purchase.objects.create()
        purchase.created_on = purchase.created_on.replace(year=2014)
        purchase.save()
        self.purchaseitem2k14 = purchase.purchaseitem_set.create()

        purchase = Purchase.objects.create()
        purchase.created_on = purchase.created_on.replace(year=2015)
        purchase.save()
        purchase.purchaseitem_set.create()

        purchase = self.purchase = Purchase.objects.create()
        self.purchaseitem = purchase.purchaseitem_set.create()

    def test_this_year(self):
        self.assertQuerysetEqual(Purchase.objects.this_year(),
                                 [repr(self.purchase)])

        self.assertQuerysetEqual(PurchaseItem.objects.this_year(),
                                 [repr(self.purchaseitem)])

    def test_from_year(self):
        self.assertQuerysetEqual(Purchase.objects.from_year(2014),
                                 [repr(self.purchase2k14)])

        self.assertQuerysetEqual(PurchaseItem.objects.from_year(2014),
                                 [repr(self.purchaseitem2k14)])


class ModelsTestCase(TestCase):
    def test_uuid_auto_generated(self):
        purchase = Purchase.objects.create()
        self.assertIsNotNone(purchase.uuid)
