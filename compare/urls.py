from django.urls import path
from . import views

app_name = 'compare'
urlpatterns = [
    path('compare/', views.compare, name='compare'),
    path('upload/', views.upload, name="upload"),
    path('dashboard/', views.dashboard, name='dashboard'),
]