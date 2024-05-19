from django.urls import path
from .views import CustomUserView

urlpatterns = [
  # path('movies/', MovieListView.as_view(), name='movie-list'),
  # path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
  path('users/', CustomUserView.as_view(), name='user-list'),
  # path('users/<int:pk>/', CustomUserDetailView.as_view(), name='user-detail'),
]
