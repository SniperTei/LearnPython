from django.urls import path, include
from .views import CustomUserView, RegisterView
from accounts.views import MyTokenObtainPairView, MyTokenRefreshView
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'custom-users', CustomUserView)

urlpatterns = [
  # ViewSet的用这种
  # path('', include(router.urls)), # include()函数允许引用其他URLconfs
  # APIView的用这种
  path('custom-user-list/', CustomUserView.as_view(), name='user-list'),
  # 注册
  path('register/', RegisterView.as_view(), name='register'),
  # 登录
  path('login/', MyTokenObtainPairView.as_view(), name='login'),
  # 刷新JWT
  path('token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
  # path('custom-users/<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
]