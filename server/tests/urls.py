from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('candidate_viewset', views.CandidateViewSet, basename='candidate_viewset')

router1 = DefaultRouter()
router1.register('candidate_generic_viewset', views.CandidateGenericViewSet, basename='candidate_generic_viewset')

router2 = DefaultRouter()
router2.register('candidate_model_viewset', views.CandidateModelViewSet, basename='')

urlpatterns = [
    path('test_list', views.test_list, name='test_list'),
    #path('candidate_list', views.candidate_list, name='candidate_list'),
    path('candidate_list', views.CandidateListAPIView.as_view(), name='candidate_list'),
    path('candidate_generic/<int:id>/', views.GenericAPIView.as_view(), name='candidate_generic'),
    path('candidate_viewset', include(router.urls), name='candidate_viewset'),
    path('candidate_viewset/<int:pk>/', include(router.urls), name='candidate_viewset'),
    path('candidate_generic_viewset', include(router1.urls), name='candidate_generic_viewset'),
    path('candidate_model_viewset', include(router2.urls)),
    #path('candidate_detail/<int:pk>/', views.candidate_detail, name='candidate_detail'),
    path('candidate_detail/<int:id>/', views.CandidateDetailAPIView.as_view(), name='candidate_detail'),
]
