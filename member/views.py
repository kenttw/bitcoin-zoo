from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect

from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from serializer import UserSerializer, GroupSerializer
from rest_framework import status
from rest_framework import parsers
from rest_framework import renderers
from rest_framework_jwt import utils
from rest_framework_jwt.authentication import JSONWebTokenAuthentication as jwt_auth
from rest_framework_jwt.serializers import JSONWebTokenSerializer
# userena
from userena import views


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    authentication_classes = (BasicAuthentication, )

    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


def signup(request):
    '''
    a simple overwritten the signup view
    '''
    return views.signup(request, success_url='/home/')


def signout(request):
    '''
    '''
    return views.signout(request, template_name='home.html')


def signin(request):
    '''
    '''
    # this is a little trick to hack the userena signin function
    return views.signin(request, redirect_signin_function=lambda *arg: '/home/')


class testSignin(APIView):

    '''
    API View that receives a POST with a user's username and password.

    Returns a JSON Web Token that can be used for authenticated requests.
    '''

    throttle_classes = ()
    permission_classes = ()
    authentication_classes = ()
    parser_classes = (parsers.FormParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = JSONWebTokenSerializer
    jwt = jwt_auth()

    def post(self, request):
        '''
        a known issue now...
        a segment fault happens if you login and then logout and login again..
        '''
        serializer = testSignin.serializer_class(data=request.DATA)

        if serializer.is_valid():

            payload = utils.jwt_decode_handler(serializer.object['token'])
            user = self.jwt.authenticate_credentials(payload)

            # below is a tric for authenticate..
            # due to the authentication in django -- it need username and password,
            # however, decode of jwt doesn't contain password.
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            # user = authenticate(username=user, nopass=True)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/home/')
                else:
                    raise Exception('user not active')

            else:
                raise Exception('not valid user')

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

