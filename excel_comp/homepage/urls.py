from django.urls import path
from . import views

app_name = 'homepage'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('404_Page_Not_Found', views.page_not_found, name='not_found')
]