from django.urls import path, include
from myglory.views import GloryHeroView
from rest_framework.routers import DefaultRouter
from . import views


# router = DefaultRouter()
# router.register('kingglory', GloryHeroList, basename='kingglorybasename')

urlpatterns = [
    path('gloryherolist/', GloryHeroView.as_view({
        'get': 'get_all_heros',
        'post': 'add_one_hero'})
    ),
    path('gloryherolist/<int:pk>', GloryHeroView.as_view({    
        'get': 'get_one_hero',
        'put': 'edit_one_hero',
        'delete': 'delete_one_hero'})
    ),
]

# print("router.urls: ", router.urls)
# urlpatterns += router.urls
