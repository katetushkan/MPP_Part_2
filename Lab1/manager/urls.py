from django.urls import path

from manager import views

urlpatterns = [
    path('', views.MainView.as_view(), name='main'),
    path('task/<int:pk>/edit', views.TaskUpdateView.as_view(), name='update_task'),
    path('task/<int:pk>/delete', views.TaskDeleteView.as_view(), name='delete_task'),
    path('task/create', views.TaskCreateView.as_view(), name='create_task')
]
