# -*- coding: utf-8 -*-
'''
Created on 2014年12月3日

@author: kent
'''
from django.conf.urls import patterns, include, url
from rest_framework import routers
from bitcoin_api.serializers import  BitcoinAddressViewSet
from bitcoin_api import views
 
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'address', BitcoinAddressViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^wallet/(?P<pk>[0-9]+)/$',views.WalletInfoView.as_view()),
    url(r'^wallet/$',views.WalletCreateView.as_view()),
    url(r'^wallet/(?P<pk>[0-9]+)/reflash/$',views.WalletReflashAddressView.as_view()),
    
)