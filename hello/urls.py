from . import views
from django.urls import path


urlpatterns = [
    path('index/', views.index_view, name='index'),
    path('turma/', views.turma_view, name='turma')
]