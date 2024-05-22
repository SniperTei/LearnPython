"""mydrfdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from mydrfdemo.myfirstdrf import views
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
#     # TokenVerifyView,
# )

router = routers.DefaultRouter()
# router.register(r'users', views.MyUserViewSet)
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    # rest_framework_simplejwt自带的得到token 这个移动到accounts.urls了
    # path('api/v1/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # 刷新JWT 这个移动到accounts.urls了
    # path('api/v1/token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
    # 验证token
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/accounts/', include('accounts.urls')),
    path('api/v1/movie/', include('movie.urls')),
    
    # 下面是其他apps的路由， 忽略
    # path('', include('snippets.urls')),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('', include('myglory.urls'))
    # path('', include(router.urls)), # include()函数允许引用其他URLconfs 这里的路由对应的是mydrfdemo下的myfirstdrf下的views.py
    # path('', include('snipermovie.urls'))
]