from django.urls import path
from userhome import views

app_name = 'userhome'
urlpatterns = [
    path('uhome/', views.home, name='userhome'),
]