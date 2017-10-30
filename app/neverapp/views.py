from django.shortcuts import render

# Create your views here.

#  # howdy/views.py
# from django.shortcuts import render
# from django.views.generic import TemplateView
#
# # Create your views here.
# class HomePageView(TemplateView):
#     template_name = 'index.html'
#                 # or
#     # def get(self, request, **kwargs):
#     #     return render(request, 'index.html', context=None)
#

from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# from rest_framework import generics
# from .models import User
# from .serializers import UserSerializer
#
# class UserViewSet(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     # permission_classes = (IsAdminOrReadOnly,)
