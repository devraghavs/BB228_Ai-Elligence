from django.urls import path
from . import views

# r'^/blog/(?P<id>\d+)/$'
r'^drinks/(?P<drink_name>\D+)/'
urlpatterns = [
    path('',views.findTrains,name='find-trains'),
    path('showTrains/book_ticket/<int:id>',views.book_ticket,name='book-ticket'),
    path('showTrains/',views.showTrains,name='show-trains')

]