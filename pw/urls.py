from . import views
from django.urls import path


app_name = 'pw'

urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('about/', views.about_view, name='about')
]