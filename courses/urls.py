from django.urls import path
from . import views as v

<<<<<<< HEAD
# from tests import views as tv
from tests.views import TestListAPIView
=======
from my_tests import views as tv
>>>>>>> 31d711533d7cce1ecaee041770751698dabf2a18
from videos import views as vv

urlpatterns = [
    path('create', v.CourseCreateAPIView.as_view()),
    path('all', v.CourseListAPIView.as_view()),
    path('<int:pk>', v.CourseDetailAPIView.as_view()),

    path('<int:pk>/test/all', TestListAPIView.as_view()),
    path('<int:pk>/video/all', vv.VideoListAPIView.as_view()),
]
