from django.urls import include, path
from . import views




app_name = 'api'

urlpatterns = [         
    path('', views.fetch_osrs_data, name='osrs_data'),
]