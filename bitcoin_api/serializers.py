# -*- coding: utf-8 -*-

from django.db import models
from rest_framework import routers, serializers, viewsets
from django_bitcoin.models import Wallet ,BitcoinAddress
from django.contrib.auth.models import User
import datetime

class WalletCreateSerializer(serializers.ModelSerializer):

# TODO: Check This Accout 是否為 KYC 合法，才能產生新的 Wallet ，否的話就回傳錯誤
#     def restore_object(self, attrs, instance=None):
#         """
#         Instantiate a new User instance.
#         """
#         assert instance is None, 'Cannot update users with CreateUserSerializer'                                
#         master_wallet = Wallet(label=attrs['label'], created_at=datetime.datetime.now() , updated_at = datetime.datetime.now())
#         return master_wallet
    class Meta:
        model = Wallet
        fields = ('label', )

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('id','created_at','transaction_counter','last_balance')
        write_only_fields = ('label',)
    
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
    

