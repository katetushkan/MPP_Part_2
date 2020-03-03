from django.contrib import admin
from django.urls import include, path


from django.urls import path

from manager import views


urlpatterns = [
    path('', views.ListTask.as_view(), name='main'),
    path('<int:pk>', views.DetailTask.as_view()),
]