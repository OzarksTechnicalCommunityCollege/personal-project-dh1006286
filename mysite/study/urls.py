from django.urls import path
from . import views

app_name = 'study'

urlpatterns = [
    path('', views.StudyListView.as_view(), name='set_collection'),
    path('<slug:slug>/', views.view_cards, name='view_cards'),
    path('<int:set_id>/add/', views.make_card, name='make_card')
]