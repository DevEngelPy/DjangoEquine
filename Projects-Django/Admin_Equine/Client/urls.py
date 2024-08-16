from Client import views
from django.urls import path

app_name = 'Clients'

urlpatterns = [
    path('', views.list_client,name='clients'),
]
