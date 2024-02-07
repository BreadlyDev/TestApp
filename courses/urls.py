from django.urls import path
from . import views

urlpatterns = [
    path('create', views.CourseCreateAPIView.as_view()),
    path('all', views.CourseListAPIView.as_view()),
    path('<int:pk>', views.CourseDetailAPIView.as_view()),
]
