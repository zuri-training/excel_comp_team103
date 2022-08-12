from django.urls import path
from . import views

app_name = 'compare'
urlpatterns = [
    path('', views.unauth, name='unauth'),
    path('upload/', views.upload, name="upload"),
    path('dashboard/', views.userDashboard, name='dashboard'),
]