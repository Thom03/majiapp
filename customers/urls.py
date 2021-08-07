from rest_framework.urlpatterns import format_suffix_patterns

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.customers.views import CustomerViewSet, UserViewset
router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'userlist', UserViewset)


api_urlpatterns = [
    path('', include(router.urls)),
]

