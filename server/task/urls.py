from django.urls import path
from .views import predict_priority_view

urlpatterns = [
  path("predict-priority/", predict_priority_view, name="predict-priority")
]