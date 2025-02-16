from django.urls import path
from . import views

urlpatterns = [
    path('', views.domu, name='domu'),
    path('tabulka/', views.tabulka, name='tabulka'),
    path('seznam_tymu/', views.seznam_tymu, name='seznam_tymu'),
    path('team/<int:team_id>/', views.soupiska_hracu, name='soupiska_hracu'),
]
