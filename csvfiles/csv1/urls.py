from django.urls import path
from .import views

#app_name='csv1'
urlpatterns=[
    path('',views.product)
]