# Create your views here.

from rest_framework import viewsets, permissions
# from .models import User
from django.contrib.auth.models import User, Group
from .serializers import UserSerializer


from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope



class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


