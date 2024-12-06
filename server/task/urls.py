from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.predict_priority_view, name='predict_priority'),
    path('tasks/<int:task_id>/', views.task_detail_view, name='task_detail'),
]