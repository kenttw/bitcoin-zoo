# -*- coding: utf-8 -*-

from django.db import models
from rest_framework import routers, serializers, viewsets
from django_bitcoin.models import Wallet ,BitcoinAddress
from django.contrib.auth.models import User
import datetime
from openpyxl.cell import read_only

class WalletCreateSerializer(serializers.ModelSerializer):

# TODO: Check This Accout 是否為 KYC 合法，才能產生新的 Wallet ，否的話就回傳錯誤
# >curl -X POST http://localhost:8000/api/wallet/ -d  '{"label":"fsdfdf"}'
    def restore_object(self, attrs, instance=None):
        """
        Instantiate a new User instance.
        """
        assert instance is None, 'Cannot update users with CreateUserSerializer'                                
        master_wallet = Wallet(label=attrs['label'], created_at=datetime.datetime.now() , updated_at = datetime.datetime.now())
#         master_wallet.save()
        return master_wallet
    class Meta:
        model = Wallet
        write_only_fields = ('label',)
        fields = ('label','id' ,'last_balance')

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('label','id','created_at','transaction_counter','last_balance')
#         write_only_fields = ('label',)
    
class BitcoinAddressSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_attrs):
        return BitcoinAddress.objects.create(label="test_address")    
    class Meta:
        model = BitcoinAddress
        fields = ('address', 'created_at', 'active', 'least_received')

# ViewSets define the view behavior.
class BitcoinAddressViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BitcoinAddress.objects.all()
    serializer_class = BitcoinAddressSerializer
    

