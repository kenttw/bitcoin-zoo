# -*- coding: utf-8 -*-
'''
Created on 2014年12月3日

@author: kent
'''
from django.conf.urls import patterns, include, url
from rest_framework import routers
from bitcoin_api.serializers import UserViewSet, WalletViewSet , BitcoinAddressViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'wallets', WalletViewSet)
router.register(r'address', BitcoinAddressViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)