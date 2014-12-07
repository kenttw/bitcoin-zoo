from django.shortcuts import render
from bitcoin_api.serializers import WalletSerializer  
from django_bitcoin.models import Wallet
from django.http import Http404
from rest_framework.views import APIView 
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class WalletInfoView(APIView):
    
    def get(self, request, pk):
        wallet = Wallet.objects.get(id=pk)
        serializer = WalletSerializer(wallet)
        return Response(serializer.data)
#     def post(self, request, pk):
#         pass
#     def delete(self, request, pk):
#         pass

class WalletCreateView(generics.CreateAPIView):
    model = Wallet
    serializer_class = WalletSerializer
    permission_classes = [
        permissions.AllowAny
    ]
#     def post(self, request):
#         request.
#         wallet = Wallet.objects.get_or_create(uid=request.DATA['uid'],lable=request.DATA['lable'])
#         serializer = WalletSerializer(wallet)
#         return Response(serializer.data)

class ListWalets(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
#     authentication_classes = (authentication.TokenAuthentication,)
#     permission_classes = (permissions.IsAdminUser,)

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)