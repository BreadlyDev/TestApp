from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views as v

from main.settings import DEBUG

urlpatterns = [
    path('', v.main_view, name='home'),
    path('course/<int:pk>', v.course_view, name='course'),
    path('test/<int:pk>', v.test_view, name='test'),
    path('login', v.login, name='login'),
]

if DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
