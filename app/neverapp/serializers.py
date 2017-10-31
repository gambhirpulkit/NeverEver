from rest_framework import serializers
# from .models import User
from django.contrib.auth.models import User, Group

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ('name', 'email', 'work', 'phone')
        fields = '__all__'
