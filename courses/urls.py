from django.urls import path
from . import views as v

from tests import views as tv

urlpatterns = [
    path('create', v.CourseCreateAPIView.as_view()),
    path('all', v.CourseListAPIView.as_view()),
    path('<int:pk>', v.CourseDetailAPIView.as_view()),

    path('<int:pk>/test/all', tv.TestListAPIView.as_view()),
    path('<int:pk>/video/all', tv.VideoListAPIView.as_view()),
]
