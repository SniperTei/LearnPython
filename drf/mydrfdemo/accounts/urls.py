from django.urls import path, include
from .views import CustomUserView
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'custom-users', CustomUserView)

urlpatterns = [
  # ViewSet的用这种
  # path('', include(router.urls)), # include()函数允许引用其他URLconfs
  # APIView的用这种
  path('custom-users/', CustomUserView.as_view(), name='user-list'),
  # path('custom-users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
]