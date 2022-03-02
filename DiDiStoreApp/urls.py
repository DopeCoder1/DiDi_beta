from unicodedata import name
from django.urls import path
from .views import *

urlpatterns = [
    path("",index, name="home"),
    path('category/<int:id>/', show_category, name='category'),
    path("detail/<int:bookid>/",show_book, name="detail"),
    path('cart/', cart_details, name='cart_details'),
	path('add/<int:bookid>', cart_add, name='cart_add'),
	path('remove/<int:bookid>', cart_remove, name='cart_remove'),
	path('update/<int:bookid>/<int:quantity>', cart_update, name='cart_update'),

    path("cab/", my_cab,name="cab"),
    path("out/", logout,name="out")
]
