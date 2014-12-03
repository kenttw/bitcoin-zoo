from django.db import models
from rest_framework import routers, serializers, viewsets
from django_bitcoin.models import Wallet
from django.contrib.auth.models import User

# Create your models here.
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Serializers define the API representation.
class WalletSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_attrs):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Wallet.objects.create(label="master_wallet")    
    class Meta:
        model = Wallet
        fields = ('created_at', 'updated_at', 'label', 'transaction_counter')

# ViewSets define the view behavior.
class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    

