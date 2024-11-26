from django.urls import path
from .views import *

urlpatterns = [
    path('<str:language>/',SurahList.as_view()),
    path('<int:pk>/<str:language>/',SurahDetails.as_view()),
]