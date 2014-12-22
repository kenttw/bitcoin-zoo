"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django_bitcoin import tasks
from bitcoin import bci
from django_bitcoin.models import Wallet , BitcoinAddress

class BasicTest(TestCase):
#     def test_basic_addition(self):
#         """
#         Tests that 1 + 1 always equals 2.
#         """
#         self.assertEqual(1 + 1, 2)
    def setUp(self):
        self.w1 = Wallet.objects.create(label='test wallet')
        self.w1.save()
        self.w1.receiving_address()

        
    def test_pytool_unspent(self):
        # 3CVVtR2coaLqBbav3XcP8VdekR4CvdtYCg is kent's personal bitcoin address . you are welcome send you bicoin to this address !!
        balance = bci.unspent('3CVVtR2coaLqBbav3XcP8VdekR4CvdtYCg')[0]['value']
        self.assertEqual(balance, 500000, 'use pybitcoion tool to get balance fail')
    
    def test_reflash_wallet_address(self):
        self.w1.receiving_address()
        list = BitcoinAddress.objects.all()
        self.assert_(len(list) > 0, 'get new bitocoin address fial')
        
    def test_sync_alladdress_balance(self):
        tasks.sync_alladdress_balance()
        
    def test_address_getbalance(self):
        ads = BitcoinAddress.objects.filter(wallet=self.w1)
        for ad in ads :
            print ad.getunspent()
