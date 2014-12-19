from django.shortcuts import render
from bitcoin_api.serializers import WalletSerializer ,WalletCreateSerializer
from django_bitcoin.models import Wallet
from django.http import Http404
from rest_framework.views import APIView 
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

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
# curl -X POST http://localhost:8000/api/wallet/ -d  'label=fsdfdf'
class WalletCreateView(generics.CreateAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    model = Wallet
    serializer_class = WalletCreateSerializer
    def post(self, request, *args, **kwargs):
        return generics.CreateAPIView.post(self, request, *args, **kwargs)
class WalletReflashAddressView(generics.RetrieveAPIView):
    model = Wallet
    serializer_class = WalletSerializer
    permission_classes = [
        permissions.AllowAny
    ]
    
    def get(self, request,pk):
        wallet = Wallet.objects.get(id=pk)
        wallet.receiving_address()
        serializer = WalletSerializer(wallet)
        return Response(serializer.data)


