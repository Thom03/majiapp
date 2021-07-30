from rest_framework.urlpatterns import format_suffix_patterns

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.customers import views

router = DefaultRouter()
router.register(r'customers', views.CustomerViewSet)

urlpatterns = format_suffix_patterns([
    path('', include(router.urls)),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view())


])
