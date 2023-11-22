from django.urls import path
from app2.views import *
app_name='prashu'

urlpatterns=[
    path('response/',response,name='response'),
]
