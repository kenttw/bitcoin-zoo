from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
# import django_bitcoin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'core.views.home', name='home'),
    # url(r'^core/', include('core.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
#     url(r'^test/', include('django_bitcoin.urls')),
    url(r'^' , include('django_bitcoin.urls')),
#     url(r'^debuginfo/$', views.debug),

)
