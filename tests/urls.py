from django.urls import path
from . import views

urlpatterns = [
    path('create', views.TestCreateAPIView.as_view()),
    path('all', views.TestListAPIView.as_view()),
    path('<int:pk>', views.TestDetailAPIView.as_view()),
    path('course/<int:pk>', views.TestByCourseAPIView.as_view()),

    path('video/create', views.VideoCreateAPIView.as_view()),
    path('video/all', views.VideoListAPIView.as_view()),
    path('video/<int:pk>', views.VideoDetailAPIView.as_view()),
    path('course/video/<int:pk>', views.VideoByCourseAPIView.as_view()),
]
