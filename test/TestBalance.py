from django_bitcoin.models import *
master_wallet = Wallet.objects.get(label="master_wallet")
print master_wallet.total_balance()
    