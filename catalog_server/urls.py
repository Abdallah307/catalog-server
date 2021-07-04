from django.urls import path
from .views import search_book_by_topic, book_details, update_book

urlpatterns = [
    path('search/<str:topic>', search_book_by_topic, name='search_by_topic'),
    path('info/<int:pk>', book_details, name='book-details'),
    path('update/<int:pk>', update_book, name='update_book'),
]