from django.urls import path
from app1.views import *

app_name='rish'
urlpatterns=[
    path('jangam/',jangam,name='jangam'),
]