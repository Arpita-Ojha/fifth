from django.urls import path
from app1.views import*

app_name='name1'

urlpatterns=[
    path('kim/',kim,name='kim'),
]