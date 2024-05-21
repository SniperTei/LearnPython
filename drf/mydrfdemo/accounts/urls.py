from django.urls import path
from .views import CustomUserViewSet

urlpatterns = [
  path('custom-users/', CustomUserViewSet.as_view(), name='user-list'),
  # path('custom-users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
]