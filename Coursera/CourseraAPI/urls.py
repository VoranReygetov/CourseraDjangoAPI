from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter


# from rest_framework.routers import SimpleRouter
# router = SimpleRouter(trailing_slash=False)
# router.register('books', views.BookView, basename='books')


urlpatterns = (
[   path('__debug__/', include('debug_toolbar.urls')),
    path('books', views.BookView.as_view()),
    path('books/<int:pk>',views.SingleBookView.as_view(), name='book-detail'),
    path('genre/<int:pk>',views.GenreView.as_view(), name='genre-detail'),
    path('books_list',views.booklist),
    path('welcome',views.welcome),
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