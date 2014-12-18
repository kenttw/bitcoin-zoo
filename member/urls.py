from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User
from member.views import UserViewSet, GroupViewSet, testSignin
from django.contrib import admin
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns


admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

'''
viewset will automatically generate the URL conf
'''


urlpatterns = patterns('member.views',
    # Examples:
    # url(r'^$', 'trade_center.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^signup/', 'signup'),
    url(r'^signin/', 'signin'),
    url(r'^singout/', 'signout'),
)

urlpatterns += patterns(
    'rest_framework_jwt.views',
    url(r'^api-token-auth/', 'obtain_jwt_token'), # get token
)

# urlpatterns = format_suffix_patterns(urlpatterns)