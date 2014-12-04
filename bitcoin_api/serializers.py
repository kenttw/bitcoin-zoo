from django.db import models
from rest_framework import routers, serializers, viewsets
from django_bitcoin.models import Wallet ,BitcoinAddress
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class WalletSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_attrs):
        return Wallet.objects.create(label="master_wallet")    
    class Meta:
        model = Wallet
        fields = ('created_at', 'updated_at', 'label', 'transaction_counter')

class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

    
class BitcoinAddressSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_attrs):
        return BitcoinAddress.objects.create(label="test_address")    
    class Meta:
        model = BitcoinAddress
        fields = ('address', 'created_at', 'active', 'least_received')

# ViewSets define the view behavior.
class BitcoinAddressViewSet(viewsets.ModelViewSet):
    queryset = BitcoinAddress.objects.all()
    serializer_class = BitcoinAddressSerializer
    

