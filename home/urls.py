from django.urls import path
from .views import *

app_name='home'
urlpatterns = [
    path('connect/<operation>/<int:pk>/', change_friends, name='change_friends'),
    path('katil/<int:id>/',katil_post,name='katil_post'),

]