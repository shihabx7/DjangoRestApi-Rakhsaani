from django.urls import path
from .views import *

urlpatterns = [
    path('',LanguageList.as_view())
]