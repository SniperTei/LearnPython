from django.urls import path, include
from myglory.views import GloryHeroList, GloryHeroDetail
# from rest_framework import routers
# from . import views


# routers = routers.DefaultRouter()
# routers.register('gkinglory', GloryHeroList, GloryHeroDetail)

urlpatterns = [
    path('gloryherolist/', GloryHeroList.as_view({
        'get': 'get_all_heros', 
        'post': 'add_one_hero'})
    ),
    path('gloryherolist/<int:pk>', GloryHeroDetail.as_view({    
        'get': 'get_one_hero',
        'put': 'edit_one_hero',
        'delete': 'delete_one_hero'})
    ),
]

# urlpatterns += routers.urls
