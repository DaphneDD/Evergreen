from django.urls import path

from . import views

urlpatterns = [
    path('test_list', views.test_list, name='test_list'),
]