from django.urls import path
from app.views.dashboard import dashboard

urlpatterns = [
    path('', dashboard, name='dashboard'),
]
