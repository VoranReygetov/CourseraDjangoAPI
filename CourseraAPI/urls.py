from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken.views import obtain_auth_token

# from rest_framework.routers import SimpleRouter
# router = SimpleRouter(trailing_slash=False)
# router.register('books', views.BookView, basename='books')


urlpatterns = (
[   path('__debug__/', include('debug_toolbar.urls')),
    path('books', views.BookView.as_view()),
    path('books/<int:pk>',views.SingleBookView.as_view(), name='book-detail'),
    path('genre/<int:pk>',views.GenreView.as_view(), name='genre-detail'),
    path('books-url',views.BookUrlView.as_view(), name='book-url-detail'),
    path('book-genre-name',views.BookGenreView.as_view(), name='book-url-detail'),
    path('books_list',views.booklist),
    path('welcome',views.welcome),
    path('api-token-auth', obtain_auth_token),
    path('manager/users', views.manager),
    path('ratings', views.RatingsView.as_view()),

#     path('books/', views.BookView.as_view({
#         'get': 'list',
#         'post': 'create',
#     })),
#     path('books/<int:pk>', views.BookView.as_view({
#         'get': 'retrieve',             # Retrieve a specific book
#         'put': 'update',               # Update a specific book
#         'patch': 'partial_update',     # Partially update a specific book
#         'delete': 'destroy',           # Delete a specific book
#     })),
])