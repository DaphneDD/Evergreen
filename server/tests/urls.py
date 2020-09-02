from django.urls import path

from . import views

urlpatterns = [
    path('test_list', views.test_list, name='test_list'),
    path('candidate_list', views.candidate_list, name='candidate_list'),
    path('candidate_detail/<int:pk>/', views.candidate_detail, name='candidate_detail'),
]
