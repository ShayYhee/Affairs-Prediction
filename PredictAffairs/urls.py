from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name = 'PredictAffairs-home'),
    path('predictions/', views.predictions, name = 'PredictAffairs-predictions')
]