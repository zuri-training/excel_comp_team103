from django.urls import path
from . import views

app_name = 'contact_page'
urlpatterns = [
    path('', views.contact_us, name='contact_us'),
]