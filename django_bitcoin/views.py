# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.core.cache import cache
import qrcode
import StringIO


from django_bitcoin.models import Wallet, currency 
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

def debug(request):
#     master_wallet = Wallet.objects.get(label="master_wallet")
#     print master_wallet.total_balance()
#     return HttpResponse("ok" )
#     testSpent()
    testCreateWallet()
    return HttpResponse("ok" )
def testCreateWallet():
    from django_bitcoin.models import *
    master_wallet, created = Wallet.objects.get_or_create(label="master_wallet")
    recv_address = master_wallet.receiving_address(fresh_addr=False)
    print recv_address

def testSpent():
    from decimal import Decimal
    master_wallet = Wallet.objects.get(label="master_wallet")
    master_wallet.send_to_address("1HijmGewaaz7bQLNXMZiBzSgYLvhRFJEJv", Decimal("0.000221141"), "Just Test")
    