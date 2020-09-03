from django.urls import path

from . import views

urlpatterns = [
    path('test_list', views.test_list, name='test_list'),
    #path('candidate_list', views.candidate_list, name='candidate_list'),
    path('candidate_list', views.CandidateListAPIView.as_view(), name='candidate_list'),
    path('candidate_generic/<int:id>/', views.GenericAPIView.as_view(), name='candidate_generic'),
    #path('candidate_detail/<int:pk>/', views.candidate_detail, name='candidate_detail'),
    path('candidate_detail/<int:id>/', views.CandidateDetailAPIView.as_view(), name='candidate_detail'),
]
