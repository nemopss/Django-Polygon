from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='main'), # http://127.0.0.1:8000/
    path('learn', learn, name='learn'), # http://127.0.0.1:8000/learn
    path('registry/', RegisterUser.as_view(), name='registry'), # http://127.0.0.1:8000/registry
    path('auth', auth, name='auth'), # http://127.0.0.1:8000/learn

]