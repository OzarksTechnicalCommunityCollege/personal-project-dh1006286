from django.urls import include, path
from django.contrib.sitemaps.views import sitemap
from . import views
from study.sitemaps import SetSiteMap
from django.contrib.auth import views as auth_views

sitemaps = {'sets': SetSiteMap,}

app_name = 'study'

urlpatterns = [         
    path('register/', views.register, name='register'),
    path('addSet/', views.make_set, name='make_set'),
    path('', views.view_sets, name='set_collection'),    
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('<slug:slug>/', views.view_cards, name='view_cards'),
    path('<int:set_id>/add/', views.make_card, name='make_card'),
    path('<slug:tag_slug>/', views.view_sets, name='set_collection_by_tag'),
    path('<int:set_id>/game/', views.start_game, name='start_game'),
    path('<int:card_id>/<int:set_id>/', views.edit_card, name='edit_card'),
]