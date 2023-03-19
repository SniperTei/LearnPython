from django.urls import path, include
from myglory.views import GloryHeroList
# from rest_framework import routers

# routers = routers.DefaultRouter()

urlpatterns = [
    path('gloryherolist/', GloryHeroList.as_view()),
]
