from django.urls import path, include
from .views import MovieView
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'custom-users', CustomUserView)

urlpatterns = [
  # ViewSet的用这种
  # path('', include(router.urls)), # include()函数允许引用其他URLconfs
  # APIView的用这种
  path('movie-list/', MovieView.as_view(), name='movie-list'),
  # path('custom-users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
]