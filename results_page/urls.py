from django.urls import path
from .views import *

urlpatterns = [
    path('', display_all_results, name='display_all_results'),
    path('user/', display_user_results, name='display_user_results'),
    # Add other urlpatterns as needed
]
