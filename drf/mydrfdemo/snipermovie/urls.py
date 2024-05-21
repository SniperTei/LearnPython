from django.urls import path, include
# from .views import MovieListAPIView, MovieDetailAPIView

urlpatterns = [
  # path('movies/', MovieListAPIView.as_view(), name='movie-list'),
  # path('movies/<int:pk>/', MovieDetailAPIView.as_view(), name='movie-detail'),
  path('snipermovie/', include('snipermovie.movie.urls')),
  path('snipermovie/', include('snipermovie.accounts.urls')),
]

# from django.urls import path, include

# urlpatterns = [
#     path('posts/', include('myapp.posts.urls')),
#     path('comments/', include('myapp.comments.urls')),
#     path('users/', include('myapp.users.urls')),
# ]
