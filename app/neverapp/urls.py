# from django.conf.urls import url
# from neverapp import views
#
# urlpatterns = [
#     # url(r'^$', views.HomePageView.as_view()),
#     url(r'^users/(?P<pk>[0-9]+)/$', views.UserViewSet.as_view()),
# ]

from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = router.urls