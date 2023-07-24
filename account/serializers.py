
from rest_framework import serializers

from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'password', 'avatar', 'created_at', 'last_login', 'created_by', 'status']
