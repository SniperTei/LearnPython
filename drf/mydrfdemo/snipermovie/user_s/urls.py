from django.urls import path, include
from rest_framework import routers
# from user_s import views
from snipermovie.user_s import views
# from rest_framework.routers import DefaultRouter
# from user_s import views
# from django.contrib import admin

# Create a router and register our viewsets with it.
# router = DefaultRouter()
# router.register(r'snippets', views.SnippetViewSet,basename="snippet")
# router.register(r'users', views.UserViewSet,basename="user")

router = routers.DefaultRouter() # 创建路由器
# router.register(r'user_s', views.SUserList, basename="snipermovie") # 注册视图集

# The API URLs are now determined automatically by the router.
urlpatterns = [
    # path('', include(router.urls)),
    path('', views.SUserList.as_view(), name='user-list'),
]