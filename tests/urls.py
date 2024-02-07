from django.urls import path
from . import views

urlpatterns = [
    path('create', views.TestCreateAPIView.as_view()),
    path('all', views.TestListAPIView.as_view()),
    path('<int:pk>', views.TestDetailAPIView.as_view()),

    path('video/create', views.TestCreateAPIView.as_view()),
    path('video/all', views.TestListAPIView.as_view()),
    path('video/<int:pk>', views.TestDetailAPIView.as_view()),
]
