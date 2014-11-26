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
    master_wallet = Wallet.objects.get(label="master_wallet")
    print master_wallet.total_balance()
    return HttpResponse("ok" )
    