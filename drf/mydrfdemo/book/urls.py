from django.urls import path, include
from .views import BookListView
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'custom-users', CustomUserView)

urlpatterns = [
  # ViewSet的用这种
  # path('', include(router.urls)), # include()函数允许引用其他URLconfs
  # APIView的用这种
  path('book-list/', BookListView.as_view(), name='book-list'),
  # path('custom-users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
]