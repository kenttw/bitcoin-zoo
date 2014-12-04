from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User
from member import views
from django.contrib import admin
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns


admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

'''
viewset will automatically generate the URL conf
'''


urlpatterns = patterns('member.views',
    # Examples:
    # url(r'^$', 'trade_center.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^signup/', 'signup'),
    url(r'^signin/', views.testSignin.as_view()),
    url(r'^singout/', views.signout),
)

urlpatterns += patterns(
    'rest_framework_jwt.views',
    url(r'^api-token-auth/', 'obtain_jwt_token'), # get token
)

# urlpatterns = format_suffix_patterns(urlpatterns)