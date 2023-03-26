from django.urls import path, include
from myglory.views import GloryHeroList, GloryHeroDetail
# from rest_framework import routers

# routers = routers.DefaultRouter()

urlpatterns = [
    path('gloryherolist/', GloryHeroList.as_view()),
    path('gloryherolist/<int:id>', GloryHeroDetail.as_view()),
]
