# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.core.cache import cache
import qrcode
import StringIO


from django_bitcoin.models import Wallet, currency , Profile , Escrow
from time import sleep

def qrcode_view(request, key):
    cache_key="qrcode:"+key
    c=cache.get(cache_key)
    if not c:
        img = qrcode.make(key, box_size=4)
        output = StringIO.StringIO()
        img.save(output, "PNG")
        c = output.getvalue()
        cache.set(cache_key, c, 60*60)
    return HttpResponse(c, mimetype="image/png")



def test(request):
    
    
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
