from django_bitcoin.models import Wallet, currency
from django.db import models
from django.db.models import *
from time import sleep

class Profile(models.Model):
    wallet = ForeignKey(Wallet)
    outgoing_bitcoin_address = CharField()

class Escrow(models.Model):
    wallet = ForeignKey(Wallet)
    buyer_happy = BooleanField(default=False)

buyer=Profile.objects.create()
seller=Profile.objects.create()

purchase=Escrow.objects.create()

AMOUNT_USD="9.99"

m=currency.Money(AMOUNT_USD, "USD")
btc_amount=currency.exchange(m, "BTC")

print "Send "+str(btc_amount)+" BTC to address "+buyer.wallet.receiving_address()

sleep(5000) # wait for transaction

# if p1.wallet.total_balance()>=btc_amount:
#     p1.send_to_wallet(purchase, btc_amount)
# 
#     sleep(1000) # wait for product/service delivery
# 
#     if purchase.buyer_happy:
#         purchase.wallet.send_to_wallet(seller.wallet)
#         seller.wallet.send_to_address(seller.outgoing_bitcoin_address, seller.wallet.total_balance())
#     else:
#         print "WHY U NO HAPPY"
#         #return bitcoins to buyer, 50/50 split or something