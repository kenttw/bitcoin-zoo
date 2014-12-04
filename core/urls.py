from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from rest_framework import routers
from bitcoin_api.serializers import UserViewSet, WalletViewSet , BitcoinAddressViewSet
import bitcoin_api
# import django_bitcoin
admin.autodiscover()

 

# Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'wallets', WalletViewSet)
# router.register(r'address', BitcoinAddressViewSet)






urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bitcoin/' , include('django_bitcoin.urls')),
    url(r'^api/', include('bitcoin_api.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
