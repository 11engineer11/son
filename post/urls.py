
from django.urls import path
from .views import *
from django.conf.urls import url
app_name='post'
urlpatterns = [
    path('<int:id>/', post_detail, name='detail'),
    path('<int:id>/', post_detay, name='detay'),
    path('index/',post_index),
    path('create/',post_create),
    path('<int:id>/delete',post_delete,name='delete'),
    path('<int:id>/update/',post_update,name='update'),
    path('katilim/',post_katilim,name='katilimci'),

   
]
