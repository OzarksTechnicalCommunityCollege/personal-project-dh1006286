from django.urls import path
from . import views

app_name = 'study'

urlpatterns = [
    path('', views.set_collection, name='set_collection'),
    path('<int:id>/', views.view_cards, name='view_cards')
]