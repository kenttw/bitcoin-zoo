from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from core import views
# import django_bitcoin
admin.autodiscover()


# Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'wallets', WalletViewSet)
# router.register(r'address', BitcoinAddressViewSet)
urlpatterns = patterns(
    '',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bitcoin/', include('django_bitcoin.urls')),
    url(r'^api/', include('bitcoin_api.urls')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),
    # overwirtte some views of userena
    url(r'^member/', include('member.urls')),
    url(r'^member/', include('userena.urls')),
    url(r'^home/', views.home),

)
